import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Visualization on Streamlit')

st.write('Please select which visualization you want to see.')

df = px.data.gapminder()

fig = px.bar(df, x="continent", y="pop",
  animation_frame="year", animation_group="country", range_y=[0,4000000000])

continent=st.button("Click here to show the population by continent")
if continent:
    st.write('Population by continent from 1952 to 2007')
    st.write(fig)
st.markdown('---')

chipotle = st.button('Click here to show the locations Chipotle in the USA')
dataf = pd.read_csv('chipotle_stores.csv')

if chipotle:
    st.write('Locations of Chipotle in the USA')
    st.map(dataf)
    st.write('The code I have used on Jupyter Notebook is different for this one.')
    st.write('In fact, Streamlit uses a very easy way to map the dataframe in no time.')
