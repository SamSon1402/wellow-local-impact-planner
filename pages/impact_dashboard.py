import streamlit as st
import random
from modules.styles import pixel_metric
from modules.data_generator import generate_impact_metrics
from modules.visualizations import create_participation_trend, create_category_distribution

def show_impact_dashboard():
    st.markdown('<h2 style="text-align: center; text-transform: lowercase;">impact dashboard</h2>', unsafe_allow_html=True)
    st.markdown('<p style="text-align: center; font-family: \'Montserrat\', sans-serif; color: white;">(conceptual visualization)</p>', unsafe_allow_html=True)
    
    # Generate mock impact metrics
    impact_metrics = generate_impact_metrics()
    
    # Display key metrics in a grid
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(pixel_metric("total activities", impact_metrics["total_activities"]), unsafe_allow_html=True)
    with col2:
        st.markdown(pixel_metric("participants", impact_metrics["participants"], color="#E91E63"), unsafe_allow_html=True)
    with col3:
        st.markdown(pixel_metric("volunteer hours", impact_metrics["volunteer_hours"], color="#4CAF50"), unsafe_allow_html=True)
        
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(pixel_metric("partners engaged", impact_metrics["partners_engaged"]), unsafe_allow_html=True)
    with col2:
        st.markdown(pixel_metric("neighborhoods", impact_metrics["neighborhoods_reached"], color="#E91E63"), unsafe_allow_html=True)
    with col3:
        st.markdown(pixel_metric("satisfaction rate", f"{impact_metrics['satisfaction_rate']}%", color="#4CAF50"), unsafe_allow_html=True)
    
    # Mock participation trend chart
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">participation trend</h3>', unsafe_allow_html=True)
    
    fig = create_participation_trend()
    st.plotly_chart(fig, use_container_width=True)
    
    # Activity categories distribution
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">activity category distribution</h3>', unsafe_allow_html=True)
    
    fig = create_category_distribution()
    st.plotly_chart(fig, use_container_width=True)
    
    # Impact across neighborhoods
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">neighborhood impact</h3>', unsafe_allow_html=True)
    
    # Create mock data for neighborhoods
    neighborhoods = ["Centre-ville", "Bas Montreuil", "La Noue", "Villiers-Barbusse", "Signac", "Ruffins"]
    activities_count = [random.randint(1, 8) for _ in range(6)]
    engagement_score = [random.randint(1, 10) for _ in range(6)]
    
    # Create a horizontal bar chart
    import plotly.graph_objects as go
    
    fig = go.Figure()
    
    # Add bars for activities count
    fig.add_trace(go.Bar(
        y=neighborhoods,
        x=activities_count,
        name='Activities',
        orientation='h',
        marker_color='#F9DD3E'
    ))
    
    # Add markers for engagement score
    fig.add_trace(go.Scatter(
        y=neighborhoods,
        x=engagement_score,
        name='Engagement Score',
        mode='markers',
        marker=dict(
            size=15,
            color='#E91E63',
            line=dict(color='white', width=2)
        )
    ))
    
    fig.update_layout(
        title='neighborhood engagement',
        title_font=dict(family='Montserrat', size=24, color='white'),
        font=dict(family='Montserrat', color='white'),
        plot_bgcolor='rgba(255, 255, 255, 0.1)',
        paper_bgcolor='rgba(255, 255, 255, 0.1)',
        xaxis=dict(
            title='count / score',
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.2)',
            showline=True,
            linecolor='white',
            linewidth=2,
            color='white'
        ),
        yaxis=dict(
            title=None,
            showgrid=False,
            showline=True,
            linecolor='white',
            linewidth=2,
            color='white'
        ),
        margin=dict(t=50, b=50, l=120, r=50),
        legend=dict(
            font=dict(family='Montserrat', size=12, color='white'),
            bgcolor='rgba(0,0,0,0.3)',
            bordercolor='white'
        ),
        barmode='group'
    )
    
    st.plotly_chart(fig, use_container_width=True)