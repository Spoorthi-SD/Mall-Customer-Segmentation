import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# Load dataset
df = pd.read_csv("data/Mall_Customers.csv")


# Feature combinations
feature_sets = {
    "Income + Spending": [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ],
    "Age + Income + Spending": [
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
}


results = []


# Compare both feature sets
for name, features in feature_sets.items():

    X = df[features]

    # Standardize features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Test different cluster counts
    for k in range(2, 11):

        kmeans = KMeans(
            n_clusters=k,
            random_state=42,
            n_init=10
        )

        labels = kmeans.fit_predict(X_scaled)

        silhouette = silhouette_score(
            X_scaled,
            labels
        )

        results.append({
            "Feature Set": name,
            "K": k,
            "Inertia": kmeans.inertia_,
            "Silhouette Score": silhouette
        })


# Convert results to DataFrame
results_df = pd.DataFrame(results)


print("\nClustering Comparison:")
print(results_df.to_string(index=False))


# -----------------------------------
# Plot Silhouette Scores
# -----------------------------------

plt.figure(figsize=(10, 6))

for name in feature_sets:

    subset = results_df[
        results_df["Feature Set"] == name
    ]

    plt.plot(
        subset["K"],
        subset["Silhouette Score"],
        marker="o",
        label=name
    )

plt.title("Silhouette Score Comparison")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.xticks(range(2, 11))
plt.legend()
plt.grid(True)

plt.tight_layout()

plt.savefig(
    "outputs/silhouette_comparison.png",
    dpi=300
)

plt.show()


# -----------------------------------
# Best configuration
# -----------------------------------

best_result = results_df.loc[
    results_df["Silhouette Score"].idxmax()
]

print("\nBest Configuration:")
print(best_result)