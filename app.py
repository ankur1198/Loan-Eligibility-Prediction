import joblib

import streamlit as st
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
#with open('D:\Ankur\Assignments\Loan Eligibility Prediction\decision_tree.pickle','rb') as f:
    #clf = pickle.load(f)

#with open('D:\Ankur\Assignments\Loan Eligibility Prediction\drandom_forest.pickle','rb') as f:
    #rc = pickle.load(f)
with open('C:\Final_Project\dm_forest.pickle','rb') as f:
    rc = pickle.load(f)


def prediction(Gender, Married,Dependents,Education,Self_Employed, LoanAmount, lat, Credit_History, Property_Area, Total_Income, EMI):   
 
    # Pre-processing user input    
    if Gender == "Male":
        Gender = 1
    else:
        Gender = 0
 
    if Married == "Unmarried":
        Married = 0
    else:
        Married = 1
    
    if Education == "Graduate":
        Education = 1
    else:
        Education = 0
    
    if Self_Employed == "Yes":
        Self_Employed = 1
    else:
        Self_Employed = 0

    if Credit_History == "Unclear Debts":
        Credit_History = 0
    else:
        Credit_History = 1 
    
    if Property_Area == "Urban":
        Property_Area = 1
    elif Property_Area == "Rural":
        Property_Area = 0
    elif Property_Area == "Semiurban":
        Property_Area = 2

    #Total_Income= ApplicantIncome + CoapplicantIncome
    #EMI = LoanAmount/ lat

    prediction = rc.predict( 
        [[Gender, Married, Dependents, Education,Self_Employed,LoanAmount,lat,Credit_History,Property_Area,Total_Income,EMI]])
    return prediction 
    


def main():
    st.title('Loan Eligibility Prediction System')
    Gender = st.selectbox('Gender',['Male','Female'])
    Married = st.selectbox('Marrital Status',['Married','Unmarried'])
    Dependents = st.number_input('Number of Dependents')
    Education = st.selectbox('Education',['Graduate','Not Graduate'])
    Self_Employed = st.selectbox('Self_Employed',['Yes','No'])
    ApplicantIncome = st.number_input('ApplicantIncome')
    CoapplicantIncome = st.number_input('CoapplicantIncome')
    LoanAmount = st.number_input('LoanAmount')
    lat = st.number_input('Loan_Amount_Term')
    Credit_History = st.selectbox('Credit_History',['Unclear Debt','CLeared Debt'])
    Property_Area = st.selectbox('Property_Area',['Urban','Rural','Semiurban'])
    Total_Income= ApplicantIncome + CoapplicantIncome
    EMI = LoanAmount/ lat
   

    if st.button('Predict'):
        result = prediction(Gender,Married,Dependents,Education,Self_Employed,LoanAmount,lat,Credit_History,Property_Area, Total_Income, EMI)
        if result==0:
            st.error('You are not Eligible for the Loan.')
        elif result==1:
            st.success('You are Eligible for the Loan.')


if __name__=='__main__':
    main()