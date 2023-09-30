import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache_data
def load_data():
    data = pd.read_csv("datasets/heart_failure.csv")
    return data

st.sidebar.title("EDA Options")

data = load_data()
data.dropna()
st.title("Heart Failure Dataset")
st.write("""
The heart failure dataset is a collection of medical data that offers critical insights on heart failure.

""")

age_range = st.sidebar.slider("Select Age Range", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
gender = st.sidebar.radio("Select Gender", ["All", "Male", "Female"])
    
st.header("Data Visualization")
filtered_data = data.copy()
filtered_data = filtered_data[(filtered_data['Age'] >= age_range[0]) & (filtered_data['Age'] <= age_range[1])]
if gender != "All":
    filtered_data = filtered_data[filtered_data['Sex'] == ("F" if gender == "Female" else "M")]

selected_features = st.multiselect("Select Features", ["RestingBP","Cholesterol","FastingBS","MaxHR","Oldpeak"])
g = sns.pairplot(filtered_data[selected_features+["Age","HeartDisease"]], hue="HeartDisease")

st.pyplot(g)

g = sns.FacetGrid(data=filtered_data, col="ChestPainType", row="Sex", hue="HeartDisease")
g.map(sns.scatterplot,"MaxHR", "Oldpeak")
st.pyplot(g)

g = sns.jointplot(
    data=filtered_data,
    x="MaxHR", y="Oldpeak", hue="HeartDisease",
    kind="kde"
)
st.pyplot(g)

g = sns.violinplot(data=filtered_data, x="HeartDisease", y="MaxHR", palette="pastel")
st.pyplot(g.figure)

st.header("Correlation")
corr=data.select_dtypes(include='number').corr()
g = sns.heatmap(corr,cmap="viridis")
st.pyplot(g.figure)

st.header("Data Summary")
st.write(data.describe())

st.sidebar.markdown("**Note:** Use the sliders and radio buttons to explore the dataset.")