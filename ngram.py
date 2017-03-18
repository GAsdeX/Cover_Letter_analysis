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

def differences(phrasesList, computingDeph):
    if len(phrasesList) > 1:
        tempSample = set()
        tempList = []
        for letter in range(len(phrasesList)):
            if (letter == 0):
                pass
            if letter == 1:
                tempSample = (phrasesList[0].intersection(phrasesList[letter]))
            else:
                for i in range(len(phrasesList)):

                    if i != letter:
                        tempSample = ((phrasesList[i]).intersection(phrasesList[letter]))

                if len(tempSample) != 0:
                    tempList.append(tempSample)

        differences(tempList, computingDeph)
        return (tempList)


def restoreText (text):
    # print (text)
    listOfNgrams = []
    newPhrasesList = []
    for i in text:
        temp = (list(i))
        for j in range(len(temp)):
            temp[j] = temp[j].split()

        listOfNgrams.append(temp)

    for gramsList in listOfNgrams:
        for gram in range(len(gramsList)):
            for i in range(len(gramsList)):
                if (gramsList[gram][:(numberOfGrams-1)]) ==  (gramsList[i][(len(gramsList[i])-(numberOfGrams-1)):]):
                    temp = (list(itertools.chain.from_iterable([gramsList[i],gramsList[gram][(numberOfGrams-1):]])))
                    gramsList[gram] = temp
                    newPhrasesList.append(" ".join(temp))
    print ((dict(collections.Counter(newPhrasesList))))
    print (list(dict(collections.Counter(newPhrasesList))))

    for i in ((dict(collections.Counter(newPhrasesList)))):
        print (i)

    return (dict(collections.Counter(newPhrasesList)))

def intersect():
    slicedLetters = slicetext()
    listOfIntersections = []
    listOfDifferences = []
    listOfIntersections = differences(slicedLetters, len(slicedLetters))
    listOfphrases = restoreText(listOfIntersections)
    return listOfphrases


def writeIntoFile():

    phrases = intersect()
    listOfDublicates = []
    for phrase in phrases:
        listOfDublicates += [(phrase)]

    f= open('result.txt', 'w+')
    for i in listOfDublicates:
        f.write(str(i) + '\n')
    f.close()

if __name__ == "__main__":
    writeIntoFile()
