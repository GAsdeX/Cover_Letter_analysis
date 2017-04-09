from nltk import ngrams
import math
import json
from collections import Counter
import itertools
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

coverletterList = []

numberOfGrams = 3

def ejectLetters():
    f = open('letters_rinat.json')
    _letterList = json.loads(f.readlines()[0])

    wordlist = list()

    for i in range(len(_letterList)):
        wordlist.append(_letterList[i]['coverLetter'])
    # print (wordlist)

    return wordlist

def slicetext(n = numberOfGrams):

    slicedLetters = list()

    for letter in ejectLetters():
        letter = list(ngrams(letter.split(), n))
        joinedLeter = list()

        for i in letter:
            joinedLeter.append(" ".join(i))

        slicedLetters.append(joinedLeter)
        del joinedLeter

    dictOfMentions = dict()
    x = list()
    y = list()

    begining = dict()
    ending = dict()

    for letter in slicedLetters:
        letterSize = len(letter)

        for ngram in (range(len(letter))):

            if dictOfMentions.get(letter[ngram]):
                dictOfMentions[letter[ngram]]['mentions'].append([ slicedLetters.index(letter), float(letter.index(letter[ngram])/letterSize)])

                begining[" ".join(letter[ngram].split()[1:])] = {'mentions' : [ slicedLetters.index(letter), letter.index(letter[ngram])/letterSize]}
                ending[" ".join(letter[ngram].split()[:2])] = letter[ngram]

            if not dictOfMentions.get(letter[ngram]):
                dictOfMentions[letter[ngram]] = {'mentions' : [ slicedLetters.index(letter), letter.index(letter[ngram])/letterSize]}
                begining[" ".join(letter[ngram].split()[1:])] = {'mentions' : [ slicedLetters.index(letter), letter.index(letter[ngram])/letterSize]}
                ending[" ".join(letter[ngram].split()[:2])] = letter[ngram]

    cehckEnd = True
    temp = ending
    prev = ending
    topPhrasesList = dict()

    # print (dictOfMentions)
    # print(json.dumps(dictOfMentions))
    # temp = json.dumps(dictOfMentions)
    # io = StringIO()
    # json.dump(['streaming API'], io)
    # io.getvalue()

    # print (json.dumps(dictOfMentions, separators=(',', ':')))
    # f = open("ngrams.json", "w+")
    # f.write(json.dumps(json.dumps(dictOfMentions, separators=(',', ':'))))
    # f.close()

    #
    dictOfPhrases = dict()
    for i in dictOfMentions:
        countTrigrams = len(dictOfMentions[i]['mentions'])
        if dictOfPhrases.get(countTrigrams):
            dictOfPhrases[countTrigrams].append([i , dictOfMentions[i]])
        if not dictOfPhrases.get(countTrigrams):
            dictOfPhrases[countTrigrams] = [i , dictOfMentions[i]]
    print (dictOfPhrases)


    words = list()
    dictOfPhrases = dict()

    while dictOfMentions:
        tempMaxtrigramMention = max(dictOfMentions,key=lambda i: len(dictOfMentions[i]['mentions']))
        words = tempMaxtrigramMention.split()

        # print (len(words))

        for i in range((len(words)-3)+1,(len(words)-3)+2):

            word1 = words[i]
            word2 = words[i+1]
            maxVal = 0
            temp = ''
            # print (word1, "--", word2)
            tempList = []
            for j in dictOfMentions:
                # j is string
                trigram = j.split()
                # print (trigram)

                if trigram[0] == word1 and trigram[1] == word2:
                    print (len(dictOfMentions[j]['mentions']))

                    # print (j,' == ',len(dictOfMentions[j]['mentions']))

                    listOfngrams = []
                    if len(dictOfMentions[j]['mentions']) > maxVal:
                        # print (dictOfMentions[j]['mentions'][1])
                        maxVal = len(dictOfMentions[j]['mentions'])
                        temp = trigram[2]
                        tempList.append(len(dictOfMentions[j]['mentions']))
                        # print ('    trigram = ',' '.join(trigram))
                        # print ('    temp = ', temp)
                        # print ()
                        listOfngrams.append(' '.join(trigram))
                        # print (Counter(listOfngrams))
            print (tempList)
                    # if Counter:
                    #     print (listOfngrams)

            # print ('champion = ', temp)
            words.append(temp)
            # print(words)
            # print (' '.join(temp))
            dictOfMentions[' '.join(words)] = dictOfMentions.pop(tempMaxtrigramMention)
            # del dictOfMentions[" ".join(temp)]

    temp = dictOfMentions
    dictOfMentions = dict()
    dictOfNgrams = dict()
    prevVal= 0

    return dictOfMentions



def writeIntoFile():
    phrases = intersect()
    f= open('result.txt', 'w+')

    while phrases:

        tempMaxMention = max(phrases, key=lambda i: phrases[i]['phraseCounter'])
        f.write('\"' + tempMaxMention + '\" - ' + str(phrases[tempMaxMention]['phraseCounter']) + str(phrases[tempMaxMention]['phraseMentions']) + '\n')


    f.close()

if __name__ == "__main__":
    slicetext()
