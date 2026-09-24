import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load clustered dataset
df = pd.read_csv("outputs/customer_segments.csv")


# Calculate average values for each cluster
profile = df.groupby("Cluster")[
    ["Annual Income (k$)", "Spending Score (1-100)"]
].mean().reset_index()


# Display profile
print("Customer Segment Profiles:")
print(profile.to_string(index=False))


# Create profile visualization
profile_melted = profile.melt(
    id_vars="Cluster",
    var_name="Feature",
    value_name="Average Value"
)


plt.figure(figsize=(10, 6))

sns.barplot(
    data=profile_melted,
    x="Cluster",
    y="Average Value",
    hue="Feature"
)

plt.title("Customer Segment Profile")
plt.xlabel("Customer Cluster")
plt.ylabel("Average Value")
plt.tight_layout()

plt.savefig(
    "outputs/cluster_profile.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# Print business interpretation
print("\nBusiness Interpretation:")
print("Cluster 0: Average-income and average-spending customers.")
print("Cluster 1: High-income and high-spending customers.")
print("Cluster 2: Low-income but high-spending customers.")
print("Cluster 3: High-income but low-spending customers.")
print("Cluster 4: Low-income and low-spending customers.")

print("\nCluster profiling completed successfully!")