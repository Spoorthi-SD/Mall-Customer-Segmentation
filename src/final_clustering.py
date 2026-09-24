import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score


# Load dataset
df = pd.read_csv("data/Mall_Customers.csv")


# Select final features
features = [
    "Annual Income (k$)",
    "Spending Score (1-100)"
]

X = df[features]


# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


# Train final K-Means model
kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)


# Calculate silhouette score
silhouette = silhouette_score(X_scaled, df["Cluster"])

print("Final Clustering Results")
print("------------------------")
print("Number of Clusters:", 5)
print("Features Used:", features)
print("Silhouette Score:", round(silhouette, 4))


# Display cluster sizes
print("\nCluster Sizes:")
print(df["Cluster"].value_counts().sort_index())


# Calculate cluster profiles
cluster_profile = df.groupby("Cluster")[features].mean()

print("\nCluster Profiles:")
print(cluster_profile)


# Visualize clusters
plt.figure(figsize=(10, 7))

sns.scatterplot(
    data=df,
    x="Annual Income (k$)",
    y="Spending Score (1-100)",
    hue="Cluster",
    palette="Set2",
    s=100
)

# Plot cluster centers
centers = scaler.inverse_transform(kmeans.cluster_centers_)

plt.scatter(
    centers[:, 0],
    centers[:, 1],
    marker="X",
    s=250,
    color="black",
    label="Cluster Centers"
)

plt.title("Customer Segmentation using K-Means")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.tight_layout()

plt.savefig(
    "outputs/customer_segments.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Save clustered dataset
df.to_csv(
    "outputs/customer_segments.csv",
    index=False
)

print("\nFinal clustering completed successfully!")
print("Saved: outputs/customer_segments.csv")
print("Saved: outputs/customer_segments.png")