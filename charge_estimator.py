import streamlit as st

def estimate_charge_time(current_charge, battery_capacity, charger_power):
    charger_current = charger_power / 5000
    time_to_charge = (current_charge - 80) / (charger_current / battery_capacity)
    return time_to_charge

st.title("Mobile Phone Charge Estimator")

# Collect user inputs
current_charge = st.number_input("Enter the current charge level (%):", min_value=0, max_value=100, value=0)
battery_capacity = st.number_input("Enter the battery capacity (mAh):", min_value=0, value=0)
charger_power = st.number_input("Enter the charger power (mW):", min_value=0, value=0)

# Calculate and display the estimate
if current_charge and battery_capacity and charger_power:
    estimated_time = estimate_charge_time(current_charge, battery_capacity, charger_power)
    st.write(f"Estimated time to charge to 80%: {estimated_time} hours")
else:
    st.write("Please enter all the required information.")
