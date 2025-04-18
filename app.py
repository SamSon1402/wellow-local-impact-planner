import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import random
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="Wellow Local Impact Planner",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS for Wellow brand aesthetics based on the logo
def local_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;700&display=swap');
        
        :root {
            --wellow-pink: #E91E63;
            --wellow-yellow: #F9DD3E;
            --wellow-blue: #283593;
            --wellow-dark: #121212;
        }
        
        .stApp {
            background-color: var(--wellow-pink);
            color: white;
        }
        
        h1, h2, h3 {
            font-family: 'Montserrat', sans-serif;
            color: white;
            font-weight: 700;
            text-transform: lowercase;
        }
        
        p, div {
            font-family: 'Montserrat', sans-serif;
        }
        
        .sidebar .sidebar-content {
            background-color: var(--wellow-dark);
            border-right: none;
        }
        
        .stButton button {
            font-family: 'Montserrat', sans-serif;
            background-color: var(--wellow-yellow);
            color: var(--wellow-blue);
            border: none;
            box-shadow: 4px 4px 0px var(--wellow-blue);
            border-radius: 4px;
            font-weight: 700;
            transition: all 0.1s ease;
        }
        
        .stButton button:hover {
            transform: translate(2px, 2px);
            box-shadow: 2px 2px 0px var(--wellow-blue);
        }
        
        .wellow-box {
            border: none;
            background-color: white;
            color: var(--wellow-dark);
            padding: 20px;
            box-shadow: 6px 6px 0px var(--wellow-blue);
            border-radius: 8px;
            margin-bottom: 20px;
        }
        
        .metric-value {
            font-family: 'Montserrat', sans-serif;
            font-size: 2.5rem;
            color: var(--wellow-yellow);
            font-weight: 700;
            text-shadow: 2px 2px 0px var(--wellow-blue);
        }
        
        .metric-label {
            font-family: 'Montserrat', sans-serif;
            font-size: 0.9rem;
            color: white;
            text-transform: lowercase;
            font-weight: 500;
        }
        
        .category-environment {
            background-color: #4CAF50;
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
        }
        
        .category-social {
            background-color: var(--wellow-blue);
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
        }
        
        .category-skills {
            background-color: var(--wellow-pink);
            color: white;
            padding: 5px 10px;
            border-radius: 4px;
            font-family: 'Montserrat', sans-serif;
            font-weight: 500;
        }
        
        .dataframe {
            font-family: 'Montserrat', sans-serif;
            border: none;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .stPlotlyChart {
            border: none;
            box-shadow: 6px 6px 0px var(--wellow-blue);
            border-radius: 8px;
            overflow: hidden;
            background-color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Call the CSS function
local_css()

# Function to generate synthetic data for local needs
def generate_local_needs():
    categories = ["Environment", "Social Inclusion", "Skills Development"]
    needs = [
        "Green space maintenance", "Urban gardening support", "Waste reduction initiative",
        "Elderly companionship program", "Youth mentoring", "Immigrant integration support",
        "Digital literacy workshops", "Craftsmanship preservation", "Entrepreneurship training",
        "Recycling awareness", "Sustainable transport promotion", "Biodiversity protection",
        "Mental health support", "Child care assistance", "Disability access improvements",
        "Language exchange", "Creative arts training", "Job search assistance"
    ]
    
    priorities = ["High", "Medium", "Low"]
    neighborhoods = ["Centre-ville", "Bas Montreuil", "La Noue", "Villiers-Barbusse", "Signac", "Ruffins"]
    
    data = []
    for i in range(15):
        category = categories[i % 3]
        need_index = i % len(needs)
        data.append({
            "need_id": i + 1,
            "need": needs[need_index],
            "category": category,
            "priority": random.choice(priorities),
            "neighborhood": random.choice(neighborhoods),
            "identified_date": (datetime.now() - timedelta(days=random.randint(1, 90))).strftime("%Y-%m-%d"),
            "impact_score": random.randint(1, 10)
        })
    
    return pd.DataFrame(data)

# Function to generate synthetic data for local partners
def generate_local_partners():
    partner_types = ["Association", "Community Center", "Social Enterprise", "School", "Local Business"]
    focus_areas = ["Environment", "Social Inclusion", "Skills Development", "Multiple"]
    
    partner_names = [
        "Eco Montreuil", "Centre Social Esperanza", "La Ruche Sociale", 
        "Ateliers Partagés", "Association AVEC", "Club des Ainés", 
        "Jardin Participatif", "Maison de Quartier", "La Recyclerie de l'Est",
        "École des Arts Urbains", "La Fabrique Solidaire", "Centre Jeunesse Active",
        "Atelier Numérique", "Collectif Vert", "Association Sportive du Quartier"
    ]
    
    data = []
    for i in range(len(partner_names)):
        # Generate somewhat realistic coordinates for Montreuil area
        lat = 48.86 + random.uniform(-0.02, 0.02)
        lon = 2.44 + random.uniform(-0.02, 0.02)
        
        data.append({
            "partner_id": i + 1,
            "name": partner_names[i],
            "type": random.choice(partner_types),
            "focus_area": random.choice(focus_areas),
            "address": f"{random.randint(1, 100)} Rue {random.choice(['de Paris', 'des Ruffins', 'de Vincennes', 'Etienne Marcel', 'du Capitaine Dreyfus'])}",
            "website": f"https://www.{partner_names[i].lower().replace(' ', '')}.org",
            "contact_person": f"{random.choice(['Marie', 'Jean', 'Sophie', 'Thomas', 'Laure'])} {random.choice(['Martin', 'Dubois', 'Petit', 'Robert', 'Moreau'])}",
            "latitude": lat,
            "longitude": lon,
            "previous_engagements": random.randint(0, 8)
        })
    
    return pd.DataFrame(data)

# Function to generate potential engagement activities
def suggest_engagement_activities(needs_df, partners_df):
    activities = []
    
    for _, need in needs_df.iterrows():
        # Find partners with matching focus area
        matching_partners = partners_df[
            (partners_df["focus_area"] == need["category"]) | 
            (partners_df["focus_area"] == "Multiple")
        ]
        
        if not matching_partners.empty:
            # Select a random matching partner
            partner = matching_partners.sample(1).iloc[0]
            
            # Generate activity suggestion
            activity_base = ""
            if need["category"] == "Environment":
                activity_base = random.choice([
                    "neighborhood cleanup", 
                    "urban gardening workshop", 
                    "recycling awareness campaign",
                    "sustainable living workshop",
                    "local biodiversity project"
                ])
            elif need["category"] == "Social Inclusion":
                activity_base = random.choice([
                    "community gathering", 
                    "cultural exchange event", 
                    "support group",
                    "neighborhood festival",
                    "intergenerational meetup"
                ])
            else:  # Skills Development
                activity_base = random.choice([
                    "skill-sharing workshop", 
                    "training session", 
                    "mentoring program",
                    "learning circle",
                    "practical demonstration"
                ])
            
            activity_desc = f"Partner with {partner['name']} for a {activity_base} addressing '{need['need']}'"
            
            activities.append({
                "need_id": need["need_id"],
                "partner_id": partner["partner_id"],
                "need": need["need"],
                "category": need["category"],
                "partner_name": partner["name"],
                "activity_description": activity_desc,
                "estimated_impact": random.randint(1, 10),
                "estimated_effort": random.randint(1, 10),
                "feasibility_score": random.randint(1, 10),
                "neighborhood": need["neighborhood"]
            })
    
    return pd.DataFrame(activities)

# Function to create the impact dashboard data
def generate_impact_metrics():
    # This would be connected to real data in a production system
    return {
        "total_activities": random.randint(15, 30),
        "participants": random.randint(120, 350),
        "volunteer_hours": random.randint(400, 1200),
        "partners_engaged": random.randint(8, 15),
        "neighborhoods_reached": random.randint(4, 6),
        "satisfaction_rate": round(random.uniform(80, 98), 1)
    }

# Create a styled header with Wellow logo
def create_header():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <div style="display: inline-block; background-color: #E91E63; border-radius: 10px; padding: 20px; box-shadow: 6px 6px 0px #283593;">
            <div style="font-size: 60px; font-weight: bold; color: #F9DD3E; text-shadow: 4px 4px 0px #283593; font-family: 'Montserrat', sans-serif; line-height: 0.8;">w</div>
        </div>
        <h1 style="margin-top: 15px; font-size: 40px; letter-spacing: 1px; text-transform: lowercase;">wellow local impact planner</h1>
        <p style="font-family: 'Montserrat', sans-serif; margin-top: 5px; color: white; font-weight: 500; text-transform: uppercase; letter-spacing: 2px; font-size: 14px;">montreuil edition</p>
    </div>
    """, unsafe_allow_html=True)

# Create a Wellow-styled metric
def pixel_metric(label, value, color="#F9DD3E"):
    return f"""
    <div style="text-align: center; margin: 10px 0; background-color: rgba(255, 255, 255, 0.1); padding: 15px; border-radius: 8px;">
        <div class="metric-value" style="color: {color};">{value}</div>
        <div class="metric-label">{label.lower()}</div>
    </div>
    """

# Function to create a retro-styled map using Streamlit's built-in map
def create_retro_map(df):
    # Create a color column based on focus area
    def get_color(focus_area):
        if focus_area == 'Environment':
            return '#5CDB95'  # pixel-green
        elif focus_area == 'Social Inclusion':
            return '#3772FF'  # pixel-blue
        elif focus_area == 'Skills Development':
            return '#FF6F61'  # coral
        else:
            return '#F9DD3E'  # main-yellow
    
    # Make a copy to avoid modifying the original dataframe
    map_df = df[['name', 'latitude', 'longitude', 'focus_area']].copy()
    
    # Display the map
    st.map(map_df, color='focus_area')
    
    # Display a legend for the map
    st.markdown("""
    <div style="margin-top: 10px; text-align: center;">
        <span style="font-family: 'Space Mono', monospace; font-size: 14px; color: white;">
            Map markers represent partner locations (hover for details)
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a table with partner details
    for idx, row in df.iterrows():
        if row['focus_area'] == 'Environment':
            color = '#5CDB95'  # pixel-green
            text_color = 'black'
        elif row['focus_area'] == 'Social Inclusion':
            color = '#3772FF'  # pixel-blue
            text_color = 'white'
        elif row['focus_area'] == 'Skills Development':
            color = '#FF6F61'  # coral
            text_color = 'white'
        else:
            color = '#F9DD3E'  # main-yellow
            text_color = 'black'
        
        # Create a small card for each partner
        st.markdown(f"""
        <div style="
            margin-bottom: 10px;
            border: 3px solid black;
            background-color: {color};
            color: {text_color};
            padding: 10px;
            box-shadow: 4px 4px 0px #000000;
        ">
            <div style="font-family: 'VT323', monospace; font-size: 18px; font-weight: bold;">
                {row['name']}
            </div>
            <div style="font-family: 'Space Mono', monospace; font-size: 12px;">
                <strong>Type:</strong> {row['type']} | 
                <strong>Focus:</strong> {row['focus_area']} | 
                <strong>Address:</strong> {row['address']} | 
                <strong>Contact:</strong> {row['contact_person']} | 
                <strong>Previous engagements:</strong> {row['previous_engagements']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    return None

# Main function
def main():
    # Initialize session state if it doesn't exist
    if 'needs_df' not in st.session_state:
        # Generate data the first time
        st.session_state.needs_df = generate_local_needs()
        st.session_state.partners_df = generate_local_partners()
        st.session_state.activities_df = suggest_engagement_activities(
            st.session_state.needs_df, 
            st.session_state.partners_df
        )
    
    # Create sidebar
    with st.sidebar:
        st.markdown("""
        <div style="text-align: center; margin-bottom: 25px;">
            <div style="display: inline-block; background-color: #E91E63; border-radius: 10px; padding: 15px; box-shadow: 4px 4px 0px #283593;">
                <div style="font-size: 40px; font-weight: bold; color: #F9DD3E; text-shadow: 3px 3px 0px #283593; font-family: 'Montserrat', sans-serif; line-height: 0.8;">w</div>
            </div>
            <h3 style="margin-top: 10px; font-size: 24px; text-transform: lowercase;">wellow</h3>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('<h3 style="margin-top: 20px; text-transform: lowercase;">control panel</h3>', unsafe_allow_html=True)
        
        # Location selector (for future expansion)
        st.markdown('<p style="font-family: \'Montserrat\', sans-serif; font-size: 16px; color: white; font-weight: 500; text-transform: lowercase;">select location</p>', unsafe_allow_html=True)
        location = st.selectbox("", ["Montreuil", "Future Location 1", "Future Location 2"], index=0)
        
        # Navigation
        st.markdown('<p style="font-family: \'Montserrat\', sans-serif; font-size: 16px; color: white; font-weight: 500; margin-top: 25px; text-transform: lowercase;">navigation</p>', unsafe_allow_html=True)
        page = st.radio("", ["Local Needs Overview", "Partner Map", "Engagement Suggester", "Impact Dashboard"])
        
        # Filters section
        st.markdown('<p style="font-family: \'Montserrat\', sans-serif; font-size: 16px; color: white; font-weight: 500; margin-top: 25px; text-transform: lowercase;">filters</p>', unsafe_allow_html=True)
        
        # Category filter
        category_filter = st.multiselect(
            "Categories",
            ["Environment", "Social Inclusion", "Skills Development"],
            default=["Environment", "Social Inclusion", "Skills Development"]
        )
        
        # Priority filter
        priority_filter = st.multiselect(
            "Priorities",
            ["High", "Medium", "Low"],
            default=["High", "Medium", "Low"]
        )
        
        # Neighborhood filter
        neighborhoods = sorted(st.session_state.needs_df['neighborhood'].unique())
        neighborhood_filter = st.multiselect(
            "Neighborhoods",
            neighborhoods,
            default=neighborhoods
        )
    
    # Create the header
    create_header()
    
    # Filter data based on sidebar selections
    filtered_needs = st.session_state.needs_df[
        (st.session_state.needs_df['category'].isin(category_filter)) &
        (st.session_state.needs_df['priority'].isin(priority_filter)) &
        (st.session_state.needs_df['neighborhood'].isin(neighborhood_filter))
    ]
    
    # Main content based on page selection
    if page == "Local Needs Overview":
        st.markdown('<h2 style="text-align: center;">LOCAL NEEDS OVERVIEW</h2>', unsafe_allow_html=True)
        
        # Summary metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(pixel_metric("TOTAL NEEDS", len(filtered_needs)), unsafe_allow_html=True)
        with col2:
            high_priority = len(filtered_needs[filtered_needs['priority'] == 'High'])
            st.markdown(pixel_metric("HIGH PRIORITY", high_priority, color="#FF6F61"), unsafe_allow_html=True)
        with col3:
            neighborhoods_count = filtered_needs['neighborhood'].nunique()
            st.markdown(pixel_metric("NEIGHBORHOODS", neighborhoods_count, color="#5CDB95"), unsafe_allow_html=True)
        
        # Needs by category chart
        cat_counts = filtered_needs['category'].value_counts().reset_index()
        cat_counts.columns = ['Category', 'Count']
        
        fig = px.bar(
            cat_counts, 
            x='Category', 
            y='Count',
            color='Category',
            color_discrete_map={
                'Environment': '#5CDB95',
                'Social Inclusion': '#3772FF',
                'Skills Development': '#FF6F61'
            },
            template="plotly_dark"
        )
        
        fig.update_layout(
            title='NEEDS BY CATEGORY',
            title_font=dict(family='VT323', size=24),
            font=dict(family='Space Mono'),
            plot_bgcolor='#1E1E3F',
            paper_bgcolor='#1E1E3F',
            xaxis=dict(
                title=None,
                showgrid=False,
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2
            ),
            yaxis=dict(
                title=None,
                showgrid=True,
                gridcolor='rgba(249, 221, 62, 0.2)',
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2
            ),
            margin=dict(t=50, b=50, l=50, r=50),
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Detailed needs table
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">DETAILED NEEDS</h3>', unsafe_allow_html=True)
        
        # Format the DataFrame for display
        display_needs = filtered_needs[['need', 'category', 'priority', 'neighborhood', 'impact_score']].copy()
        display_needs.columns = ['Need', 'Category', 'Priority', 'Neighborhood', 'Impact Score']
        
        # Add color coding for priorities
        def color_priority(val):
            if val == 'High':
                return 'background-color: #FF6F61; color: white; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
            elif val == 'Medium':
                return 'background-color: #F9DD3E; color: black; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
            else:
                return 'background-color: #5CDB95; color: black; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
        
        # Add color coding for categories
        def color_category(val):
            if val == 'Environment':
                return 'background-color: #5CDB95; color: black; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
            elif val == 'Social Inclusion':
                return 'background-color: #3772FF; color: white; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
            else:
                return 'background-color: #FF6F61; color: white; font-family: "VT323", monospace; text-align: center; border: 2px solid black;'
        
        # Style the dataframe
        styled_needs = display_needs.style.applymap(color_priority, subset=['Priority']).applymap(color_category, subset=['Category'])
        
        st.dataframe(styled_needs, height=400, use_container_width=True)
    
    elif page == "Partner Map":
        st.markdown('<h2 style="text-align: center;">LOCAL PARTNER MAP</h2>', unsafe_allow_html=True)
        
        # Partner type and focus area filters
        col1, col2 = st.columns(2)
        
        with col1:
            partner_types = sorted(st.session_state.partners_df['type'].unique())
            selected_types = st.multiselect(
                "Filter by Partner Type",
                partner_types,
                default=partner_types
            )
        
        with col2:
            focus_areas = sorted(st.session_state.partners_df['focus_area'].unique())
            selected_focus = st.multiselect(
                "Filter by Focus Area",
                focus_areas,
                default=focus_areas
            )
        
        # Filter partners based on selections
        filtered_partners = st.session_state.partners_df[
            (st.session_state.partners_df['type'].isin(selected_types)) &
            (st.session_state.partners_df['focus_area'].isin(selected_focus))
        ]
        
        # Display map
        if not filtered_partners.empty:
            st.markdown('<div style="margin: 30px 0;"></div>', unsafe_allow_html=True)
            create_retro_map(filtered_partners)
            
            # Partner legend
            st.markdown("""
            <div style="margin-top: 20px; text-align: center;">
                <div style="display: inline-block; margin: 0 15px;">
                    <div style="width: 15px; height: 15px; background-color: #5CDB95; border: 2px solid black; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                    <span style="font-family: 'Space Mono', monospace; color: white;">Environment</span>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div style="width: 15px; height: 15px; background-color: #3772FF; border: 2px solid black; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                    <span style="font-family: 'Space Mono', monospace; color: white;">Social Inclusion</span>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div style="width: 15px; height: 15px; background-color: #FF6F61; border: 2px solid black; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                    <span style="font-family: 'Space Mono', monospace; color: white;">Skills Development</span>
                </div>
                <div style="display: inline-block; margin: 0 15px;">
                    <div style="width: 15px; height: 15px; background-color: #F9DD3E; border: 2px solid black; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                    <span style="font-family: 'Space Mono', monospace; color: white;">Multiple</span>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Partner list
        if not filtered_partners.empty:
            st.markdown('<h3 style="text-align: center; margin-top: 30px; text-transform: lowercase;">partner directory</h3>', unsafe_allow_html=True)
            
            # Display partners in card format
            cols = st.columns(2)
            
            for i, (_, partner) in enumerate(filtered_partners.iterrows()):
                col_idx = i % 2
                
                # Determine card color based on focus area
                if partner['focus_area'] == 'Environment':
                    card_color = '#4CAF50'
                elif partner['focus_area'] == 'Social Inclusion':
                    card_color = '#283593'
                elif partner['focus_area'] == 'Skills Development':
                    card_color = '#E91E63'
                else:
                    card_color = '#F9DD3E'
                
                with cols[col_idx]:
                    st.markdown(f"""
                    <div style="
                        background-color: white;
                        border-radius: 8px;
                        padding: 15px;
                        margin-bottom: 15px;
                        box-shadow: 4px 4px 0px {card_color};
                    ">
                        <h4 style="color: {card_color}; font-family: 'Montserrat', sans-serif; font-weight: 700; margin-bottom: 8px;">{partner['name']}</h4>
                        <div style="font-family: 'Montserrat', sans-serif; font-size: 13px; color: #333;">
                            <p style="margin: 4px 0;"><strong>Type:</strong> {partner['type']}</p>
                            <p style="margin: 4px 0;"><strong>Focus:</strong> {partner['focus_area']}</p>
                            <p style="margin: 4px 0;"><strong>Address:</strong> {partner['address']}</p>
                            <p style="margin: 4px 0;"><strong>Contact:</strong> {partner['contact_person']}</p>
                            <p style="margin: 4px 0;"><strong>Previous engagements:</strong> {partner['previous_engagements']}</p>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("No partners match the selected filters.")
    
    elif page == "Engagement Suggester":
        st.markdown('<h2 style="text-align: center;">ENGAGEMENT ACTIVITY SUGGESTER</h2>', unsafe_allow_html=True)
        
        # Filter activities based on sidebar selections
        filtered_activities = st.session_state.activities_df[
            (st.session_state.activities_df['category'].isin(category_filter)) &
            (st.session_state.activities_df['neighborhood'].isin(neighborhood_filter))
        ]
        
        # Sort by estimated impact
        filtered_activities = filtered_activities.sort_values('estimated_impact', ascending=False)
        
        # Top activities metrics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(pixel_metric("POSSIBLE ACTIVITIES", len(filtered_activities)), unsafe_allow_html=True)
        with col2:
            high_impact = len(filtered_activities[filtered_activities['estimated_impact'] >= 7])
            st.markdown(pixel_metric("HIGH IMPACT", high_impact, color="#FF6F61"), unsafe_allow_html=True)
        with col3:
            partners_involved = filtered_activities['partner_name'].nunique()
            st.markdown(pixel_metric("PARTNERS INVOLVED", partners_involved, color="#5CDB95"), unsafe_allow_html=True)
        
        # Activity cards
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">RECOMMENDED ACTIVITIES</h3>', unsafe_allow_html=True)
        
        # Display top 5 activities as cards
        top_activities = filtered_activities.head(5)
        
        for _, activity in top_activities.iterrows():
            # Determine card color based on category
            if activity['category'] == 'Environment':
                card_color = '#5CDB95'
                text_color = 'black'
            elif activity['category'] == 'Social Inclusion':
                card_color = '#3772FF'
                text_color = 'white'
            else:  # Skills Development
                card_color = '#FF6F61'
                text_color = 'white'
            
            # Create card HTML
            card_html = f"""
            <div style="
                border: none;
                background-color: white;
                color: #333;
                padding: 20px;
                margin-bottom: 20px;
                border-radius: 8px;
                box-shadow: 5px 5px 0px #283593;
            ">
                <h3 style="font-family: 'Montserrat', sans-serif; font-size: 20px; margin-bottom: 10px; color: #E91E63; font-weight: 700;">
                    {activity['activity_description']}
                </h3>
                <div style="display: flex; justify-content: space-between; margin-top: 15px;">
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 14px;">
                        <strong>Need:</strong> {activity['need']}<br>
                        <strong>Category:</strong> {activity['category']}<br>
                        <strong>Neighborhood:</strong> {activity['neighborhood']}
                    </div>
                    <div style="font-family: 'Montserrat', sans-serif; font-size: 14px; text-align: right;">
                        <strong>Partner:</strong> {activity['partner_name']}<br>
                        <strong>Impact:</strong> {'★' * int(activity['estimated_impact'])}<br>
                        <strong>Effort:</strong> {'⚡' * int(activity['estimated_effort'])}
                    </div>
                </div>
            </div>
            """
            
            st.markdown(card_html, unsafe_allow_html=True)
        
        # Activity matrix - Plot impact vs effort
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">ACTIVITY IMPACT MATRIX</h3>', unsafe_allow_html=True)
        
        fig = px.scatter(
            filtered_activities,
            x='estimated_effort',
            y='estimated_impact',
            color='category',
            size='feasibility_score',
            hover_name='activity_description',
            text='partner_name',
            color_discrete_map={
                'Environment': '#5CDB95',
                'Social Inclusion': '#3772FF',
                'Skills Development': '#FF6F61'
            },
            template="plotly_dark"
        )
        
        fig.update_layout(
            title='IMPACT vs EFFORT MATRIX',
            title_font=dict(family='VT323', size=24),
            font=dict(family='Space Mono'),
            plot_bgcolor='#1E1E3F',
            paper_bgcolor='#1E1E3F',
            xaxis=dict(
                title='EFFORT LEVEL',
                showgrid=True,
                gridcolor='rgba(249, 221, 62, 0.2)',
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2,
                range=[0, 11]
            ),
            yaxis=dict(
                title='IMPACT LEVEL',
                showgrid=True,
                gridcolor='rgba(249, 221, 62, 0.2)',
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2,
                range=[0, 11]
            ),
            margin=dict(t=50, b=50, l=50, r=50),
        )
        
        # Add quadrant lines
        fig.add_shape(type="line", x0=5.5, y0=0, x1=5.5, y1=11, line=dict(color="#F9DD3E", width=2, dash="dash"))
        fig.add_shape(type="line", x0=0, y0=5.5, x1=11, y1=5.5, line=dict(color="#F9DD3E", width=2, dash="dash"))
        
        # Add quadrant labels
        fig.add_annotation(x=3, y=8, text="HIGH IMPACT,<br>LOW EFFORT<br>(QUICK WINS)", showarrow=False, font=dict(family="VT323", size=14, color="#F9DD3E"))
        fig.add_annotation(x=8, y=8, text="HIGH IMPACT,<br>HIGH EFFORT<br>(MAJOR PROJECTS)", showarrow=False, font=dict(family="VT323", size=14, color="#F9DD3E"))
        fig.add_annotation(x=3, y=3, text="LOW IMPACT,<br>LOW EFFORT<br>(FILL-INS)", showarrow=False, font=dict(family="VT323", size=14, color="#F9DD3E"))
        fig.add_annotation(x=8, y=3, text="LOW IMPACT,<br>HIGH EFFORT<br>(AVOID)", showarrow=False, font=dict(family="VT323", size=14, color="#F9DD3E"))
        
        st.plotly_chart(fig, use_container_width=True)
        
    elif page == "Impact Dashboard":
        st.markdown('<h2 style="text-align: center;">IMPACT DASHBOARD</h2>', unsafe_allow_html=True)
        st.markdown('<p style="text-align: center; font-family: \'Space Mono\', monospace; color: #F9DD3E;">(CONCEPTUAL VISUALIZATION)</p>', unsafe_allow_html=True)
        
        # Generate mock impact metrics
        impact_metrics = generate_impact_metrics()
        
        # Display key metrics in a grid
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(pixel_metric("TOTAL ACTIVITIES", impact_metrics["total_activities"]), unsafe_allow_html=True)
        with col2:
            st.markdown(pixel_metric("PARTICIPANTS", impact_metrics["participants"], color="#FF6F61"), unsafe_allow_html=True)
        with col3:
            st.markdown(pixel_metric("VOLUNTEER HOURS", impact_metrics["volunteer_hours"], color="#5CDB95"), unsafe_allow_html=True)
            
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(pixel_metric("PARTNERS ENGAGED", impact_metrics["partners_engaged"]), unsafe_allow_html=True)
        with col2:
            st.markdown(pixel_metric("NEIGHBORHOODS", impact_metrics["neighborhoods_reached"], color="#FF6F61"), unsafe_allow_html=True)
        with col3:
            st.markdown(pixel_metric("SATISFACTION RATE", f"{impact_metrics['satisfaction_rate']}%", color="#5CDB95"), unsafe_allow_html=True)
        
        # Mock participation trend chart
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">PARTICIPATION TREND</h3>', unsafe_allow_html=True)
        
        # Generate mock monthly data for the past 6 months
        months = ["November", "December", "January", "February", "March", "April"]
        participants = [random.randint(15, 40) for _ in range(6)]
        cumulative = [sum(participants[:i+1]) for i in range(6)]
        
        # Create the trend chart
        fig = go.Figure()
        
        # Add monthly participants bars
        fig.add_trace(go.Bar(
            x=months,
            y=participants,
            name='Monthly Participants',
            marker_color='#F9DD3E'
        ))
        
        # Add cumulative line
        fig.add_trace(go.Scatter(
            x=months,
            y=cumulative,
            name='Cumulative Participants',
            mode='lines+markers',
            line=dict(color='#E91E63', width=4),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title='community participation',
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
                title='participants',
                showgrid=True,
                gridcolor='rgba(255, 255, 255, 0.2)',
                showline=True,
                linecolor='white',
                linewidth=2,
                color='white'
            ),
            margin=dict(t=50, b=50, l=50, r=50),
            legend=dict(
                font=dict(family='Montserrat', size=12, color='white'),
                bgcolor='rgba(0,0,0,0.3)',
                bordercolor='white'
            )
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Activity categories distribution
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">ACTIVITY CATEGORY DISTRIBUTION</h3>', unsafe_allow_html=True)
        
        # Create mock data for the categories
        categories = ['Environment', 'Social Inclusion', 'Skills Development']
        category_counts = [random.randint(3, 10) for _ in range(3)]
        
        # Create a pie chart
        fig = px.pie(
            values=category_counts,
            names=categories,
            color=categories,
            color_discrete_map={
                'Environment': '#4CAF50',
                'Social Inclusion': '#283593',
                'Skills Development': '#E91E63'
            },
            hole=0.4
        )
        
        fig.update_layout(
            title='activities by category',
            title_font=dict(family='Montserrat', size=24, color='white'),
            font=dict(family='Montserrat', color='white'),
            plot_bgcolor='rgba(255, 255, 255, 0.1)',
            paper_bgcolor='rgba(255, 255, 255, 0.1)',
            margin=dict(t=50, b=50, l=50, r=50),
            legend=dict(
                font=dict(family='Montserrat', size=12, color='white'),
                bgcolor='rgba(0,0,0,0.3)',
                bordercolor='white'
            )
        )
        
        fig.update_traces(
            textfont=dict(family='VT323', size=18),
            textinfo='percent+label',
            marker=dict(line=dict(color='#000000', width=2))
        )
        
        st.plotly_chart(fig, use_container_width=True)
        
        # Impact across neighborhoods
        st.markdown('<h3 style="text-align: center; margin-top: 30px;">NEIGHBORHOOD IMPACT</h3>', unsafe_allow_html=True)
        
        # Create mock data for neighborhoods
        neighborhoods = ["Centre-ville", "Bas Montreuil", "La Noue", "Villiers-Barbusse", "Signac", "Ruffins"]
        activities_count = [random.randint(1, 8) for _ in range(6)]
        engagement_score = [random.randint(1, 10) for _ in range(6)]
        
        # Create a horizontal bar chart
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
                symbol='square',
                color='#FF6F61',
                line=dict(color='#000000', width=2)
            )
        ))
        
        fig.update_layout(
            title='NEIGHBORHOOD ENGAGEMENT',
            title_font=dict(family='VT323', size=24),
            font=dict(family='Space Mono'),
            plot_bgcolor='#1E1E3F',
            paper_bgcolor='#1E1E3F',
            xaxis=dict(
                title='COUNT / SCORE',
                showgrid=True,
                gridcolor='rgba(249, 221, 62, 0.2)',
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2
            ),
            yaxis=dict(
                title=None,
                showgrid=False,
                showline=True,
                linecolor='#F9DD3E',
                linewidth=2
            ),
            margin=dict(t=50, b=50, l=120, r=50),
            legend=dict(
                font=dict(family='VT323', size=16),
                bgcolor='rgba(0,0,0,0.5)',
                bordercolor='#F9DD3E'
            ),
            barmode='group'
        )
        
        st.plotly_chart(fig, use_container_width=True)

# Run the app
if __name__ == "__main__":
    main()