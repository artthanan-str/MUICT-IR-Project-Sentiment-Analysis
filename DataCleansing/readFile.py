import csv
import re

cleanedData = 'train = ['

print 'Start reading dataset from tsv file\n'
with open('RawData/dataset.tsv') as tsvfile:
  reader = csv.DictReader(tsvfile, dialect='excel-tab') # read tsv file
  for row in reader:
    text = re.sub(r'[\d+]', '', row['Phrase']) # Delete digit
    text = re.sub(r'[\t+]', '', text) # Delete \t
    text = re.sub(r'[\.+]', "", text) # Delete fullstop
    text = re.sub(r' +', " ", text) # Combine more spaces to single space

    cleanedData += '("'
    cleanedData += text
    cleanedData += '", "'
    cleanedData += row['Sentiment']
    cleanedData += '"),\n'

cleanedData = cleanedData[:-1] # delete the last \n
cleanedData = cleanedData[:-1] # delete the last ,
cleanedData += ']'

# write file in same path
f = open('cleanedDataset.py','w')
f.write(cleanedData)
f.close()

# write file into TrainingData Folder
file = open('C:/Users/artthanan/Desktop/IR-Project3/TrainingData/cleanedDataset.py', 'w')
file.write(cleanedData)
file.close()

print 'Finish correcting format and Cleaned dataset is saved'