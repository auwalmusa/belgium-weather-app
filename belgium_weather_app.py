import streamlit as st
import pandas as pd
import os

# Corrected function to load data from CSV files within the 'data' subdirectory
def load_data():
    base_path = os.path.dirname(__file__)  # Get the directory where the script is located
    locations_path = os.path.join(base_path, 'data', 'Locations_Belgium_Updated.csv')
    weather_data_path = os.path.join(base_path, 'data', 'Weather_Data_Belgium_Updated.csv')
    
    locations_df = pd.read_csv(locations_path, encoding='utf-8')
    weather_data_df = pd.read_csv(weather_data_path, encoding='utf-8')
    return locations_df, weather_data_df

locations_df, weather_data_df = load_data()

st.title('Weather Monitoring in Belgium')

selected_location = st.selectbox('Select a location:', locations_df['location_name'].unique())

if selected_location:
    location_id = locations_df[locations_df['location_name'] == selected_location]['location_id'].iloc[0]

    if location_id in weather_data_df['location_id'].values:
        selected_weather_data = weather_data_df[weather_data_df['location_id'] == location_id]
        latest_weather_data = selected_weather_data.sort_values(by='timestamp', ascending=False).head(1)
        selected_location_name = locations_df[locations_df['location_id'] == location_id]['location_name'].iloc[0]

        if not latest_weather_data.empty:
            st.write(f"Weather conditions for {selected_location_name}:")
            st.write(latest_weather_data)
        else:
            st.write("No recent weather data available for the selected location.")
    else:
        st.write("Weather data not found for the selected location.")
