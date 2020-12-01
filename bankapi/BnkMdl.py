
import os
import math
import pickle
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def pre_processing(data):
    data.drop('Loan_ID', axis=1, inplace=True)
    #data['Loan_Status'] = data['Loan_Status'].replace(['Y', 'N'], [1, 0])
    
    # Filling None Values
    data['Dependents'].fillna(0, inplace=True)
    data['LoanAmount'].fillna(data['LoanAmount'].mean(), inplace=True)
    data['Loan_Amount_Term'].fillna(360, inplace=True)
    data['Credit_History'].fillna(1.0, inplace=True)
    data['Gender'].fillna('Male', inplace=True)
    data['Married'].fillna('Yes', inplace=True)
    data['Self_Employed'].fillna('No', inplace=True)
    
    # Converting catagorical feature into numerical feature
    data['Gender'] = data['Gender'].replace(['Male', 'Female'], [1, 0])
    data['Married'] = data['Married'].replace(['Yes', 'No'], [1, 0])
    data['Education'] = data['Education'].replace(['Graduate', 'Not Graduate'], [1, 0])
    data['Self_Employed'] = data['Self_Employed'].replace(['Yes', 'No'], [1, 0])
    
    # One Hot Encoding
    data = pd.get_dummies(data)
    return data

def training(data):
    # Preprocessed dataset
    data = pre_processing(data)
    
    # Divide into feature and lable
    y = data['Loan_Status']
    data.drop('Loan_Status', axis=1, inplace=True)
    X = data
    
    dummyrow = pd.DataFrame(np.zeros(len(X.columns)).reshape(1, len(X.columns)), columns=X.columns)
    dummyrow.to_csv("dummyrow", index=False)
    # Spliting into training and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=8)
    
    # Build Model
    model = XGBClassifier()
    model.fit(X, y)

    # Picking our model
    pickel_file = "pickel_model.pkl"
    with open(pickel_file, 'wb') as files:
        pickle.dump(model, files)
    
    

def predict_result(ob):
    d1 = ob.to_dict()
    df = pd.DataFrame(d1, index=[0])
    #print(df.head()) 
    df.drop('Loan_Status', axis=1, inplace=True)
    df = pre_processing(df)
    #print(df)
    filepath = os.path.dirname(os.path.abspath(__file__))
    df2 = pd.read_csv(os.path.join(filepath, 'dummyrow'))   
    for c1 in df.columns:
        df2[c1] = df[c1]

    pklfile = os.path.dirname(os.path.abspath(__file__))
    pklpath = os.path.join(filepath, 'pickel_model.pkl')  
    #pickel_file = "pickel_model.pkl"
    with open(pklpath, "rb") as f:
        model = pickle.load(f)       
    pred = model.predict(df2)
    return pred


if __name__ == "__main__":
    workpath = os.path.dirname(os.path.abspath(__file__))
    data = pd.read_csv(os.path.join(workpath, 'banking.csv'))
    training(data)
    