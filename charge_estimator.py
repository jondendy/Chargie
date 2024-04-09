import json
import os
import streamlit as st

def record_charging_details(device_name, date, time, charge_length, charge_outcome):
    """
    Records charging details to a JSON file.

    Parameters:
    device_name (str): The name of the device.
    date (str): The date of the charging session.
    time (str): The time of the charging session.
    charge_length (str): The length of the charging session.
    charge_outcome (str): The outcome of the charging session.
    """
    # Define the file path
    file_path = 'charging_details.json'

    # Check if the file exists
    if not os.path.exists(file_path):
        # If not, create an empty list
        charging_details = []
    else:
        # If it exists, load the existing data
        with open(file_path, 'r') as file:
            charging_details = json.load(file)

    # Append the new details
    new_detail = {
        'device_name': device_name,
        'date': date,
        'time': time,
        'charge_length': charge_length,
        'charge_outcome': charge_outcome
    }
    charging_details.append(new_detail)

    # Write the updated details back to the file
    with open(file_path, 'w') as file:
        json.dump(charging_details, file, indent=4)

def read_charging_details():
    """
    Reads and displays charging details from a JSON file.
    """
    # Define the file path
    file_path = 'charging_details.json'

    # Check if the file exists
    if not os.path.exists(file_path):
        st.write("No charging details recorded yet.")
    else:
        # If it exists, load the data
        with open(file_path, 'r') as file:
            charging_details = json.load(file)

        # Display the details
        for detail in charging_details:
            st.write(detail)

# Add input fields for charging details
device_name = st.text_input("Device Name:")
date = st.text_input("Date (YYYY-MM-DD):")
time = st.text_input("Time (HH:MM):")
charge_length = st.text_input("Charge Length (e.g., 1.5 hours):")
charge_outcome = st.text_input("Charge Outcome (e.g., 100%):")

# Add a button to record the details
if st.button("Record Charging Details"):
    record_charging_details(device_name, date, time, charge_length, charge_outcome)

# Add a section to display the recorded details
st.header("Recorded Charging Details")
read_charging_details()

