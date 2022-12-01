# import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import csv
import pandas as pd

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

data=pd.read_csv("Symptom-severity.csv")
test=[0]*17
symptoms = []


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms.append(request.form['symptom_1'])
    symptoms.append(request.form['symptom_2'])
    symptoms.append(request.form['symptom_3'])
    symptoms.append(request.form['symptom_4'])
    # symptoms.append(request.form['symptom_5'])
    # symptoms.append(request.form['symptom_6'])
    # symptoms.append(request.form['symptom_7'])
    # symptoms.append(request.form['symptom_8'])    

    for i in range(len(symptoms)):
        for j in range(len(data["Symptom"])):
            if symptoms[i] == data["Symptom"][j]:
                test[i] = data["weight"][j]
    
    prediction = model.predict([test])
    output = prediction[0]

    return render_template('index.html',prediction_text="You are suffering from {}".format(output))
    
    # output = round(prediction[0], 2)
    #return test[1]
    # return render_template('index.html', prediction_text='Employee Salary Should be $ {}'.format(output))

# @app.route('/predict_api', methods=['POST'])
# def predict_api():
#     data = request.get_json(force=True)
#     prediction = model.predict([np.array(list(data.values()))])
    
#     output = prediction[0]
#     return jsonify(output)

if __name__ == "__main__":
    app.run(debug = True)