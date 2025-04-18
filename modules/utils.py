import streamlit as st

# Function to display an activity card
def display_activity_card(activity):
    st.markdown(f"""
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
    """, unsafe_allow_html=True)

# Function to display a partner card
def display_partner_card(partner, col):
    # Determine card color based on focus area
    if partner['focus_area'] == 'Environment':
        card_color = '#4CAF50'
    elif partner['focus_area'] == 'Social Inclusion':
        card_color = '#283593'
    elif partner['focus_area'] == 'Skills Development':
        card_color = '#E91E63'
    else:
        card_color = '#F9DD3E'
    
    with col:
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

# Function to initialize session state
def initialize_session_state(data_generator):
    if 'needs_df' not in st.session_state:
        # Generate data the first time
        st.session_state.needs_df = data_generator.generate_local_needs()
        st.session_state.partners_df = data_generator.generate_local_partners()
        st.session_state.activities_df = data_generator.suggest_engagement_activities(
            st.session_state.needs_df, 
            st.session_state.partners_df
        )