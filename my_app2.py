import streamlit as st
import pickle
import pandas as pd
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OrdinalEncoder


st.sidebar.title('Car Price Prediction')
html_temp = """
<div style="background-color:green;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit ML Cloud App </h2>
</div>"""
st.markdown(html_temp, unsafe_allow_html=True)

cons=st.sidebar.slider("What is the fuel consumption of your car?", 3, 10, step=0.1)
fuel=st.sidebar.radio('Select fuel type',('Diesel', 'Benzine', 'LPG/CNG', 'Electric'))
age=st.sidebar.selectbox("What is the age of your car:",(0,1,2,3))
km=st.sidebar.slider("What is the km of your car", 0,350000, step=1000)
gearing_type=st.sidebar.radio('Select gear type',('Automatic','Manual','Semi-automatic'))
car_model=st.sidebar.selectbox("Select model of your car", ('Audi A1', 'Audi A3', 'Opel Astra', 'Opel Corsa', 'Opel Insignia', 'Renault Clio', 'Renault Duster', 'Renault Espace'))


richard_model=pickle.load(open("rf_model_new2","rb"))
richard_transformer = pickle.load(open('transformer2', 'rb'))


my_dict = {
    "age": age,
    "hp_kW": hp,
    "km": km,
    'Gearing_Type':gearing_type,
    "make_model": car_model
    "cons_comb": cons,
    "Fuel": fuel
    
}

df = pd.DataFrame.from_dict([my_dict])


st.header("The configuration of your car is below")
st.table(df)

df2 = richard_transformer.transform(df)

st.subheader("Press predict if configuration is okay")

if st.button("Predict"):
    prediction = richard_model.predict(df2)
    st.success("The estimated price of your car is €{}. ".format(int(prediction[0])))
    
