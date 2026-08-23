"""An introductory exploratory data analysis app for the Titanic dataset."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st


st.set_page_config(page_title="Titanic EDA", page_icon="ship", layout="wide")

st.title("Titanic Exploratory Data Analysis")
st.write(
    "This app introduces the Titanic dataset through summary tables and a few "
    "simple visualizations."
)


@st.cache_data
def load_data():
    """Load the Titanic CSV file."""
    data_path = Path(__file__).parent / "data" / "titanic.csv"
    return pd.read_csv(data_path)


df = load_data()
sns.set_theme(style="whitegrid")

st.header("Dataset overview")

row_count, column_count = df.shape
col1, col2 = st.columns(2)
col1.metric("Rows", row_count)
col2.metric("Columns", column_count)

st.subheader("Dataset preview")
st.dataframe(df.head(10), use_container_width=True)

st.subheader("Descriptive statistics")
st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

st.subheader("Missing values")
missing_values = df.isna().sum().reset_index()
missing_values.columns = ["Column", "Missing values"]
st.dataframe(missing_values, use_container_width=True, hide_index=True)

st.header("Visualizations")

left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Overall survival counts")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Survived", hue="Survived", palette="Set2", legend=False, ax=ax)
    ax.set_xticks([0, 1], ["Did not survive", "Survived"])
    ax.set_xlabel("Outcome")
    ax.set_ylabel("Number of passengers")
    st.pyplot(fig)
    plt.close(fig)

with right_chart:
    st.subheader("Survival by sex")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Sex", hue="Survived", palette="Set2", ax=ax)
    ax.set_xlabel("Sex")
    ax.set_ylabel("Number of passengers")
    ax.legend(title="Outcome", labels=["Did not survive", "Survived"])
    st.pyplot(fig)
    plt.close(fig)

left_chart, right_chart = st.columns(2)

with left_chart:
    st.subheader("Survival by passenger class")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.countplot(data=df, x="Pclass", hue="Survived", palette="Set2", ax=ax)
    ax.set_xlabel("Passenger class")
    ax.set_ylabel("Number of passengers")
    ax.legend(title="Outcome", labels=["Did not survive", "Survived"])
    st.pyplot(fig)
    plt.close(fig)

with right_chart:
    st.subheader("Age distribution")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.histplot(data=df, x="Age", bins=30, color="steelblue", ax=ax)
    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Number of passengers")
    st.pyplot(fig)
    plt.close(fig)

st.subheader("Fare distribution")
fig, ax = plt.subplots(figsize=(8, 4))
sns.histplot(data=df, x="Fare", bins=40, color="coral", ax=ax)
ax.set_xlabel("Fare paid")
ax.set_ylabel("Number of passengers")
st.pyplot(fig)
plt.close(fig)

st.header("A few observations")
st.markdown(
    """
    - More passengers did not survive than survived.
    - Survival patterns differ noticeably between female and male passengers.
    - Passenger class is also associated with different survival outcomes.
    - Age and Cabin contain missing values; Cabin is missing for most passengers.
    - Most fares are relatively low, with a small number of much higher values.
    """
)
