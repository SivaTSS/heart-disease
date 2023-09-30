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
st.title("Heart Failure Dataset")

col1, col2 = st.columns(2)

st.header("Explore Data")
# feature_to_plot = st.sidebar.selectbox("Select a feature to visualize", data.columns)
age_range = st.sidebar.slider("Select Age Range", min_value=int(data['Age'].min()), max_value=int(data['Age'].max()), value=(int(data['Age'].min()), int(data['Age'].max())))
gender = st.sidebar.radio("Select Gender", ["All", "Male", "Female"])
    
st.header("Data Visualization")
filtered_data = data.copy()
filtered_data = filtered_data[(filtered_data['Age'] >= age_range[0]) & (filtered_data['Age'] <= age_range[1])]
if gender != "All":
    filtered_data = filtered_data[filtered_data['Sex'] == ("F" if gender == "Female" else "M")]

# corr=data.corr()
# g = sns.heatmap(corr,cmap="viridis")
# st.pyplot(g)

# g = sns.pairplot(filtered_data[["Age","RestingBP","Cholesterol","FastingBS","MaxHR","Oldpeak","HeartDisease"]], hue="HeartDisease")
# st.pyplot(g)

g = sns.jointplot(
    data=filtered_data,
    x="MaxHR", y="Oldpeak", hue="HeartDisease",
    kind="kde"
)
st.pyplot(g)

# g = sns.lmplot(data=filtered_data, x="MaxHR", y="Oldpeak", markers='o', scatter_kws={'s': 5, 'alpha': 0.8}, lowess=True, hue= "HeartDisease", palette="muted")
# st.pyplot(g.figure)

g = sns.violinplot(data=filtered_data, x="HeartDisease", y="MaxHR", palette="pastel")
st.pyplot(g.figure)

# g =sns.boxplot(data=filtered_data, x="HeartDisease", y="Oldpeak", palette="muted")
# st.pyplot(g.figure)

g = sns.FacetGrid(data=filtered_data, col="ChestPainType", row="Sex", hue="HeartDisease")
g.map(sns.scatterplot,"MaxHR", "Oldpeak")
st.pyplot(g)

st.header("Data Summary")
st.write(data.describe())

# Note
st.sidebar.markdown("**Note:** This is an EDA-only app. Use the sliders and radio buttons to explore the dataset.")