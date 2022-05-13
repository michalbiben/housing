import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

st.title('California Housing Data (1990) by Michal Biben')

df = pd.read_csv('housing.csv')

median_p_filter = st.slider('Median House Price', 0, 501000, 200000)

proximity_filter = st.sidebar.multiselect('Choose the location type', df.ocean_proximity.unique(), df.ocean_proximity.unique())

income_filter = st.sidebar.radio('Choose icome level', ['Low', 'Medium', 'High'])
income_filter

if income_filter == 'Low':
    df = df[df.median_income<2.5]
elif income_filter == 'Medium':
    df = df[(df['median_income'] > 2.5) & (df['median_income'] < 4.5)]
elif income_filter == 'High':
    df = df[df.median_income>4.5]

df = df[df.median_house_value>median_p_filter]
df = df[df.ocean_proximity.isin(proximity_filter)]

st.map(df)

st.subheader('Histogram of the Median House Value')
fig, ax = plt.subplots(figsize=(20, 10))
histogram = df.median_house_value.hist(bins=30)
histogram.plot(ax=ax)
st.pyplot(fig)
