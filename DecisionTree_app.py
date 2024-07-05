from plotly import hist_frame
import streamlit as st
import pickle
import numpy as np
model = pickle.load(open('model.pkl','rb'))

def diabetes_prediction(input_data):
  input_datas = np.asarray(input_data)
  input_reshaped = input_datas.reshape(1,-1)

  prediction = model.predict(input_reshaped)

  if(prediction[0]==0):
    return 'The Person is not diabetic'
  else:
    return 'The person is diabetic'


def main():
  Pregnancies=st.number_input('Pregnancies',0,10)
  Glucose=st.slider('Glucose',0,200)
  BloodPressure=st.number_input('BloodPressure',0,100)
  SkinThickness=st.slider('SkinThickness',0,50)
  Insulin=st.number_input('Insulin',0,200)
  BMI=st.slider('BMI',0,50)
  DiabetesPedigreeFunction=st.number_input('DiabetesPedigreeFunction',0,10)
  Age=st.slider('Age',0,100)


  diagnosis = ''

  if st.button("Diabetes Test Result"):
    diagnosis = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])

  st.success(diagnosis)

if __name__ == '__main__':
  main()



import pandas as pd
df=pd.read_csv('/content/diabetes.csv')
a=df["Age"]
if st.button("LINE_CHART_BUTTON"):
  st.line_chart(a)

a=df["Age"]
c=df["BMI"]
if st.button("SCATTER_CHART_BUTTON"):
  st.scatter_chart(df["Age"])

if st.button("BAR_CHART_BUTTON"):
  st.bar_chart(df["Age"])


st.balloons()


custom_css = ""
<style>
body{
  
}

