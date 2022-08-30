from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
  val = 0
  req = requests.get('https://economia.awesomeapi.com.br/JSON/CAD-USD/7')
  dict_rec = req.json()
  c = dict_rec[0]['bid']
  print('home() was called')
  if request.method == 'POST':
    data = request.form
    a = data['in']
    if a == '':
      pass
    elif a != '':
      val = float(a)*float(c)
    
    
  
  return render_template('index.html', x=dict_rec, val=val)



if __name__ == '__main__':
  app.run(debug=True)