import nltk
from nltk.tokenize import word_tokenize
from dictionary import dictionary
from trainedDataset import trainedData
import time

def classifySen(sentence):
    startTime = time.clock() # set the start time

    classifier = nltk.NaiveBayesClassifier.train(trainedData) # train data by using Naive Bayes Classifier
    sentence = {word.lower(): (word in word_tokenize(sentence.lower())) for word in dictionary} # set sentence to lowercasem do tokenization and check word in dictionary

    result = classifier.classify(sentence) # classify sentence from classifier

    timeEnd = (time.clock() - startTime) # set the stop time

    print time.strftime("\nThe total time used for classifying sentence: %H:%M:%S\n", time.gmtime(timeEnd))

    return result
