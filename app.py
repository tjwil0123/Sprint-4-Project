import pandas as pd
import streamlit as st
import plotly.express as px

vehicles_df = pd.read_csv('cleaned_vehicles.csv')

# set title
st.title('Vehicle Data Analysis')

# make scatter plot
st.header('Price vs Odometer Value')

# set checkbox
show_condition_color = st.checkbox('Color by Condition')

if show_condition_color:
    scatter_fig = px.scatter(vehicles_df, x='odometer', y='price', color='condition',
                             title='Price vs Odometer Value (Colored by Condition)',
                             labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)', 'condition': 'Condition'})
else:
    scatter_fig = px.scatter(vehicles_df, x='odometer', y='price',
                             title='Price vs Odometer Value',
                             labels={'odometer': 'Odometer (miles)', 'price': 'Price (USD)'})

st.plotly_chart(scatter_fig)

# make histogram
st.header('Distribution of Vehicle Conditions')

hist_fig = px.histogram(vehicles_df, x='condition', title='Vehicle Condition Distribution',
                        labels={'condition': 'Condition', 'count': 'Count'})

st.plotly_chart(hist_fig)