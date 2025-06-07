import streamlit as st

st.title("Clinical Dietary Advisor for Potassium Levels")
st.markdown("""
This tool provides dietary advice for patients based on their **potassium levels** and **kidney disease status**.
""")

# Step 1: Inputs
potassium = st.number_input("Enter potassium level (mmol/L):", min_value=2.0, max_value=7.0, value=4.0, step=0.1)
has_kidney_disease = st.radio("Does the patient have chronic kidney disease (CKD)?", ["Yes", "No"])

# Step 2: Advice Logic
advice = "General Advice :"
foods_to_eat = []
foods_to_avoid = []
warning = "Consult a doctor immediately if potassium level is dangerously high or low."

if has_kidney_disease == "Yes":
    if potassium < 3.5:
        warning = "Potassium is low (hypokalemia)."
        advice = "Increase potassium-rich foods to correct deficiency."
        foods_to_eat = ["Bananas", "Potatoes", "Spinach"]
        foods_to_avoid = []
    elif 3.5 <= potassium <= 5.0:
        advice = "Potassium is in the normal range. No dietary changes needed unless on specific medications."
        foods_to_eat = ["Regular balanced diet"]
        foods_to_avoid = []
    elif potassium > 5.0:
        warning = "Potassium is high (hyperkalemia) — potentially dangerous!"
        advice = "Restrict potassium-rich foods to prevent complications."
        foods_to_avoid = ["Bananas", "Tomatoes", "Oranges", "Potatoes", "Dried Fruits"]
        foods_to_eat = ["Apples", "Berries", "White Rice"]
else:
    advice = "No CKD — potassium level monitoring is less critical unless other conditions apply."
    if potassium < 3.5:
        warning = "Low potassium. Consider foods rich in potassium."
        foods_to_eat = ["Bananas", "Potatoes", "Spinach"]
    elif potassium > 5.0:
        warning = "High potassium. Consult a doctor if symptoms occur."
        foods_to_avoid = ["Bananas", "Oranges", "Dried Fruits"]

# Step 3: Display Output
st.markdown("---")

if warning:
    st.error(warning)

st.subheader("Dietary Advice:")
st.write(advice)

if foods_to_eat:
    st.success("Recommended Foods:")
    st.write(", ".join(foods_to_eat))

if foods_to_avoid:
    st.warning("Foods to Avoid:")
    st.write(", ".join(foods_to_avoid))
