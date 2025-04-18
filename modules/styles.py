import streamlit as st

# Custom CSS for Wellow brand aesthetics
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

# Create sidebar branding and structure
def create_sidebar():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 25px;">
        <div style="display: inline-block; background-color: #E91E63; border-radius: 10px; padding: 15px; box-shadow: 4px 4px 0px #283593;">
            <div style="font-size: 40px; font-weight: bold; color: #F9DD3E; text-shadow: 3px 3px 0px #283593; font-family: 'Montserrat', sans-serif; line-height: 0.8;">w</div>
        </div>
        <h3 style="margin-top: 10px; font-size: 24px; text-transform: lowercase;">wellow</h3>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<h3 style="margin-top: 20px; text-transform: lowercase;">control panel</h3>', unsafe_allow_html=True)