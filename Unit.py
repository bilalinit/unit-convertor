import streamlit as st

# Conversion functions
def convert_length(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 1 / 1000,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 1 / 1609.34,
        "yards": 1 / 0.9144,
        "feet": 1 / 0.3048,
        "inches": 1 / 0.0254,
        "nautical miles": 1 / 1852,
    }
    return value * (length_units[to_unit] / length_units[from_unit])


def convert_area(value, from_unit, to_unit):
    area_units = {
        "square meters": 1,
        "square kilometers": 1 / 1e6,
        "square centimeters": 1e4,
        "square millimeters": 1e6,
        "hectares": 1 / 10000,
        "acres": 1 / 4046.86,
        "square miles": 1 / 2.59e6,
        "square yards": 1 / 0.836127,
        "square feet": 1 / 0.092903,
        "square inches": 1 / 0.00064516,
    }
    return value * (area_units[to_unit] / area_units[from_unit])


def convert_data_rate(value, from_unit, to_unit):
    data_rate_units = {
        "bits per second": 1,
        "kilobits per second": 1 / 1000,
        "megabits per second": 1 / 1e6,
        "gigabits per second": 1 / 1e9,
    }
    return value * (data_rate_units[to_unit] / data_rate_units[from_unit])


def convert_digital_storage(value, from_unit, to_unit):
    storage_units = {
        "bytes": 1,
        "kilobytes": 1 / 1024,
        "megabytes": 1 / (1024**2),
        "gigabytes": 1 / (1024**3),
        "terabytes": 1 / (1024**4),
    }
    return value * (storage_units[to_unit] / storage_units[from_unit])


def convert_energy(value, from_unit, to_unit):
    energy_units = {
        "joules": 1,
        "kilojoules": 1 / 1000,
        "calories": 1 / 4.184,
        "kilocalories": 1 / 4184,
        "watt-hours": 1 / 3600,
        "kilowatt-hours": 1 / 3.6e6,
    }
    return value * (energy_units[to_unit] / energy_units[from_unit])


def convert_frequency(value, from_unit, to_unit):
    frequency_units = {
        "hertz": 1,
        "kilohertz": 1 / 1000,
        "megahertz": 1 / 1e6,
        "gigahertz": 1 / 1e9,
    }
    return value * (frequency_units[to_unit] / frequency_units[from_unit])


def convert_fuel_economy(value, from_unit, to_unit):
    fuel_units = {
        "liters per 100 kilometers": 1,
        "miles per gallon (US)": 235.215,
        "miles per gallon (UK)": 282.481,
    }
    return value * (fuel_units[to_unit] / fuel_units[from_unit])


def convert_mass(value, from_unit, to_unit):
    mass_units = {
        "grams": 1,
        "kilograms": 1 / 1000,
        "milligrams": 1000,
        "micrograms": 1e6,
        "pounds": 1 / 453.592,
        "ounces": 1 / 28.3495,
        "stones": 1 / 6350.29,
    }
    return value * (mass_units[to_unit] / mass_units[from_unit])


def convert_plane_angle(value, from_unit, to_unit):
    angle_units = {
        "degrees": 1,
        "radians": 1 / 57.2958,
    }
    return value * (angle_units[to_unit] / angle_units[from_unit])


def convert_pressure(value, from_unit, to_unit):
    pressure_units = {
        "pascals": 1,
        "kilopascals": 1 / 1000,
        "bars": 1 / 1e5,
        "atmospheres": 1 / 101325,
        "millimeters of mercury": 1 / 133.322,
        "pounds per square inch": 1 / 6894.76,
    }
    return value * (pressure_units[to_unit] / pressure_units[from_unit])


def convert_speed(value, from_unit, to_unit):
    speed_units = {
        "meters per second": 1,
        "kilometers per hour": 3.6,
        "miles per hour": 1 / 0.44704,
        "feet per second": 1 / 0.3048,
        "knots": 1 / 0.514444,
    }
    return value * (speed_units[to_unit] / speed_units[from_unit])


def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9 / 5) + 32
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    return value


def convert_time(value, from_unit, to_unit):
    time_units = {
        "seconds": 1,
        "minutes": 1 / 60,
        "hours": 1 / 3600,
        "days": 1 / 86400,
        "weeks": 1 / 604800,
    }
    return value * (time_units[to_unit] / time_units[from_unit])


def convert_volume(value, from_unit, to_unit):
    volume_units = {
        "cubic meters": 1,
        "cubic kilometers": 1 / 1e9,
        "cubic centimeters": 1e6,
        "cubic millimeters": 1e9,
        "liters": 1000,
        "milliliters": 1e6,
        "gallons (US)": 264.172,
        "gallons (UK)": 219.969,
        "fluid ounces (US)": 33814,
        "fluid ounces (UK)": 35195.1,
    }
    return value * (volume_units[to_unit] / volume_units[from_unit])


# Streamlit UI
st.title("Unit Converter")
st.sidebar.header("Conversion Options")

# Select category
category = st.sidebar.selectbox(
    "Select a category",
    [
        "Length",
        "Area",
        "Data Transfer Rate",
        "Digital Storage",
        "Energy",
        "Frequency",
        "Fuel Economy",
        "Mass",
        "Plane Angle",
        "Pressure",
        "Speed",
        "Temperature",
        "Time",
        "Volume",
    ],
)

# Input value
value = st.number_input("Enter the value to convert", value=0.0)

