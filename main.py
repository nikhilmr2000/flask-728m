from flask import Flask, jsonify
import os
import sys

import pickle
import numpy as np
import re

app = Flask(__name__)
 
@app.route('/predict',methods=["POST"])
def hello_world():
    ypred=""
    l=[]
    if request.method=="POST":
        model = pickle.load(open("salary_predict.pkl", 'rb'))
        content=request.get_json()
        l.append(content["exp"])
        ypred=model.predict(np.array(l).reshape(-1,1))[0]
        ypred=stringconverter(str(ypred))
    return ypred
 
def stringconverter(name):
    count=0
    new_string=""
    for i in range(0,len(name)):
        if(name[i]=='.'):
            count=1
        if(count==0):
           new_string+=name[i]  
    return new_string
    
# main driver function
if __name__ == '__main__':
    app.run()
