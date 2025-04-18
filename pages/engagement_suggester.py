import streamlit as st
from modules.styles import pixel_metric
from modules.visualizations import create_impact_matrix
from modules.utils import display_activity_card

def show_engagement_suggester(filtered_activities):
    st.markdown('<h2 style="text-align: center; text-transform: lowercase;">engagement activity suggester</h2>', unsafe_allow_html=True)
    
    # Sort by estimated impact
    filtered_activities = filtered_activities.sort_values('estimated_impact', ascending=False)
    
    # Top activities metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(pixel_metric("possible activities", len(filtered_activities)), unsafe_allow_html=True)
    with col2:
        high_impact = len(filtered_activities[filtered_activities['estimated_impact'] >= 7])
        st.markdown(pixel_metric("high impact", high_impact, color="#E91E63"), unsafe_allow_html=True)
    with col3:
        partners_involved = filtered_activities['partner_name'].nunique()
        st.markdown(pixel_metric("partners involved", partners_involved, color="#4CAF50"), unsafe_allow_html=True)
    
    # Activity cards
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">recommended activities</h3>', unsafe_allow_html=True)
    
    # Display top 5 activities as cards
    top_activities = filtered_activities.head(5)
    
    for _, activity in top_activities.iterrows():
        display_activity_card(activity)
    
    # Activity matrix - Plot impact vs effort
    st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">activity impact matrix</h3>', unsafe_allow_html=True)
    
    fig = create_impact_matrix(filtered_activities)
    st.plotly_chart(fig, use_container_width=True)