# Select units based on category
if category == "Length":
    from_unit = st.selectbox(
        "From Unit",
        [
            "meters",
            "kilometers",
            "centimeters",
            "millimeters",
            "miles",
            "yards",
            "feet",
            "inches",
            "nautical miles",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "meters",
            "kilometers",
            "centimeters",
            "millimeters",
            "miles",
            "yards",
            "feet",
            "inches",
            "nautical miles",
        ],
    )
    result = convert_length(value, from_unit, to_unit)
elif category == "Area":
    from_unit = st.selectbox(
        "From Unit",
        [
            "square meters",
            "square kilometers",
            "square centimeters",
            "square millimeters",
            "hectares",
            "acres",
            "square miles",
            "square yards",
            "square feet",
            "square inches",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "square meters",
            "square kilometers",
            "square centimeters",
            "square millimeters",
            "hectares",
            "acres",
            "square miles",
            "square yards",
            "square feet",
            "square inches",
        ],
    )
    result = convert_area(value, from_unit, to_unit)
elif category == "Data Transfer Rate":
    from_unit = st.selectbox(
        "From Unit",
        [
            "bits per second",
            "kilobits per second",
            "megabits per second",
            "gigabits per second",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "bits per second",
            "kilobits per second",
            "megabits per second",
            "gigabits per second",
        ],
    )
    result = convert_data_rate(value, from_unit, to_unit)
elif category == "Digital Storage":
    from_unit = st.selectbox(
        "From Unit", ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
    )
    to_unit = st.selectbox(
        "To Unit", ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]
    )
    result = convert_digital_storage(value, from_unit, to_unit)
elif category == "Energy":
    from_unit = st.selectbox(
        "From Unit",
        [
            "joules",
            "kilojoules",
            "calories",
            "kilocalories",
            "watt-hours",
            "kilowatt-hours",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "joules",
            "kilojoules",
            "calories",
            "kilocalories",
            "watt-hours",
            "kilowatt-hours",
        ],
    )
    result = convert_energy(value, from_unit, to_unit)
elif category == "Frequency":
    from_unit = st.selectbox(
        "From Unit", ["hertz", "kilohertz", "megahertz", "gigahertz"]
    )
    to_unit = st.selectbox(
        "To Unit", ["hertz", "kilohertz", "megahertz", "gigahertz"]
    )
    result = convert_frequency(value, from_unit, to_unit)
elif category == "Fuel Economy":
    from_unit = st.selectbox(
        "From Unit",
        ["liters per 100 kilometers", "miles per gallon (US)", "miles per gallon (UK)"],
    )
    to_unit = st.selectbox(
        "To Unit",
        ["liters per 100 kilometers", "miles per gallon (US)", "miles per gallon (UK)"],
    )
    result = convert_fuel_economy(value, from_unit, to_unit)
elif category == "Mass":
    from_unit = st.selectbox(
        "From Unit",
        ["grams", "kilograms", "milligrams", "micrograms", "pounds", "ounces", "stones"],
    )
    to_unit = st.selectbox(
        "To Unit",
        ["grams", "kilograms", "milligrams", "micrograms", "pounds", "ounces", "stones"],
    )
    result = convert_mass(value, from_unit, to_unit)
elif category == "Plane Angle":
    from_unit = st.selectbox("From Unit", ["degrees", "radians"])
    to_unit = st.selectbox("To Unit", ["degrees", "radians"])
    result = convert_plane_angle(value, from_unit, to_unit)
elif category == "Pressure":
    from_unit = st.selectbox(
        "From Unit",
        [
            "pascals",
            "kilopascals",
            "bars",
            "atmospheres",
            "millimeters of mercury",
            "pounds per square inch",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "pascals",
            "kilopascals",
            "bars",
            "atmospheres",
            "millimeters of mercury",
            "pounds per square inch",
        ],
    )
    result = convert_pressure(value, from_unit, to_unit)
elif category == "Speed":
    from_unit = st.selectbox(
        "From Unit",
        [
            "meters per second",
            "kilometers per hour",
            "miles per hour",
            "feet per second",
            "knots",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "meters per second",
            "kilometers per hour",
            "miles per hour",
            "feet per second",
            "knots",
        ],
    )
    result = convert_speed(value, from_unit, to_unit)
elif category == "Temperature":
    from_unit = st.selectbox("From Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To Unit", ["Celsius", "Fahrenheit", "Kelvin"])
    result = convert_temperature(value, from_unit, to_unit)
elif category == "Time":
    from_unit = st.selectbox(
        "From Unit", ["seconds", "minutes", "hours", "days", "weeks"]
    )
    to_unit = st.selectbox(
        "To Unit", ["seconds", "minutes", "hours", "days", "weeks"]
    )
    result = convert_time(value, from_unit, to_unit)
elif category == "Volume":
    from_unit = st.selectbox(
        "From Unit",
        [
            "cubic meters",
            "cubic kilometers",
            "cubic centimeters",
            "cubic millimeters",
            "liters",
            "milliliters",
            "gallons (US)",
            "gallons (UK)",
            "fluid ounces (US)",
            "fluid ounces (UK)",
        ],
    )
    to_unit = st.selectbox(
        "To Unit",
        [
            "cubic meters",
            "cubic kilometers",
            "cubic centimeters",
            "cubic millimeters",
            "liters",
            "milliliters",
            "gallons (US)",
            "gallons (UK)",
            "fluid ounces (US)",
            "fluid ounces (UK)",
        ],
    )
    result = convert_volume(value, from_unit, to_unit)

# Display result
st.write(f"Converted value: {result} {to_unit}")
