import streamlit as st
from modules.visualizations import create_retro_map

def show_partner_map(filtered_partners):
    st.markdown('<h2 style="text-align: center; text-transform: lowercase;">local partner map</h2>', unsafe_allow_html=True)
    
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
                <div style="width: 15px; height: 15px; background-color: #4CAF50; border-radius: 4px; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                <span style="font-family: 'Montserrat', sans-serif; color: white;">Environment</span>
            </div>
            <div style="display: inline-block; margin: 0 15px;">
                <div style="width: 15px; height: 15px; background-color: #283593; border-radius: 4px; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                <span style="font-family: 'Montserrat', sans-serif; color: white;">Social Inclusion</span>
            </div>
            <div style="display: inline-block; margin: 0 15px;">
                <div style="width: 15px; height: 15px; background-color: #E91E63; border-radius: 4px; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                <span style="font-family: 'Montserrat', sans-serif; color: white;">Skills Development</span>
            </div>
            <div style="display: inline-block; margin: 0 15px;">
                <div style="width: 15px; height: 15px; background-color: #F9DD3E; border-radius: 4px; display: inline-block; vertical-align: middle; margin-right: 5px;"></div>
                <span style="font-family: 'Montserrat', sans-serif; color: white;">Multiple</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Partner list
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