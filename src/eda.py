import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/Mall_Customers.csv")


# -----------------------------------
# 1. Gender Distribution
# -----------------------------------

plt.figure(figsize=(7, 5))

sns.countplot(data=df, x="Gender")

plt.title("Customer Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("outputs/gender_distribution.png", dpi=300)
plt.show()


# -----------------------------------
# 2. Age Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Age",
    bins=15,
    kde=True
)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("outputs/age_distribution.png", dpi=300)
plt.show()


# -----------------------------------
# 3. Annual Income Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Annual Income (k$)",
    bins=15,
    kde=True
)

plt.title("Annual Income Distribution")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("outputs/income_distribution.png", dpi=300)
plt.show()


# -----------------------------------
# 4. Spending Score Distribution
# -----------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="Spending Score (1-100)",
    bins=15,
    kde=True
)

plt.title("Spending Score Distribution")
plt.xlabel("Spending Score")
plt.ylabel("Number of Customers")

plt.tight_layout()
plt.savefig("outputs/spending_distribution.png", dpi=300)
plt.show()


# -----------------------------------
# 5. Income vs Spending Score
# -----------------------------------

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Gender",
    s=80
)

plt.title("Annual Income vs Spending Score")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")

plt.tight_layout()
plt.savefig("outputs/income_vs_spending.png", dpi=300)
plt.show()


# -----------------------------------
# 6. Age vs Spending Score
# -----------------------------------

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="Age",
    y="Spending Score (1-100)",
    hue="Gender",
    s=80
)

plt.title("Age vs Spending Score")
plt.xlabel("Age")
plt.ylabel("Spending Score")

plt.tight_layout()
plt.savefig("outputs/age_vs_spending.png", dpi=300)
plt.show()


# -----------------------------------
# 7. Correlation Heatmap
# -----------------------------------

numeric_columns = [
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

correlation = df[numeric_columns].corr()

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Numerical Features")

plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=300)
plt.show()


print("EDA completed successfully!")