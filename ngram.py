from nltk import ngrams
import math
import json
import collections
import itertools

coverletterList = []

numberOfGrams = 3

def ejectLetters():

    f = open('letters_rinat.json')
    _letterList = json.loads(f.readlines()[0])

    wordlist = set()

    for i in range(len(_letterList)):
        wordlist.add(_letterList[i]['coverLetter'])

    return wordlist

def slicetext(n = numberOfGrams):

    slicedLetters = list()
    for letter in ejectLetters():
        letter = list(ngrams(letter.split(), n))
        joinedLeter = set()
        for i in letter:
            joinedLeter.add(" ".join(i))
        slicedLetters.append(joinedLeter)

    return slicedLetters

def differences(phrasesList):
    ngramcCounter = dict()
    for letter in range(len(phrasesList)):
        for i in range(len(phrasesList)):
            tempListOfIntersections = list(phrasesList[letter].intersection(phrasesList[i]))
            tempChecker = dict()
            for  ngram in tempListOfIntersections:
                try:
                    ngramcCounter[ngram]['phraseMentions'].append(i)

                except:
                    ngramcCounter[ngram] = {'phraseCounter' : int(0), 'phraseMentions' : [i]}

    for i in (ngramcCounter):
        ngramcCounter[i]['phraseMentions'] = dict(collections.Counter(ngramcCounter[i]['phraseMentions']))
        tempMax = max(ngramcCounter[i]['phraseMentions'], key=ngramcCounter[i]['phraseMentions'].get)
        tempMin = min(ngramcCounter[i]['phraseMentions'], key=ngramcCounter[i]['phraseMentions'].get)
        ngramcCounter[i]['phraseCounter'] = ngramcCounter[i]['phraseMentions'][tempMax]
        ngramcCounter[i]['phraseMentions'] = list(collections.Counter(ngramcCounter[i]['phraseMentions']))

    return (ngramcCounter)


#
# def restoreText (text):
#     # print (text)
#     listOfNgrams = []
#     newPhrasesList = []
#     for i in text:
#         temp = (list(i))
#         for j in range(len(temp)):
#             temp[j] = temp[j].split()
#
#         listOfNgrams.append(temp)
#
#     for gramsList in listOfNgrams:
#         for gram in range(len(gramsList)):
#             for i in range(len(gramsList)):
#                 if (gramsList[gram][:(numberOfGrams-1)]) ==  (gramsList[i][(len(gramsList[i])-(numberOfGrams-1)):]):
#                     temp = (list(itertools.chain.from_iterable([gramsList[i],gramsList[gram][(numberOfGrams-1):]])))
#                     gramsList[gram] = temp
#                     newPhrasesList.append(" ".join(temp))
#     print ((dict(collections.Counter(newPhrasesList))))
#     print (list(dict(collections.Counter(newPhrasesList))))
#
#     for i in ((dict(collections.Counter(newPhrasesList)))):
#         print (i)
#
#     return (dict(collections.Counter(newPhrasesList)))

def intersect():
    slicedLetters = slicetext()
    listOfIntersections = []
    listOfDifferences = []
    listOfIntersections = differences(slicedLetters)
    # listOfphrases = restoreText(listOfIntersections)
    return listOfIntersections


def writeIntoFile():

    phrases = intersect()
    listOfDublicates = []
    for phrase in phrases:
        listOfDublicates += [(phrase)]

    f= open('result.txt', 'w+')
    while phrases:

        tempMaxMention = max(phrases, key=lambda i: phrases[i]['phraseCounter'])
        f.write('\"' + tempMaxMention + '\" - ' + str(phrases[tempMaxMention]['phraseCounter']) + str(phrases[tempMaxMention]['phraseMentions']) + '\n')
        del phrases[tempMaxMention]

    f.close()

if __name__ == "__main__":
    writeIntoFile()
