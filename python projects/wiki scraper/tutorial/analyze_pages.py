import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

json_path = os.path.join(os.path.dirname(__file__), 'pages.json')

# Always treat as JSON array
try:
    df = pd.read_json(json_path)
except Exception as e:
    print(f"Error reading JSON array: {e}")
    exit(1)

np_data = df.to_numpy()

print("NumPy array shape:", np_data.shape)
print("First 3 rows:\n", np_data[:3])

# Histogram: distribution of number of links per page
if 'num_links' in df.columns:
    plt.figure(figsize=(10, 6))
    df['num_links'].plot.hist(bins=50, alpha=0.7)
    plt.title('Distribution of Number of Links per Wikipedia Page')
    plt.xlabel('Number of Links')
    plt.ylabel('Number of Pages')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()
else:
    print("'num_links' column not found in data. No histogram generated.")
