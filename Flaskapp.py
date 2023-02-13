import csv
import pandas as pd
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import Flask,render_template,request
from flask import redirect,url_for

ALLOWED_EXTENSIONS=set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app=Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')



@app.route('/upload',methods=['POST'])
def upload():
    if request.method=='POST':
        file=request.files['uploaded_file']
        if file and allowed_file(file.filename):
            new_filename=secure_filename(file.filename)
            # new_filename=f'{filename.split(".")[0]}_{str(datetime.now())}.csv'
            file.save(os.path.join('input',new_filename))
        return redirect(url_for('index'))


@app.route("/dataset",methods=['GET'])
def index():
    folder = "./input/"
    filepath = os.listdir(folder)
    (filename)=filepath[0]
    filepath=os.path.join(folder,filename)
    dataset=pd.read_csv(filepath)
    with open(filepath) as f:
        reader = csv.reader(f)
        header = next(reader)
        data = list(reader)
    return render_template("app.html", header=header, data=data)



    
    
        

  

if __name__=="__main__":
    app.run(debug=True)
    