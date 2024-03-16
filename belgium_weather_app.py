import streamlit as st
import pandas as pd

# Function to load data from CSV files within the 'data' subdirectory
def load_data():
    # Since we're loading directly from GitHub in Streamlit Cloud, we use the relative path from the app's root directory
    locations_path = 'data/Locations_Belgium_Updated.csv'
    weather_data_path = 'data/Weather_Data_Belgium_Updated.csv'
    
    locations_df = pd.read_csv(locations_path, encoding='utf-8')
    weather_data_df = pd.read_csv(weather_data_path, encoding='utf-8')
    return locations_df, weather_data_df

locations_df, weather_data_df = load_data()

# Streamlit app title
st.title('Weather Monitoring in Belgium')

# Dropdown for location selection
selected_location = st.selectbox('Select a location:', locations_df['location_name'].unique())

if selected_location:
    # Get the selected location_id
    location_id = locations_df[locations_df['location_name'] == selected_location]['location_id'].iloc[0]
    
    # Filter weather data for the selected location
    selected_weather_data = weather_data_df[weather_data_df['location_id'] == location_id]
    
    # Get the latest weather data for the selected location
    latest_weather_data = selected_weather_data.sort_values(by='timestamp', ascending=False).head(1)
    
    if not latest_weather_data.empty:
        # Display the latest weather conditions
        st.write(f"Weather conditions for {selected_location}:")
        st.write(latest_weather_data)
    else:
        st.write("No weather data available for the selected location.")
