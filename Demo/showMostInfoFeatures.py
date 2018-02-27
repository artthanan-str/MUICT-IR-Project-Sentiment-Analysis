import nltk
from trainedDataset import trainedData
import re

def showInfoFeatures():
    classifier = nltk.NaiveBayesClassifier.train(trainedData) # train data by using Naive Bayes Classifier

    text = classifier.most_informative_features(20) # show top 20 informative features
    text = str(text) # change type of text to string

    text = re.sub(r'[\W+]', '', text) # delete unnecessary character (non-alphabet)
    text = re.sub(r'True', ',\n', text) # change 'True' to new line
    text = re.sub(r'False', ',\n', text) # change 'False' to new line

    text = text[:-1] # delete last string
    text = text[:-1] # delete last string

    # the returned text will have only words
    return text

