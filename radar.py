import plotly.graph_objects as go

# Sample data structure based on your description
data = [
    [{"axis": "Danceability", "value": 0.56}, {"axis": "Energy", "value": 0.57}, {"axis": "Acousticness", "value": 0.38}, {"axis": "Instrumentalness", "value": 0.21}, {"axis": "Liveness", "value": 0.16}, {"axis": "Valence", "value": 0.44}],
    [{"axis": "Danceability", "value": 0.62}, {"axis": "Energy", "value": 0.58}, {"axis": "Acousticness", "value": 0.35}, {"axis": "Instrumentalness", "value": 0.24}, {"axis": "Liveness", "value": 0.17}, {"axis": "Valence", "value": 0.55}],
    [{"axis": "Danceability", "value": 0.59}, {"axis": "Energy", "value": 0.63}, {"axis": "Acousticness", "value": 0.26}, {"axis": "Instrumentalness", "value": 0.17}, {"axis": "Liveness", "value": 0.22}, {"axis": "Valence", "value": 0.4}]
]

# Create a radar chart for each dataset
fig = go.Figure()
arr = ['short term', 'medium term', 'long term']

for i, dataset in enumerate(data):
    fig.add_trace(go.Scatterpolar(
        r=[d['value'] for d in dataset],
        theta=[d['axis'] for d in dataset],
        fill='toself',
        name=f'{arr[i]}'
    ))

# Update layout to fit the 0-1 scale and improve aesthetics
fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 1]
        ),
    ),
    showlegend=True
)

fig.show()
