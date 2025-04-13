import pandas as pd
import os
import numpy as np

# Create data directory
os.makedirs('data', exist_ok=True)

# Berlin districts
districts = [
    'Mitte', 'Friedrichshain-Kreuzberg', 'Pankow', 'Charlottenburg-Wilmersdorf',
    'Spandau', 'Steglitz-Zehlendorf', 'Tempelhof-Schöneberg', 'Neukölln',
    'Treptow-Kölln', 'Marzahn-Hellersdorf', 'Lichtenberg', 'Reinickendorf'
]

# Approximate population (2023 estimates)
population = {
    'Mitte': 385000,
    'Friedrichshain-Kreuzberg': 290000,
    'Pankow': 410000,
    'Charlottenburg-Wilmersdorf': 340000,
    'Spandau': 245000,
    'Steglitz-Zehlendorf': 310000,
    'Tempelhof-Schöneberg': 350000,
    'Neukölln': 330000,
    'Treptow-Kölln': 270000,
    'Marzahn-Hellersdorf': 280000,
    'Lichtenberg': 300000,
    'Reinickendorf': 265000
}

# Coordinates
coords = {
    'Mitte': [52.5200, 13.4050],
    'Friedrichshain-Kreuzberg': [52.5000, 13.4400],
    'Pankow': [52.5700, 13.4000],
    'Charlottenburg-Wilmersdorf': [52.5000, 13.3000],
    'Spandau': [52.5500, 13.2000],
    'Steglitz-Zehlendorf': [52.4300, 13.2500],
    'Tempelhof-Schöneberg': [52.4700, 13.3800],
    'Neukölln': [52.4800, 13.4300],
    'Treptow-Kölln': [52.4900, 13.5100],
    'Marzahn-Hellersdorf': [52.5400, 13.5900],
    'Lichtenberg': [52.5200, 13.5000],
    'Reinickendorf': [52.5800, 13.3300]
}

# Generate realistic waste data (tons, based on 606 kg/capita/year)
data = {
    'district': districts,
    'population': [population[d] for d in districts],
    'recyclables_tons': [],  # ~40% of total (paper, plastic, glass)
    'organic_waste_tons': [],  # ~25% of total
    'residual_waste_tons': [],  # ~35% of total
    'lat': [coords[d][0] for d in districts],
    'lon': [coords[d][1] for d in districts],
    'income_level': []  # Placeholder (0–1)
}

# Waste per capita (606 kg = 0.606 tons)
total_waste_per_capita = 0.606
for pop in data['population']:
    total_waste = pop * total_waste_per_capita
    # Random variation to mimic real data
    recyclables = total_waste * (0.40 + np.random.uniform(-0.05, 0.05))
    organic = total_waste * (0.25 + np.random.uniform(-0.05, 0.05))
    residual = total_waste - recyclables - organic
    data['recyclables_tons'].append(round(recyclables, 2))
    data['organic_waste_tons'].append(round(organic, 2))
    data['residual_waste_tons'].append(round(residual, 2))
    # Income level (realistic estimates)
    data['income_level'].append(np.random.uniform(0.3, 0.9))

# Create DataFrame
df = pd.DataFrame(data)

# Save
df.to_csv('/home/kapil/Downloads/Optimizing Waste Sorting Compliance Web App/data/berlin_waste_data.csv', index=False)
print("Sample dataset saved as data/berlin_waste_data.csv")