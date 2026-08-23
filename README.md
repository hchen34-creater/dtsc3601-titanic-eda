# Titanic Streamlit Exploratory Data Analysis

An introductory exploratory data analysis (EDA) project that uses the Titanic dataset and a Streamlit interface to make core data-inspection and visualization techniques easy to explore.

## Project Overview

This application loads Titanic passenger data, presents a quick dataset overview, and summarizes the data through tables and charts. It explores common introductory EDA questions, including who survived, how survival varied by sex and passenger class, and how passenger ages and fares were distributed.

## Dataset

The project uses [`data/titanic.csv`](data/titanic.csv), which contains passenger-level records. Main variables include:

`PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, `SibSp`, `Parch`, `Ticket`, `Fare`, `Cabin`, and `Embarked`.

## EDA Performed

- Dataset dimensions and preview
- Descriptive statistics
- Missing-value analysis
- Survival by sex
- Survival by passenger class
- Age distribution
- Fare distribution

## Key Findings

- More passengers did not survive than survived.
- Female passengers had substantially higher survival counts than male passengers.
- First-class passengers had better survival outcomes than third-class passengers.
- `Age` and `Cabin` contain missing values.
- Fare is strongly right-skewed because of a small number of expensive tickets.

## Visualizations

![Dashboard Overview](screenshots/overview.png)

![Visualizations](screenshots/visualizations.png)

## How to Run

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. From the project directory, run:

```powershell
uv sync
uv run streamlit run app.py
```

Streamlit will normally make the app available locally at [http://localhost:8501](http://localhost:8501).

## Technologies

- Python
- Streamlit
- pandas
- Matplotlib
- Seaborn
- uv

## Project Structure

```text
app.py                 # Streamlit EDA application
data/titanic.csv       # Titanic dataset
screenshots/           # Application screenshots
requirements.txt       # Python dependencies
pyproject.toml         # Project configuration
uv.lock                # Locked dependency versions
.gitignore             # Git ignore rules
```
