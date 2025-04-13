# Berlin Waste Sorting Compliance Web App

## Overview
Analyzes waste sorting in Berlin’s districts using real data. Applies K-means clustering and Isolation Forest to identify non-compliant districts and suggests campaigns. Deployed on Heroku with Flask, Plotly, and Folium.

## Features
- **Dashboard**: Cluster waste ratios.
- **Map**: Non-compliant districts.
- **Recommendations**: Campaign suggestions.

## Data
Based on Berlin’s waste statistics, approximated from public data.

## Tech
- **Data Science**: Python, Pandas, Scikit-learn
- **Web**: Flask, Plotly, Folium
- **Deployment**: Heroku

## Installation
1. Clone: `git clone <repo>`
2. Env: `python -m venv venv; source venv/bin/activate`
3. Install: `pip install -r requirements.txt`
4. Run: `python app.py`

## Author
Kapil Adhikari
