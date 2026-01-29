import pandas as pd

# Load dataset
df = pd.read_csv("data/placement_targets.csv")

# Simple modification: remove duplicate rows
df_cleaned = df.drop_duplicates()

# Save modified dataset
df_cleaned.to_csv("data/placement_targets_v1.csv", index=False)

print("Preprocessing v1 completed")
