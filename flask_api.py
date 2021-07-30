"""created on Sat 29July2021
@ author : Gaurav Patil
"""

from flask import Flask, request
import pandas as pd
import numpy as np
import pickle
import flasgger          # Lib to create beautiful frontend webApp,
                         # initially App was running without flasgger ( using URL editing and postman) but as we want to build webApp hence we have to do it with
from flasgger import Swagger



app = Flask(__name__)
Swagger(app)

pickle_in = open('classifier.pickle', 'rb')
clf = pickle.load(pickle_in)


@app.route('/')
def welcome():
    return "Welcom all"


@app.route(
    '/predict')  # by defaults method will be GET, to give inputs in browser manually give it in http..5000/predict?variance=2&skewness=3&curtosis=2&entropy=1
# n when you Enter the you will get "predicted values is [0]" output on browser
# /predict?variance=2&skewness=3&curtosis=2&entropy=1   these are the inputs that we r gonna give with GET method
def predict_note_authentication():
    """Let's Authenticate the Banks Note using mannual inputs
    This is using docstrings for specifications.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: true
      - name: skewness
        in: query
        type: number
        required: true
      - name: curtosis
        in: query
        type: number
        required: true
      - name: entropy
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values

    """
    variance = request.args.get('variance')
    skewness = request.args.get('skewness')
    curtosis = request.args.get('curtosis')
    entropy = request.args.get('entropy')
    predictioin = clf.predict([[variance, skewness, curtosis, entropy]])
    return f'predicted values is {str(predictioin)}'


@app.route('/predict_file',
           methods=["POST"])  # these are the inputs that we r gonna give with entire test_file with POST method
def predict_note_file():
    """Let's Authenticate the Banks Note using test csv file
       This is using docstrings for specifications.
       ---
       parameters:
         - name: file
           in: formData
           type: file
           required: true

       responses:
           200:
               description: The output values

       """
    df_test = pd.read_csv(request.files.get("file"))     # this name should be equal to name mentioned in 'type'  above.
    prediction = clf.predict(df_test)
    return f'predicted values for csv_file is {str(list(prediction))}'


if __name__ == '__main__':
    app.run()
