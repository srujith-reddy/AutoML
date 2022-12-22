import csv
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/",methods=['POST'])
def hello_world():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
  file = request.files['file']
  file.save('path/to/save/file.ext')
  return 'File uploaded successfully!'
  

if __name__=="__main__":
    app.run(debug=True)