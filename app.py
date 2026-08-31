"""An introductory exploratory data analysis app for the Titanic dataset."""

from pathlib import Path
import os

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
from supabase import create_client


st.set_page_config(
    page_title="Titanic EDA",
    page_icon="🚢",
    layout="wide"
)


# Supabase connection
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

if SUPABASE_URL and SUPABASE_KEY:
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
else:
    supabase = None


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


@st.cache_data
def load_supabase_data():
    """Load the Titanic dataset from Supabase."""
    if supabase is None:
        return None

    try:
        response = supabase.table("titanic").select("*").execute()

        if not response.data:
            return pd.DataFrame()

        return pd.DataFrame(response.data)

    except Exception as error:
        st.error(f"Unable to load data from Supabase: {error}")
        return None


# Load the local CSV
df = load_data()

sns.set_theme(style="whitegrid")


st.header("Dataset overview")

row_count, column_count = df.shape

col1, col2 = st.columns(2)

col1.metric("Rows", row_count)
col2.metric("Columns", column_count)


st.subheader("Dataset preview")

st.dataframe(
    df.head(10),
    width="stretch"
)


st.subheader("Descriptive statistics")

st.dataframe(
    df.describe(include="all").transpose(),
    width="stretch"
)


st.subheader("Missing values")

missing_values = df.isna().sum().reset_index()

missing_values.columns = [
    "Column",
    "Missing values"
]

st.dataframe(
    missing_values,
    width="stretch",
    hide_index=True
)


st.header("Visualizations")


left_chart, right_chart = st.columns(2)


with left_chart:

    st.subheader("Overall survival counts")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(
        data=df,
        x="Survived",
        hue="Survived",
        palette="Set2",
        legend=False,
        ax=ax
    )

    ax.set_xticks(
        [0, 1],
        ["Did not survive", "Survived"]
    )

    ax.set_xlabel("Outcome")
    ax.set_ylabel("Number of passengers")

    st.pyplot(fig)

    plt.close(fig)


with right_chart:

    st.subheader("Survival by sex")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(
        data=df,
        x="Sex",
        hue="Survived",
        palette="Set2",
        ax=ax
    )

    ax.set_xlabel("Sex")
    ax.set_ylabel("Number of passengers")

    ax.legend(
        title="Outcome",
        labels=["Did not survive", "Survived"]
    )

    st.pyplot(fig)

    plt.close(fig)


left_chart, right_chart = st.columns(2)


with left_chart:

    st.subheader("Survival by passenger class")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.countplot(
        data=df,
        x="Pclass",
        hue="Survived",
        palette="Set2",
        ax=ax
    )

    ax.set_xlabel("Passenger class")
    ax.set_ylabel("Number of passengers")

    ax.legend(
        title="Outcome",
        labels=["Did not survive", "Survived"]
    )

    st.pyplot(fig)

    plt.close(fig)


with right_chart:

    st.subheader("Age distribution")

    fig, ax = plt.subplots(figsize=(6, 4))

    sns.histplot(
        data=df,
        x="Age",
        bins=30,
        color="steelblue",
        ax=ax
    )

    ax.set_xlabel("Age (years)")
    ax.set_ylabel("Number of passengers")

    st.pyplot(fig)

    plt.close(fig)


st.subheader("Fare distribution")

fig, ax = plt.subplots(figsize=(8, 4))

sns.histplot(
    data=df,
    x="Fare",
    bins=40,
    color="coral",
    ax=ax
)

ax.set_xlabel("Fare paid")
ax.set_ylabel("Number of passengers")

st.pyplot(fig)

plt.close(fig)


# Supabase section
st.header("Supabase Database")

if supabase is None:

    st.warning(
        "Supabase credentials have not been configured yet. "
        "The application is currently using the local Titanic CSV."
    )

else:

    supabase_df = load_supabase_data()

    if supabase_df is not None and not supabase_df.empty:

        st.success(
            f"Connected to Supabase. "
            f"{len(supabase_df):,} records loaded from the titanic table."
        )

        st.subheader("Supabase data preview")

        st.dataframe(
            supabase_df.head(10),
            width="stretch"
        )

    else:

        st.warning(
            "The Supabase connection was successful, "
            "but no Titanic records were returned."
        )


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
