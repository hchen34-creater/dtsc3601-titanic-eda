Titanic Streamlit Exploratory Data Analysis

This introductory data science project presents a small interactive Streamlit
app for exploring passenger data from the Titanic.

Dataset
The dataset is stored in data/titanic.csv. It contains passenger information
including survival status, ticket class, sex, age, family relationships, fare,
cabin, and embarkation port.

EDA Performed
- Previewed the data and calculated descriptive statistics.
- Checked the number of rows and columns.
- Identified missing values, especially in Age and Cabin.
- Explored how survival relates to sex and passenger class.
- Examined the distributions of age and fare.

Visualizations
- Overall survival count chart
- Survival by sex count chart
- Survival by passenger class count chart
- Age histogram
- Fare histogram

Run the App
1. Install dependencies with: uv sync
2. Start the app with: uv run streamlit run app.py
3. Open the local URL shown in the terminal.

Main Findings
More passengers did not survive than survived. Survival differed substantially
by sex and passenger class. Age and cabin information include missing values,
and most fares are relatively low with a small number of high-fare passengers.

Screenshots
- screenshots/overview.png
- screenshots/visualizations.png
