import csv
import os
from werkzeug.utils import secure_filename
from datetime import datetime
from flask import Flask,render_template,request
from flask import redirect,url_for
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import io
import base64
from flask import jsonify
from flask import session
import pandas as pd
# from pandas_profiling import ProfileReport




ALLOWED_EXTENSIONS=set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app=Flask(__name__)
app.secret_key = 'my-secret-key'


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


@app.route("/click")    #javascript's windows href is added
def visualize():
    folder = "./input/"
    filepath = os.listdir(folder)
    (filename)=filepath[0]
    filepath=os.path.join(folder,filename)
    dataset=pd.read_csv(filepath)
    num_rows=dataset.shape[0]
    num_cols=dataset.shape[1]
    cat_cols=dataset.select_dtypes(exclude="number").columns
    discrete_cols=dataset.select_dtypes(include="number").columns
    num_cat_cols=len(cat_cols)
    num_discrete_cols=len(discrete_cols)
    num_null = dataset.isnull().sum().sum()
    stats=dataset.describe()
    columns=dataset.columns
    
    
    #drawing graphs
    sns.set_palette('tab10')
    fig,axes=plt.subplots(5,3,figsize=(16,20))
    axes=axes.flatten()
    ax_no=0
    for col in discrete_cols:
        sns.histplot(data=dataset,x=col,bins=25,kde=True,ax=axes[ax_no])
        ax_no+=1
    pngImage = io.BytesIO()
    fig.savefig(pngImage, format='png')
    pngImageB64 = base64.b64encode(pngImage.getvalue()).decode('utf8')
    
    
    
    
    # drawing cat_cols
    fig,axes=plt.subplots(5,2,figsize=(15,25))
    palettes=['viridis','Set1','prism','rocket']
    axes=axes.flatten()
    ax_no=0
    for col in cat_cols:
        sns.set_palette(palettes[ax_no%4])
        sns.histplot(data=dataset,x=col,bins=25,kde=True,ax=axes[ax_no])
        ax_no+=1
    fig.suptitle("Distibution of Continuous features")
    pngImage2 = io.BytesIO()
    fig.savefig(pngImage2, format='png')
    pngImage2B64 = base64.b64encode(pngImage2.getvalue()).decode('utf8')
    
    
    
    

    return render_template("vizeda.html",var1=num_cols,var2=num_rows,var3=num_cat_cols,var4=num_discrete_cols,var5=num_null,columns=columns,image1=pngImageB64,var6=cat_cols,var7=discrete_cols) 

@app.route('/processdata', methods=['POST'])
def processdata():
    data = request.get_json()
    clicked_buttons_array = data['clicked_buttons_array']
    targetattribute=data['targetvalue']
    session['clicked_buttons_array']=clicked_buttons_array
    session['targetattribute']=targetattribute
    return redirect('/FeatureEngineering', code=307)
   

@app.route('/FeatureEngineering', methods=['POST'])
def FeatureEngineering():
    folder = "./input/"
    filepath = os.listdir(folder)
    (filename)=filepath[0]
    filepath=os.path.join(folder,filename)
    dataset=pd.read_csv(filepath)
    cat_cols=dataset.select_dtypes(exclude="number").columns
    discrete_cols=dataset.select_dtypes(include="number").columns
    clicked_buttons_array = session.get('clicked_buttons_array')
    targetattribute=session.get('targetattribute')
    #perform preprocessing  and
    # Now train the model
    
    #under prepro
    
    sample_data_cols=clicked_buttons_array
    print(sample_data_cols)
    train_dataset=dataset[sample_data_cols]
    train_dataset.dropna()
    print(train_dataset)
    
    
    
    
    
    
    return render_template('FeatureEngineering.html',dataset_cols=clicked_buttons_array,targetattribute=targetattribute)
    
    
    
    
    



if __name__=="__main__":
    app.run(debug=True)
    
    


