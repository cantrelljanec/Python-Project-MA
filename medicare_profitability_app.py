import streamlit as st
from medicare_profitability import medicare_advantage_profitability_model

st.title("Medicare Advantage Profitability Calculator")

# Input fields for user parameters
base_rate = st.number_input("Base Rate (USD)", value=1000.0)
risk_adjustment_factor = st.number_input("Risk Adjustment Factor", value=1.2)
star_rating_bonus = st.number_input("Star Rating Bonus (%)", value=5)
annual_cost_per_member = st.number_input("Annual Cost per Member (USD)", value=9000.0)
cost_reduction = st.number_input("Cost Reduction (%)", value=10)

# Run calculation and display results
if st.button("Calculate"):
    result = medicare_advantage_profitability_model(
        base_rate, risk_adjustment_factor, star_rating_bonus, annual_cost_per_member, cost_reduction
    )
    for key, value in result.items():
        st.write(f"{key}: {value}")
