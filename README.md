# Cafe-Sales Dirty Data
📊 Cafe Sales – Data Cleaning & Analytics Project
🧩 Project Overview

This project focuses on the cleaning, transformation, and analysis of an intentionally dirty café sales dataset, designed to simulate real-world data quality issues commonly found in business environments.
The main objective was to convert inconsistent and unreliable data into trustworthy insights, store it in a relational database, and visualize it through an interactive dashboard.

🧹 Data Cleaning & Wrangling (Python)

Python, using Pandas and NumPy, was applied to address multiple data quality challenges, including:
Removal and treatment of invalid values (UNKNOWN, ERROR, NaN)
Data type conversions for incorrect fields (quantity, prices, dates)
Elimination of inconsistent records
Price correction using average prices per product
Automatic recalculation of Total Spent when missing or incorrect
Date normalization and creation of time-based features (month)
These steps transformed a disorganized dataset into a clean and analysis-ready structure.

🗄️ SQL Storage (PostgreSQL)

After cleaning, the data was loaded into PostgreSQL using SQLAlchemy, enabling:
Reliable data persistence
Scalability for larger datasets
Direct integration with Business Intelligence tools
Efficient querying for further analysis

📈 Visualization & Analysis (Power BI)

The cleaned data was connected from PostgreSQL to Power BI, where an interactive dashboard was developed featuring:
Total sales and key performance metrics (Total Spent, Quantity, Average per Unit)
Analysis by payment method and purchase type (In-store vs Takeaway)
Sales and quantity distribution by product
Time-based sales analysis
Dynamic monthly filtering
The dashboard provides clear insights into customer behavior, product performance, and sales trends through intuitive visualizations.

🛠️ Technologies Used

Python (Pandas, NumPy)
PostgreSQL
SQLAlchemy
Power BI
CSV / ETL Pipeline
Data Cleaning & Exploratory Data Analysis (EDA)

<img width="1113" height="621" alt="cafe sales" src="https://github.com/user-attachments/assets/75aa8e29-801a-4c16-bc69-9a8f498d809c" />




