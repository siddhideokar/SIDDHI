
import streamlit as st
import pandas as pd
from datetime import datetime

# Initialize session state for storing the ledger
if 'ledger' not in st.session_state:
    st.session_state['ledger'] = pd.DataFrame(columns=["Member Name", "Membership Type", "Start Date", "End Date", "Payment Status"])

# Function to add new member to the ledger
def add_member(name, membership_type, start_date, end_date, payment_status):
    new_member = pd.DataFrame([[name, membership_type, start_date, end_date, payment_status]],
                              columns=st.session_state['ledger'].columns)
    st.session_state['ledger'] = pd.concat([st.session_state['ledger'], new_member], ignore_index=True)

# Streamlit UI
st.title("Gym Membership Ledger")

# Sidebar to add new member
with st.sidebar:
    st.header("Add New Member")
    member_name = st.text_input("Enter Member Name")
    membership_type = st.selectbox("Select Membership Type", ["Monthly", "Quarterly", "Yearly"])
    start_date = st.date_input("Start Date", min_value=datetime.today())
    end_date = st.date_input("End Date", min_value=start_date)
    payment_status = st.selectbox("Payment Status", ["Paid", "Unpaid"])

    if st.button("Add Member"):
        if member_name and start_date and end_date:
            add_member(member_name, membership_type, start_date, end_date, payment_status)
            st.success(f"{member_name} has been added to the ledger.")
        else:
            st.error("Please fill in all the fields.")

# Display current ledger
st.header("Current Membership Ledger")
st.dataframe(st.session_state['ledger'])

# Option to download the ledger as CSV
st.download_button(
    label="Download Ledger as CSV",
    data=st.session_state['ledger'].to_csv(index=False),
    file_name="gym_membership_ledger.csv",
    mime="text/csv"
)

