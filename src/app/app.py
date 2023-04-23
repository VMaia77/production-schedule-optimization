from typing import Dict
import streamlit as st
from src.api.requests import post_request


def main():
    """Get the input values from the user."""
    st.title('Production schedule optimization')
    st.sidebar.title("Input Values")

    demand = st.sidebar.number_input("Demand", value=100000, step=50)
    n_days = st.sidebar.number_input("Number of Days", value=5, step=1)

    st.sidebar.subheader("Machines Production per Hour")
    machines_prod_per_hour = {
        "machine1": st.sidebar.number_input("Machine 1", value=800, step=1),
        "machine2": st.sidebar.number_input("Machine 2", value=400, step=1),
        "machine3": st.sidebar.number_input("Machine 3", value=300, step=1),
        "machine4": st.sidebar.number_input("Machine 4", value=300, step=1),
    }

    surplus_tolerance = st.sidebar.number_input(
        "Surplus Tolerance", value=0.15, step=0.05
    )

    st.sidebar.subheader("Minimum Working Hours")
    minimum_working_hours = {
        "machine1": st.sidebar.number_input("Machine 1", value=16, step=1),
        "machine2": st.sidebar.number_input("Machine 2", value=16, step=1),
        "machine3": st.sidebar.number_input("Machine 3", value=12, step=1),
        "machine4": st.sidebar.number_input("Machine 4", value=12, step=1),
    }

    st.sidebar.subheader("Maximum Working Hours")
    maximum_working_hours = {
        "machine1": st.sidebar.number_input("Machine 1", value=24, step=1),
        "machine2": st.sidebar.number_input("Machine 2", value=20, step=1),
        "machine3": st.sidebar.number_input("Machine 3", value=20, step=1),
        "machine4": st.sidebar.number_input("Machine 4", value=20, step=1),
    }

    machine_type1_mult1 = st.sidebar.number_input(
        "Machine Type 1 Multiplier 1", value=0.001
    )

    machine_type1_add1 = st.sidebar.number_input(
        "Machine Type 1 Additive 1", value=1000
    )

    machine_type2_mult1 = st.sidebar.number_input(
        "Machine Type 2 Multiplier 1", value=0.03
    )

    machine_type2_add1 = st.sidebar.number_input(
        "Machine Type 2 Additive 1", value=1700
    )

    machine_type3_mult1 = st.sidebar.number_input(
        "Machine Type 3 Multiplier 1", value=0.002
    )

    machine_type3_mult2 = st.sidebar.number_input(
        "Machine Type 3 Multiplier 2", value=0.001
    )

    machine_type3_add1 = st.sidebar.number_input(
        "Machine Type 3 Additive 1", value=300)

    time_limit = st.sidebar.number_input("Time Limit (seconds)", value=7.0, step=0.5)

    request_id = st.sidebar.number_input("Request ID", value=173)

    problem = dict(
        demand=demand,
        n_days=n_days,
        machines_prod_per_hour=machines_prod_per_hour,
        surplus_tolerance =surplus_tolerance,
        minimum_working_hours=minimum_working_hours,
        maximum_working_hours=maximum_working_hours,
        machine_type1_mult1=machine_type1_mult1,
        machine_type1_add1=machine_type1_add1,
        machine_type2_mult1=machine_type2_mult1,
        machine_type2_add1=machine_type2_add1,
        machine_type3_mult1=machine_type3_mult1,
        machine_type3_mult2=machine_type3_mult2,
        machine_type3_add1=machine_type3_add1,
        time_limit=time_limit,
        request_id=request_id
        )

    # Call the API to solve the problem
    if st.sidebar.button("Solve"):
        message = st.text("Solving the problem...")
        solution = post_request(problem)
        message.empty()
        st.write("Solution:")
        st.write(solution)

    return


if __name__ == "__main__":
    main()