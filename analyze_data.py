import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
import joblib
import os

# Create directories
os.makedirs('models', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

# Load data
df = pd.read_csv('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/data/berlin_waste_data.csv')

# Preprocessing
df['total_waste'] = df['recyclables_tons'] + df['organic_waste_tons'] + df['residual_waste_tons']
df['residual_waste_ratio'] = df['residual_waste_tons'] / df['total_waste']
df['recyclables_pc'] = df['recyclables_tons'] / df['population']
df['organic_waste_pc'] = df['organic_waste_tons'] / df['population']
df['residual_waste_pc'] = df['residual_waste_tons'] / df['population']

# Handle NaNs
df = df.fillna(df.mean(numeric_only=True))

# Features for clustering
features = ['recyclables_pc', 'organic_waste_pc', 'residual_waste_pc']
X = df[features]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-means (3 clusters)
kmeans = KMeans(n_clusters=3, random_state=42)
df['cluster'] = kmeans.fit_predict(X_scaled)

# Isolation Forest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
df['anomaly'] = iso_forest.fit_predict(X_scaled)
df['anomaly'] = df['anomaly'].map({1: 0, -1: 1})

# Save
df.to_csv('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/data/processed/processed_berlin_waste_data.csv', index=False)
joblib.dump(scaler, '/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/scaler.pkl')
joblib.dump(kmeans, '/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/kmeans_model.pkl')
joblib.dump(iso_forest, '/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/isoforest_model.pkl')

print("Analysis complete. Processed data and models saved.")