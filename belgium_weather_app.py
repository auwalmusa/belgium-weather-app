import streamlit as st
import pandas as pd
import os

def load_data():
    print("Current Working Directory:", os.getcwd())
    try:
        locations_df = pd.read_csv('Locations_Belgium_Updated.csv', encoding='utf-8')  # Start with 'utf-8'
        weather_data_df = pd.read_csv('Weather_Data_Belgium_Updated.csv', encoding='utf-8')
        return locations_df, weather_data_df
    except (FileNotFoundError, UnicodeDecodeError) as e:
        st.error(f"Error loading data: {e}. Please ensure your CSV files exist, have correct encoding, and are placed in the same directory as this script.")
        st.stop()

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
