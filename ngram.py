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
    listOfNgrams = list(list(text[i]) for i in range(len(text)))
    print (collections.Counter(list(itertools.chain.from_iterable(listOfNgrams))))
    # while True:
    #     i = 0
    # for gramsList in listOfNgrams:
    #     print (list(gramsList))
            # for gram in gramsList:
            #     print (gram)
            #     for i in
            #     if

def intersect():
    slicedLetters = slicetext()
    listOfIntersections = []
    listOfDifferences = []
    listOfIntersections = differences(slicedLetters, len(slicedLetters))
    # print (listOfIntersections)
    restoreText(listOfIntersections)
    return listOfIntersections


    # intersectedLetters = intersect()
    # if (intersectedLetters[:(numberOfGrams)])


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
    intersect()
