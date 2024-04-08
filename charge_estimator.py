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
    # Check if the current charge level is already over 79%
    if current_charge >= 79:
        return 0 # No need to calculate, already charged to or above 80%

    # Calculate the time to charge to 80%
    time_to_charge = (80 - current_charge) / (charger_current / (battery_capacity / 100))

    # Ensure the time is not negative
    if time_to_charge < 0:
        time_to_charge = 0

    return time_to_charge

def format_charge_time(time_to_charge):
    """
    Formats the estimated charge time for display.

    Parameters:
    time_to_charge (float): The estimated time in hours to charge the phone to 80%.

    Returns:
    str: The formatted time string.
    """
    if time_to_charge >= 1:
        # If the time is more than an hour, round to the nearest hour
        return f"{round(time_to_charge)} hours"
    else:
        # If the time is less than an hour, convert to minutes and round to the nearest minute
        return f"{round(time_to_charge * 60)} minutes"

st.title("Mobile Phone Charge Estimator")

# Collect user inputs
current_charge = st.number_input("Enter the current charge level (%):", min_value=0, max_value=100, value=0)
battery_capacity = st.number_input("Enter the battery capacity (mAh):", min_value=0, value=0)
charger_current = st.number_input("Enter the charger current (mA):", min_value=0, value=0)

# Calculate and display the estimate
if current_charge and battery_capacity and charger_current:
    estimated_time = estimate_charge_time(current_charge, battery_capacity, charger_current)
    if estimated_time == 0:
        st.write("Your phone is already charged to or above 80%. No further charging is needed.")
    else:
        formatted_time = format_charge_time(estimated_time)
        st.write(f"Estimated time to charge to 80%: {formatted_time}")
else:
    st.write("Please enter all the required information.")
