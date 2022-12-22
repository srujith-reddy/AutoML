import csv
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/upload', methods=['GET'])
def upload():
  file = request.files['name']
  file.save('path/to/save/file.ext')
  return 'File uploaded successfully!'
  

if __name__=="__main__":
    app.run(debug=True)
    