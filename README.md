

# Personal Expense Tracker

A Python-based command-line application that helps users record, manage, and analyse their daily expenses using SQLite.

## Overview

The Personal Expense Tracker allows users to maintain their expense records through a simple menu-driven interface. It stores data in an SQLite database and provides useful summaries and visualisations of spending habits.

## Features

* Add new expenses with amount, category, and description.
* View all recorded expenses.
* Update existing expense records.
* Delete expenses with confirmation.
* Analyse expenses category-wise.
* View monthly expense summaries.
* Display an expense dashboard with total, average, and highest expenses.
* Visualise category-wise spending using bar charts.
* Validate user input to prevent invalid entries.

## Technologies Used

* **Python** – Application development
* **SQLite** – Database management
* **Matplotlib** – Data visualisation
* **Datetime** – Date handling

## Project Structure

```text
Personal-Expense-Tracker/
│
├── main.py
├── .gitignore
└── README.md
```

The `expenses.db` database is created automatically when the application runs. It is excluded from GitHub to protect personal expense records.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/harshita-shinge/Personal-Expense-Tracker.git
```

### 2. Navigate to the project directory

```bash
cd Personal-Expense-Tracker
```

### 3. Install the required library

```bash
pip install matplotlib
```

SQLite and Datetime are included in Python's standard library.

### 4. Run the application

```bash
python main.py
```

## Application Menu

The application provides the following options:

1. Add Expense
2. View All Expenses
3. Update Expense
4. Category-wise Expense Analysis
5. Monthly Expense Summary
6. Delete Expense
7. Expense Dashboard
8. Expense Chart
9. Exit

## Learning Outcomes

Through this project, I practised:

* Python functions and control structures.
* Exception handling and input validation.
* SQLite database operations.
* CRUD operations (Create, Read, Update, Delete).
* SQL aggregate functions such as SUM, AVG, COUNT, and MAX.
* Data visualisation using Matplotlib.
* Building a menu-driven command-line application.

## Author

**Harshita Shinge**

GitHub: [harshita-shinge](https://github.com/harshita-shinge)
