import streamlit as st
import pandas as pd
from src.preprocess import load_data, preprocess_data
from src.double_booking import detect_double_bookings
from src.early_late_checkout import early_checkout, late_checkout
from src.room_upgrade import track_upgrades
from src.no_show import analyze_no_shows
from src.occupancy_calendar import occupancy_calendar

st.set_page_config(layout="wide", page_title="Hotel Booking Conflict Resolution Analysis")
st.title("🏨 Hotel Booking Conflict Resolution Analysis")

df = load_data()
df = preprocess_data(df)

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "Double Booking Conflicts",
    "Early Checkouts",
    "Late Checkouts",
    "Room Upgrades",
    "No-Show & Deposit Summary",
    "Occupancy Calendar",
    "Data Quality Issues"
])

with tab1:
    st.header("1️⃣ Double Booking Conflicts")
    conflicts = detect_double_bookings(df)
    st.dataframe(conflicts)

with tab2:
    st.header("2️⃣ Early Checkouts")
    early = early_checkout(df)
    st.dataframe(early[['booking_id','guest_name','actual_checkout','scheduled_checkout','lost_days','lost_revenue']])
    st.write(f"💰 Total Lost Revenue: ₹{early['lost_revenue'].sum()}")

with tab3:
    st.header("3️⃣ Late Checkouts")
    late = late_checkout(df)
    st.dataframe(late[['booking_id','guest_name','actual_checkout','hours_late','late_fee']])
    st.write(f"💰 Total Late Fees: ₹{late['late_fee'].sum()}")

with tab4:
    st.header("4️⃣ Room Upgrades")
    upgrades = track_upgrades(df)
    st.dataframe(upgrades[['booking_id','guest_name','room_type','actual_room_type','upgrade_requested','upgrade_opportunity']])

with tab5:
    st.header("5️⃣ No-Show & Deposit Summary")
    no_shows, summary = analyze_no_shows(df)
    st.dataframe(no_shows[['booking_id','guest_name','deposit_amount']])
    st.write(f"No-shows: {summary['no_show_count']}, Cancelled: {summary['cancelled_count']}")
    st.write(f"💰 Total Deposits Forfeited: ₹{summary['total_deposit_forfeited']}")
    st.write(f"💰 Total Deposits Refunded: ₹{summary['total_deposit_refunded']}")

with tab6:
    st.header("6️⃣ Occupancy Calendar")
    calendar_df = occupancy_calendar(df)
    st.dataframe(calendar_df)

with tab7:
    st.header("7️⃣ Data Quality Issues")
    missing_names = df[df['missing_guest_name']]
    st.subheader("Missing Guest Names")
    st.dataframe(missing_names[['booking_id','guest_name']])

    missing_checkins = df[df['data_quality_missing_checkin']]
    st.subheader("Missing Actual Check-in Times")
    st.dataframe(missing_checkins[['booking_id','guest_name','scheduled_checkin']])

    missing_checkouts = df[df['data_quality_missing_checkout']]
    st.subheader("Missing Actual Check-out Times")
    st.dataframe(missing_checkouts[['booking_id','guest_name','scheduled_checkout']])

    inconsistent = df[df['status_inconsistent']]
    st.subheader("Status Inconsistencies")
    st.dataframe(inconsistent[['booking_id','guest_name','status','actual_checkin']])
