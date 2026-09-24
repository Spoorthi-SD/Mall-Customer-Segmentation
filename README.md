Mall Customer Segmentation

CODTECH Internship – Machine Learning Task 1 Intern ID: CITS9278

 Project Overview

This project performs customer segmentation using K-Means clustering on mall customer data.

The goal is to identify groups of customers based on their annual income and spending score. These customer groups can help understand different purchasing patterns and support customer-focused business strategies.

🛠️ Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Plotly
Streamlit
Dataset

The dataset contains 200 mall customer records with the following information:

Field	Description
Customer ID	Unique identifier for each customer
Gender	Male / Female
Age	Customer's age
Annual Income	Annual income (in $k)
Spending Score	Score assigned based on spending behavior (1–100)
Machine Learning Approach

The project follows these steps:

Data analysis
Exploratory data analysis (EDA)
Feature analysis
Feature scaling
K-Means clustering
Cluster comparison
Silhouette score evaluation
Cluster profiling
Business insights
Interactive Streamlit dashboard
Model
Parameter	Value
Algorithm	K-Means Clustering
Number of clusters	5
Features used	Annual Income, Spending Score
Silhouette Score	0.5547
Customer Segments

The five identified customer groups are:

Average Customers
High-Value Customers
High-Spending, Lower-Income Customers
High-Income, Low-Spending Customers
Low-Income, Low-Spending Customers
Dashboard

The project includes an interactive Streamlit dashboard with:

Customer segmentation visualization
Customer group analysis
Customer explorer
Cluster profiles
Model insights
Gender and customer-group filters
How to Run
1. Install the required libraries
bash
pip install -r requirements.txt
2. Run the Streamlit dashboard
bash
streamlit run app.py
Project Structure
text
Mall-Customer-Segmentation/
├── data/
├── notebooks/
├── outputs/
├── src/
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
 Internship

This project was completed as part of the CODTECH IT Solutions Machine Learning Internship.

Intern ID: CITS9278