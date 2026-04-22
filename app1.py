# -*- coding: utf-8 -*-

# importing required libraries
import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib
     
# creating flask app
app = Flask(__name__)

# loading the trained model (saved earlier using joblib)
model = joblib.load(r"C:\Users\Admin\Desktop\Folder(All)\student mark prediction project\Student Mark Predictor Project Deployment\Student mark Predictor Deployment\Desktop.pkl")

# dataframe to store user inputs and predictions
df = pd.DataFrame()

# home page route
@app.route('/')
def home():
    # loads the main page
    return render_template('index.html')

# route for prediction
@app.route('/predict',methods=['POST'])
def predict():
    global df  # using global df to keep track of all predictions
    
    # getting input from form and converting to integer
    input_features = [int(x) for x in request.form.values()]
    
    # converting input into numpy array for model
    features_value = np.array(input_features)
    
    # checking if entered hours are valid
    if input_features[0] <0 or input_features[0] >24:
        return render_template('index.html', prediction_text='Please enter valid hours between 1 to 24 if you live on the Earth')
        
    # making prediction using model
    output = model.predict([features_value])[0][0].round(2)

    # storing input and output into dataframe
    df = pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    
    # printing dataframe in console (just for checking)
    print(df)   
    
    # saving all predictions to csv file
    df.to_csv('smp_data_from_app.csv')

    # sending result back to webpage
    return render_template('index.html', prediction_text='You will get [{}%] marks, when you do study [{}] hours per day '.format(output, int(features_value[0])))

# running the flask app locally
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000)

# this part can be used if deploying on server
#if __name__ == "__main__":
#    app.run(host='0.0.0.0', port=8080)