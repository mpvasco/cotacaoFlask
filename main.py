from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route("/")
def home():
  print('home() was called')
  return render_template('index.html')

@app.route("/all")
def getAll():
  print('getAll() was called')
  quote = requests.get('https://economia.awesomeapi.com.br/json/all')
  quote_dict = quote.json()
  return render_template('all.html', x=quote_dict)


@app.route("/param", methods=['GET', 'POST'])
def param():
  print('param() was called')
  
  return render_template('param.html')


@app.route("/params/filter", methods=['GET', 'POST'])
def filter():
  print('filter() was called')
  # if request.method == 'POST':
  #   formsData = request.form
  #   de = formsData['de']
  #   para = formsData['para']
  #   quote = requests.get(f'http://economia.awesomeapi.com.br/json/last/{de}-{para}')
  #   print(quote)
  #   quote_dict = quote.json()
    
  #   return render_template('filter.html', x=quote_dict)
  return render_template('filter.html')

if __name__ == '__main__':
  app.run(debug=True)