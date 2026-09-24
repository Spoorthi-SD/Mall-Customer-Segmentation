import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("data/Mall_Customers.csv")


# -----------------------------------
# 1. Numerical Feature Correlations
# -----------------------------------

numeric_columns = [
    "Age",
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

correlation = df[numeric_columns].corr()

print("Correlation Matrix:")
print(correlation)


# -----------------------------------
# 2. Pairwise Feature Relationships
# -----------------------------------

sns.pairplot(
    df[numeric_columns],
    diag_kind="kde"
)

plt.suptitle(
    "Pairwise Relationships Between Customer Features",
    y=1.02
)

plt.savefig(
    "outputs/feature_pairplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# -----------------------------------
# 3. Feature Distributions by Gender
# -----------------------------------

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(
    data=df,
    x="Gender",
    y="Age",
    ax=axes[0]
)

axes[0].set_title("Age by Gender")


sns.boxplot(
    data=df,
    x="Gender",
    y="Annual Income (k$)",
    ax=axes[1]
)

axes[1].set_title("Annual Income by Gender")


sns.boxplot(
    data=df,
    x="Gender",
    y="Spending Score (1-100)",
    ax=axes[2]
)

axes[2].set_title("Spending Score by Gender")


plt.tight_layout()

plt.savefig(
    "outputs/features_by_gender.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print("\nFeature analysis completed successfully!")