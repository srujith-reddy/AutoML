import csv
from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world"


@app.route('/upload',methods=['POST'])
def create_file():
    file=request.files['file']
    reader = csv.reader(file)
    for row in reader:
         print(row)


if __name__=="__main__":
    app.run(debug=True)