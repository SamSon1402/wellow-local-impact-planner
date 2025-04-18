import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

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