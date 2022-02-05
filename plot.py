import plotly.graph_objects as go
import numpy as np

cellcount = 16


for l in range(cellcount):
    fig = go.Figure(data=[
        go.Mesh3d(
            # 8 vertices of a cube
            x=[l-1, l-1, l, l, l-1, l-1, l, l],
            y=[l-1, l, l, l-1, l-1, l, l, l-1],
            z=[l-1, l-1, l-1, l-1, l, l, l, l],
            colorbar_title='z',
            colorscale=[[0, 'gold'],
                        [0.5, 'mediumturquoise'],
                        [1, 'magenta']],
            intensity = np.linspace(0, 1, 12, endpoint=True),
            intensitymode='cell',
            i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
            j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
            k = [0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
            name='y',
            showscale=True
        )
    ])

fig.show()