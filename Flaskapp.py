import csv
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import Flask,render_template,request

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
        return 'file uploaded succesfully'
        
        

  

if __name__=="__main__":
    app.run(debug=True)
    