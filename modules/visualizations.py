import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import random

# Function to create a retro-styled map using Streamlit's built-in map
def create_retro_map(df):
    # Create a color column based on focus area
    def get_color(focus_area):
        if focus_area == 'Environment':
            return '#4CAF50'  # green
        elif focus_area == 'Social Inclusion':
            return '#283593'  # blue
        elif focus_area == 'Skills Development':
            return '#E91E63'  # pink
        else:
            return '#F9DD3E'  # yellow
    
    # Make a copy to avoid modifying the original dataframe
    map_df = df[['name', 'latitude', 'longitude', 'focus_area']].copy()
    
    # Display the map
    st.map(map_df, color='focus_area')
    
    # Display a legend for the map
    st.markdown("""
    <div style="margin-top: 10px; text-align: center;">
        <span style="font-family: 'Montserrat', sans-serif; font-size: 14px; color: white;">
            Map markers represent partner locations (hover for details)
        </span>
    </div>
    """, unsafe_allow_html=True)
    
    # Create a table with partner details
    for idx, row in df.iterrows():
        if row['focus_area'] == 'Environment':
            color = '#4CAF50'  # green
            text_color = 'black'
        elif row['focus_area'] == 'Social Inclusion':
            color = '#283593'  # blue
            text_color = 'white'
        elif row['focus_area'] == 'Skills Development':
            color = '#E91E63'  # pink
            text_color = 'white'
        else:
            color = '#F9DD3E'  # yellow
            text_color = 'black'
        
        # Create a small card for each partner
        st.markdown(f"""
        <div style="
            margin-bottom: 10px;
            border: none;
            background-color: white;
            color: #333;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 4px 4px 0px {color};
        ">
            <div style="font-family: 'Montserrat', sans-serif; font-size: 18px; font-weight: bold; color: {color};">
                {row['name']}
            </div>
            <div style="font-family: 'Montserrat', sans-serif; font-size: 12px;">
                <strong>Type:</strong> {row['type']} | 
                <strong>Focus:</strong> {row['focus_area']} | 
                <strong>Address:</strong> {row['address']} | 
                <strong>Contact:</strong> {row['contact_person']} | 
                <strong>Previous engagements:</strong> {row['previous_engagements']}
            </div>
        </div>
        """, unsafe_allow_html=True)

# Create an impact vs effort matrix chart
def create_impact_matrix(activities_df):
    fig = px.scatter(
        activities_df,
        x='estimated_effort',
        y='estimated_impact',
        color='category',
        size='feasibility_score',
        hover_name='activity_description',
        text='partner_name',
        color_discrete_map={
            'Environment': '#4CAF50',
            'Social Inclusion': '#283593',
            'Skills Development': '#E91E63'
        },
        template="plotly_dark"
    )
    
    fig.update_layout(
        title='impact vs effort matrix',
        title_font=dict(family='Montserrat', size=24, color='white'),
        font=dict(family='Montserrat', color='white'),
        plot_bgcolor='rgba(255, 255, 255, 0.1)',
        paper_bgcolor='rgba(255, 255, 255, 0.1)',
        xaxis=dict(
            title='effort level',
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.2)',
            showline=True,
            linecolor='white',
            linewidth=2,
            range=[0, 11],
            color='white'
        ),
        yaxis=dict(
            title='impact level',
            showgrid=True,
            gridcolor='rgba(255, 255, 255, 0.2)',
            showline=True,
            linecolor='white',
            linewidth=2,
            range=[0, 11],
            color='white'
        ),
        margin=dict(t=50, b=50, l=50, r=50),
    )
    
    # Add quadrant lines
    fig.add_shape(type="line", x0=5.5, y0=0, x1=5.5, y1=11, line=dict(color="white", width=2, dash="dash"))
    fig.add_shape(type="line", x0=0, y0=5.5, x1=11, y1=5.5, line=dict(color="white", width=2, dash="dash"))
    
    # Add quadrant labels
    fig.add_annotation(x=3, y=8, text="high impact,<br>low effort<br>(quick wins)", 
                      showarrow=False, font=dict(family="Montserrat", size=12, color="white"))
    fig.add_annotation(x=8, y=8, text="high impact,<br>high effort<br>(major projects)", 
                      showarrow=False, font=dict(family="Montserrat", size=12, color="white"))
    fig.add_annotation(x=3, y=3, text="low impact,<br>low effort<br>(fill-ins)", 
                      showarrow=False, font=dict(family="Montserrat", size=12, color="white"))
    fig.add_annotation(x=8, y=3, text="low impact,<br>high effort<br>(avoid)", 
                      showarrow=False, font=dict(family="Montserrat", size=12, color="white"))
    
    return fig

# Create a participation trend chart
def create_participation_trend():
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
    
    return fig

# Create a categories pie chart
def create_category_distribution():
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
    
    return fig