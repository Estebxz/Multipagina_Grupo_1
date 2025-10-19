import streamlit as st
import plotly.graph_objects as go
import numpy as np

def plano_tridimensional():
    rg = np.linspace(-1, 1, 10)
    fixed_val = 0

    fig = go.Figure()

    X_xy, Y_xy = np.meshgrid(rg, rg)
    Z_xy = np.full(X_xy.shape, fixed_val)
    fig.add_trace(go.Surface(
        x=X_xy, y=Y_xy, z=Z_xy, name="Plano XY",
        opacity=0.7,
        colorscale=[[0, 'rgba(100, 200, 180, 0.5)'], [1, 'rgba(100, 200, 180, 0.5)']], 
        showscale=False
    ))

    # 2. Plano XZ (y=0)
    # Crea la malla para X y Z
    X_xz, Z_xz = np.meshgrid(rg, rg)
    Y_xz = np.full(X_xz.shape, fixed_val)
    fig.add_trace(go.Surface(
        x=X_xz, y=Y_xz, z=Z_xz, name="Plano XZ",
        opacity=0.7,
        colorscale=[[0, 'rgba(120, 100, 200, 0.5)'], [1, 'rgba(120, 100, 200, 0.5)']], 
        showscale=False
    ))

    # 3. Plano YZ (x=0)
    # Crea la malla para Y y Z
    Y_yz, Z_yz = np.meshgrid(rg, rg)
    X_yz = np.full(Y_yz.shape, fixed_val)
    fig.add_trace(go.Surface(
        x=X_yz, y=Y_yz, z=Z_yz, name="Plano YZ",
        opacity=0.7,
        colorscale=[[0, 'rgba(255, 140, 0, 0.5)'], [1, 'rgba(255, 140, 0, 0.5)']],
        showscale=False
    ))

    config = {
        "responsive": True,
        "displayModeBar": True,
        "displaylogo": False,
    },
    
    fig.update_layout(
        scene=dict(
            xaxis=dict(title='x', range=[-1, 1]),
            yaxis=dict(title='y', range=[-1, 1]),
            zaxis=dict(title='z', range=[-1, 1]),
            aspectmode='cube', 
            bgcolor='rgba(0,0,0,0)' 
        ),
        margin=dict(l=0, r=0, b=0, t=30),
        height=600,
        showlegend=False 
    )
    
    st.plotly_chart(fig, config=config)

if __name__ == "__main__":
    plano_tridimensional()