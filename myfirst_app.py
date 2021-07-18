import streamlit as st
import pandas as pd



header = st.beta_container()
dataset = st.beta_container()
faetuers = st.beta_container()
model_training = st.beta_container()


with header:
    st.title('Welcome to my first app data scinece')
    st.text('In this project I look into transaction of texis in NYC...')


with dataset:
    st.header('NYC texi dataset')
    st.text('I found this dataset on blalalal.com')

    texi_data = pd .read_csv('data\ texi_data.csv')
    st.write(texi_data.head())

    st.subheader('Pick-up location ID distribuion on the NYC dataset ')
    pulocation_data = pd.Dataframe(texi_data['PULocationID'].value_counts()).head(50)
    st.bar_chart(pulocation_data)


with faetuers:
    st.header('This faetuers I created ')


with model_training:
    st.header('Time to train the model!')
    st.text('Here you get to chooes the hyperparameters of the model and see how the performance change')


