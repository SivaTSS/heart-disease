import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

#iris dataset 3D plot in plotly

df = sns.load_dataset("iris")
st.write("""
# Iris dataset
The iris dataset is tabular dataset containing 5 columns with information about various species of iris.
""")
fig = px.scatter_3d(df, x="sepal_length", y="sepal_width", z="petal_length", color='species',\
                    size='petal_width', size_max=15, opacity=0.8, title='Iris dataset')
fig.update_layout(scene=dict(xaxis_title='sepal_length',yaxis_title='sepal_width',zaxis_title='petal_length'))
st.plotly_chart(fig, use_container_width=True)



#MPG dataset 3D plot in matplotlib

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = sns.load_dataset("mpg")
st.write("""
# MPG Dataset
""")
origins = df['origin'].unique()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for origin in origins:
    subset = df[df['origin'] == origin]
    scatter = ax.scatter(subset['horsepower'], subset['weight'], subset['mpg'], label=origin, s=subset['acceleration'], marker='o')

ax.set_xlabel('Horsepower')
ax.set_ylabel('Weight')
ax.set_zlabel('MPG')
ax.legend(title='Origin')
st.pyplot(fig)
