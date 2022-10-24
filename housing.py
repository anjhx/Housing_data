import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('California housing data (1990) by Linjie Zhou')
df = pd.read_csv('housing.csv')

# add a slider
housingvalue_filter = st.slider('Median House Price', 0 , 500001, 200000)



# show the map
st.header('See more filters in the sidebar')



# add a sidebar
location_filter = st.sidebar.multiselect(
     'Choose the location type',
     df.ocean_proximity.unique(),  # options
     df.ocean_proximity.unique() # defaults
)



genre = st.sidebar.radio(
    'Choose income level',
    ('Low', 'Medium', 'High'))



st.map(df)

# show the plot
st.subheader('Histogram of the Median House Value')
df = df[df.median_house_value <= housingvalue_filter]


fig,ax = plt.subplots(figsize = (20,15))
house = df.median_house_value.hist(bins = 30)
st.pyplot(fig)




