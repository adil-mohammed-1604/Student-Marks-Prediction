Student Marks Prediction System

This project is a simple machine learning-based web application that predicts student marks based on the number of hours they study per day. The model is trained using a dataset and deployed using Flask to provide real-time predictions.

Overview

The main idea behind this project is to understand how study hours affect academic performance. The system takes study hours as input and predicts the expected marks using a trained machine learning model.

The project also demonstrates how a machine learning model can be integrated into a web application.

Features

Predicts student marks based on study hours
Simple web interface using Flask
Real-time prediction
Input validation (0–24 hours)
Stores user inputs and predictions in a CSV file

Technologies Used

Python
Pandas, NumPy
Scikit-learn
Flask
Joblib
HTML

Project Structure

app1.py
Desktop.pkl
dataset.csv
Project(Adil).ipynb
smp_data_from_app.csv

templates/
index.html

static/
images/

Note

The file "dataset.csv" (student_info.csv) is the main dataset used to train the machine learning model. It contains the original data used for building the prediction system.

The file "smp_data_from_app.csv" is generated during runtime when a user interacts with the web application. It stores the user input (study hours) along with the predicted marks.

How to Run the Project

Install required libraries
pip install numpy pandas flask scikit-learn joblib
Run the application
python app1.py
Open browser
http://127.0.0.1:5000
Enter study hours and get prediction

Model Details

Algorithm used: Linear Regression
Input: Study Hours
Output: Predicted Marks

Limitations

Uses only one feature
Predictions are approximate
Model path is set for local system

Future Improvements

Add more features like attendance and sleep
Improve model accuracy
Deploy application online
Improve UI design

Author

Mohammed Adil
