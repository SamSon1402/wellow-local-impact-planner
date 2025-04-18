import streamlit as st
import pandas as pd
import plotly.express as px
from modules.styles import pixel_metric

def show_needs_overview(filtered_needs):
    st.markdown('<h2 style="text-align: center; text-transform: lowercase;">local needs overview</h2>', unsafe_allow_html=True)
    
    # Summary metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(pixel_metric("total needs", len(filtered_needs)), unsafe_allow_html=True)
    with col2:
        high_priority = len(filtered_needs[filtered_needs['priority'] == 'High'])
        st.markdown(pixel_metric("high priority", high_priority, color="#E91E63"), unsafe_allow_html=True)
    with col3:
        neighborhoods_count = filtered_needs['neighborhood'].nunique()
        st.markdown(pixel_metric("neighborhoods", neighborhoods_count, color="#4CAF50"), unsafe_allow_html=True)
    
    # Needs by category chart
    cat_counts = filtered_needs['category'].value_counts().reset_index()
    cat_counts.columns = ['Category', 'Count']
    
    fig = px.bar(
        cat_counts, 
        x='Category', 
        y='Count',
        color='Category',
        color_discrete_map={
            'Environment': '#4CAF50',
            'Social Inclusion': '#283593',
            'Skills Development': '#E91E63'
        },
        template="plotly_dark"
    )
    
    fig.update_layout(
        title='needs by category',
        title_font=dict(family='Montserrat', size=24, color='white'),
        font=dict(family='Montserrat', color='white'),
        plot_bgcolor='rgba(255, 255, 255, 0.1)',
        paper_bgcolor='rgba(255, 255, 255, 0.1)',
        xaxis=dict(
            title=None,
            showgrid=False,
            showline=True,
            linecolor='white',
            linewidth=2,
            color='white'
        ),
        yaxis=dict(
            title=None,
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.2)',
            showline=True,
            linecolor='white',
            linewidth=2,
            color='white'
        ),
        margin=dict(t=50, b=50, l=50, r=50),
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Detailed needs table
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">detailed needs</h3>', unsafe_allow_html=True)
    
    # Format the DataFrame for display
    display_needs = filtered_needs[['need', 'category', 'priority', 'neighborhood', 'impact_score']].copy()
    display_needs.columns = ['Need', 'Category', 'Priority', 'Neighborhood', 'Impact Score']
    
    # Add color coding for priorities
    def color_priority(val):
        if val == 'High':
            return 'background-color: #E91E63; color: white; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
        elif val == 'Medium':
            return 'background-color: #F9DD3E; color: black; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
        else:
            return 'background-color: #4CAF50; color: white; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
    
    # Add color coding for categories
    def color_category(val):
        if val == 'Environment':
            return 'background-color: #4CAF50; color: white; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
        elif val == 'Social Inclusion':
            return 'background-color: #283593; color: white; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
        else:
            return 'background-color: #E91E63; color: white; font-family: "Montserrat", sans-serif; text-align: center; border-radius: 4px; font-weight: 500;'
    
    # Style the dataframe
    styled_needs = display_needs.style.applymap(color_priority, subset=['Priority']).applymap(color_category, subset=['Category'])
    
    st.dataframe(styled_needs, height=400, use_container_width=True)