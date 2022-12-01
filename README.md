# Disease-Prediction
Symptom based Disease Prediction
1) First we import the required libraries needed for the model
2) We read the disease-symptoms data using pandas and store it in a dataframe
3) The Data has a lot of null values and values with different symbols which cannot be read by the algorithm. So, we perform data pre-processing to prepare the data
4) As the ratio of null values is increasing rapidly with the the number of symptoms, we addressed the issue by replacing the missing symptoms with 0
5) We have the data of different kinds of diseases and the symptoms associated with each of those diseases. The Symptoms are categorical values, we will not be able to perform calculations on the categorical values, so we assign weights to each of the symptoms
6) We use numerically assigned weights to give as input to the model for computation
7) Once we have a complete dataset, we shuffle the dataset so as to redistribute different values across the dataset and then split the dataset in to test and train datsets
8) Now we train multiple algorithms using the train datasets and test them against the test dataset and select the best fit based on the accuracy
9) Once the model is ready, we read the input from the user and predict the value based on the model and display it back to the user

Execution:
1) open terminal and go to the folder path and type "jupyter notebook"
2) Open "disease_prediction.ipynb" and run all the python scripts
3) open another terminal window and in the same folder path type "python app.py" and run the command
4) Open the default localhost 5000 port
5) Give the Symptoms as inputs using the drop-down menu options and click submit to recieve the prdecited disease

Installation of certain libraries might be required 
Run the following commands to install the libraries in the local machine


"pip install numpy"
"pip install pandas"
"pip install scikit-learn"
"pip install matplotlib"
"pip install seaborn"
"pip install xgboost"
