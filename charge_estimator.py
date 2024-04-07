import streamlit as st

def estimate_charge_time(current_charge, battery_capacity, charger_current):
    """
    Estimates the time required to charge a phone to 80% based on the current charge level,
    battery capacity, and charger current.

    Parameters:
    current_charge (float): The current charge level of the phone in percentage.
    battery_capacity (float): The total capacity of the phone's battery in mAh (milliampere-hours).
    charger_current (float): The current of the charger in mA (milliamperes).

    Returns:
    float: The estimated time in hours to charge the phone to 80%.
    """
    # Calculate the time to charge to 80%
    # Assuming a 5V USB charger, we convert the charger current to mA
    time_to_charge = (current_charge - 80) / (charger_current / battery_capacity)

    # Ensure the time is not negative
    if time_to_charge < 0:
        time_to_charge = 0

    return time_to_charge

st.title("Mobile Phone Charge Estimator")

# Collect user inputs
current_charge = st.number_input("Enter the current charge level (%):", min_value=0, max_value=100, value=0)
battery_capacity = st.number_input("Enter the battery capacity (mAh):", min_value=0, value=0)
charger_current = st.number_input("Enter the charger current (mA):", min_value=0, value=0)

# Calculate and display the estimate
if current_charge and battery_capacity and charger_current:
    estimated_time = estimate_charge_time(current_charge, battery_capacity, charger_current)
    st.write(f"Estimated time to charge to 80%: {estimated_time} hours")
else:
    st.write("Please enter all the required information.")
