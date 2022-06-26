import json
import streamlit as st
from streamlit_option_menu import option_menu
import requests

with st.sidebar:
    selected = option_menu('Menu',
    ['Home','Diabetes','Heart Disease'],default_index=0,
    icons=['house-door-fill','activity','heart'],
   
    )
if selected=='Home':
    st.title("Health Check")

if selected=='Diabetes':
    url = 'http://127.0.0.1:8000/diabetes_prediction'

    strin = "<h1 style='text-align: center; color:black;'>Diabetes Prediction</h1>"
    st.markdown(strin,unsafe_allow_html=True)
       
    #st.title("Diabetes Prediction")
    col1,col2 = st.columns(2)

    with col1:
        preg = st.text_input('Number of Pregnancies')
        glu = st.text_input("Glucose Level")
        ins = st.text_input('Insulin (mu U/ml)')
        dpf = st.text_input("Diabetes Pedigree Function value")


    with col2:
        age = st.slider('Age (Yrs)',15,100)
        bp = st.text_input('Blood Pressure (Diastolic)(mm Hg)')
        skt = st.text_input('Skin Thickness(Triceps skin fold)(mm)')
        bmi = st.text_input('BMI (Kg/m^2)')
    _,_,col3,_,_ = st.columns(5)  
    with col3:  
        state =st.button('Predict')

    if state:
        input_list ={
                'Pregnancies' : int(preg),
                'Glucose' :int(glu),
                'BloodPressure': int(bp),
                'SkinThickness' : int(skt),
                'Insulin' : int(ins),
                'BMI' : float(bmi),
                'DiabetesPedigreeFunction' : float(dpf),
                'Age' : int(age)
        }
        input_json =json.dumps(input_list)
        response = requests.post(url,data=input_json)
       
        string = "<h3 style='text-align: center; color:orange;'>"+str(response.text[1:-1])+"</h3>"
        st.markdown(string,unsafe_allow_html=True)
       

if selected=='Heart Disease':
    url = 'http://127.0.0.1:8000/heart_disease_prediction'

    strin = "<h1 style='text-align: center; color:black;'>Heart Disease Prediction</h1>"
    st.markdown(strin,unsafe_allow_html=True)
       
    #st.title("Diabetes Prediction")
    col1,col2 = st.columns(2)

    with col2:
        sex = st.selectbox('Sex',('Male','Female'))
        bp = st.text_input('Resting Blood Pressure(mm Hg)')
        fbs = st.selectbox('Fasting Blood Sugar',('Greater than 120mg/dl','Less than 120mg/dl'))
        mhr= st.text_input("Max Heart Rate")
        slope = st.selectbox("Peak Excercise ST segment",('Upslopping','Flat','Downsloping'))
        o = st.text_input("ST depression induced by excercise")


    with col1:
        age = st.slider('Age (Yrs)',15,100)
        cp = st.selectbox('Cheast Pain Type',('Typical angina','Atypical angina','Non-anginal Pain','Asymtotic'))
        sch = st.text_input('Serum cholestrol (mg/dl)')
        recg = st.selectbox("Resting ECG",('Normal','St-T wave abnormality','Left ventricular Hyperthropy'))
        eia = st.radio('Excercise Induced Angina',['Yes','No'])
        st.write('<style>div.row-widget.stRadio > div{flex-direction:row;}</style>', unsafe_allow_html=True)
        thal = st.selectbox('Thalssemia',('Normal','Fixed Defect','Reversible Defect'))
        oldpeak = st.text_input('Number of Major Vessels')

    _,_,col3,_,_ = st.columns(5)  
    with col3:  
        state =st.button('Predict')

    if state:
        input_list ={
                'Pregnancies' : int(preg),
                'Glucose' :int(glu),
                'BloodPressure': int(bp),
                'SkinThickness' : int(skt),
                'Insulin' : int(ins),
                'BMI' : float(bmi),
                'DiabetesPedigreeFunction' : float(dpf),
                'Age' : int(age)
        }
        input_json =json.dumps(input_list)
        response = requests.post(url,data=input_json)
       
        string = "<h3 style='text-align: center; color:orange;'>"+str(response.text[1:-1])+"</h3>"
        st.markdown(string,unsafe_allow_html=True)
       
    