from nltk.tokenize import word_tokenize
from cleanedDataset import train as cleanedData # read cleaned data from cleanedDataset file
import time

startTime = time.clock() # set the start time

# create dictionary from dataset
print 'start creating dictionary\n'
dictionary = set(word.lower() for passage in cleanedData for word in word_tokenize(passage[0]))

# create training data
print 'start creating train set\n'
t = [({word: (word in word_tokenize(x[0])) for word in dictionary}, x[1]) for x in cleanedData]

# write dictionary into file and save at Demo folder
f = open('C:/Users/artthanan/Desktop/IR-Project3/Demo/dictionary.py', 'w')
f.write('dictionary = ' + str(dictionary))
f.close()

# write training data into file and save at Demo folder
a = open('C:/Users/artthanan/Desktop/IR-Project3/Demo/trainedDataset.py', 'w')
a.write('trainedData = ' + str(t))
a.close()

# show the time used
timeEnd = (time.clock() - startTime) # capture the stop time
print time.strftime("The total time used: %H:%M:%S", time.gmtime(timeEnd))
