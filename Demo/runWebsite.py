from flask import Flask, request, render_template
import classifySentence
import showMostInfoFeatures
import re

app = Flask(__name__)
# nltk.download('punkt') # Add this code for first time
# nltk.download('stopwords') # Add this code for first time

# run the first page of website
@app.route('/')
def index():
	return render_template('index.html')

# do to classify the input sentence when button is hit
@app.route('/result', methods = ['GET', 'POST'])
def result():
	if request.method == 'POST':
		sentence = request.form['sentence']
	 	sentence = sentence.lower()
		result = classifySentence.classifySen(sentence)

		if str(result) == '1':
			with open('InputFromWeb/positiveInput.txt', 'a') as filetxt: filetxt.write(str(sentence) + "\n")
		else:
			with open('InputFromWeb/negativeInput.txt', 'a') as filetxt: filetxt.write(str(sentence) + "\n")

		return render_template('result.html', score = result, sent = sentence)

# show most features when button is hit
@app.route('/showFeatures', methods = ['GET', 'POST'])
def showFeatures():
	features = showMostInfoFeatures.showInfoFeatures()
	return render_template('showMostFeatures.html', text = features)

# show Pie Chart page when button is hit
@app.route('/showPieChart', methods = ['GET', 'POST'])
def showPiechart():
	labels = ["Positive", "Negative"]
	values = [7, 3]
	colors = ["#46BFBD", "#F7464A"]
	return render_template('showChart.html', set=zip(values, labels, colors))

# show positive sentence page when button is hit
@app.route('/showPositiveSen', methods = ['GET', 'POST'])
def showPositiveSen  ():
	textarray = []
	dummy = '.'
	with open('InputFromWeb/positiveInput.txt') as txtfile:
		for line in txtfile:
			line = re.sub(r'[\n+]', '', line)
			line = line.replace("\\", "")
			textarray.append(line)
	return render_template('showPositiveSen.html', text=textarray, fullstop = dummy)

# show negative sentence page when button is hit
@app.route('/showNegativeSen', methods = ['GET', 'POST'])
def showNegativeSen  ():
	textarray = []
	dummy = '.'
	with open('InputFromWeb/negativeInput.txt') as txtfile:
		for line in txtfile:
			line = re.sub(r'[\n+]', '', line)
			line = line.replace("\\", "")
			textarray.append(line)
	return render_template('showNegativeSen.html', text=textarray, fullstop = dummy)

if __name__ == '__main__':
   app.run(debug = True)
