import streamlit as st
import requests
st.title(" 📑Score Predictor ✅")
study=st.slider("Study Time",0,10)
atd=st.slider("Attended Days",0,80)
gen=st.selectbox("Gender",["Male","Female"])
gender=1 if(gen=="Male") else 0
if(st.button("Predict the score")):
    data={
        "study_time":study,
        "attendence":atd,
        "gender_Male":gender
    }
    res=requests.post("https://score-7ly9.onrender.com/predict",json=data)
    result=res.json()
    st.write("The Predict Score is",result['Predicted_score'])
