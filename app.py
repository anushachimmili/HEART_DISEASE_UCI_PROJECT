from flask import Flask,request, jsonify
from sklearn.externals import joblib
import pandas as pd
import numpy as np

app=Flask(__name__)

@app.route('/',methods=['POST'])

def notebook():
    data=request.get_json()
    data1=pd.DataFrame(data,columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal'])
    model_pred=np.array2string(model_load.predict(data1))
    return jsonify(model_pred)

if __name__=='__main__':
    model_load=joblib.load('./model/model_saved.sav')
    app.run(debug=True)