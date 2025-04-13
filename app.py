from flask import Flask, render_template, request
import pandas as pd
import plotly.express as px
import plotly
import json
import folium
import joblib

app = Flask(__name__)

# Load data and models
df = pd.read_csv('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/data/processed/processed_berlin_waste_data.csv')
scaler = joblib.load('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/scaler.pkl')
kmeans = joblib.load('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/kmeans_model.pkl')
iso_forest = joblib.load('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/models/isoforest_model.pkl')

@app.route('/')
def dashboard():
    cluster_summary = df.groupby('cluster')['residual_waste_ratio'].mean().reset_index()
    fig = px.bar(cluster_summary, x='cluster', y='residual_waste_ratio', 
                 title='Average Residual Waste Ratio by Cluster in Berlin',
                 labels={'residual_waste_ratio': 'Residual Waste Ratio', 'cluster': 'Cluster'})
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template('dashboard.html', graph_json=graph_json)

@app.route('/map')
def map_view():
    m = folium.Map(location=[52.5200, 13.4050], zoom_start=10)
    for _, row in df[df['anomaly'] == 1].iterrows():
        folium.Marker(
            location=[row['lat'], row['lon']],
            popup=f"{row['district']}: Residual Ratio {row['residual_waste_ratio']:.2f}",
            icon=folium.Icon(color='red')
        ).add_to(m)
    return m._repr_html_()

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    recommendation = None
    district = None
    if request.method == 'POST':
        district = request.form.get('district')
        area_data = df[df['district'].str.lower() == district.lower()]
        if not area_data.empty:
            if area_data['income_level'].iloc[0] < 0.5:
                recommendation = f"For {district}: Provide affordable sorting bins and community workshops."
            else:
                recommendation = f"For {district}: Distribute visual sorting guides and online tutorials."
        else:
            recommendation = "District not found."
    return render_template('recommend.html', recommendation=recommendation, district=district)

if __name__ == '__main__':
    app.run(debug=True)