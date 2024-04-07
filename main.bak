def estimate_charge_time(current_charge, battery_capacity, charger_power):
    """
    Estimates the time required to charge a phone to 80% based on the current charge level,
    battery capacity, and charger power.

    Parameters:
    current_charge (float): The current charge level of the phone in percentage.
    battery_capacity (float): The total capacity of the phone's battery in mAh (milliampere-hours).
    charger_power (float): The power of the charger in mW (milliwatts).

    Returns:
    float: The estimated time in hours to charge the phone to 80%.
    """
    # Convert charger power from mW to mA (assuming 5V, which is typical for USB chargers)
    charger_current = charger_power / 5000 # 5000mW = 5V

    # Calculate the time to charge to 80%
    time_to_charge = (current_charge - 80) / (charger_current / battery_capacity)

    return time_to_charge

# Collect user inputs
current_charge = float(input("Enter the current charge level (%): "))
battery_capacity = float(input("Enter the battery capacity (mAh): "))
charger_power = float(input("Enter the charger power (mW): "))

# Calculate and display the estimate
estimated_time = estimate_charge_time(current_charge, battery_capacity, charger_power)
print(f"Estimated time to charge to 80%: {estimated_time} hours")
""" """