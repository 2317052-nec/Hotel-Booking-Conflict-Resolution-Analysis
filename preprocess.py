import pandas as pd
from datetime import timedelta

def load_data():
    file_path = r"C:\Users\Manoj\Downloads\hotel_bookings.csv"
    df = pd.read_csv(file_path, on_bad_lines='skip')
    return df

def preprocess_data(df):
    # Rename columns to match expected names
    df = df.rename(columns={
        'check_in_date': 'scheduled_checkin',
        'check_out_date': 'scheduled_checkout',
        'booking_status': 'status',
        'deposit_paid': 'deposit_amount'
    })

    # Add missing columns
    df['actual_room_type'] = df['room_type']
    df['upgrade_requested'] = df['special_requests'].str.contains('Upgrade requested', na=False)
    df['is_vip'] = df['special_requests'].str.contains('VIP', na=False)

    date_cols = ['scheduled_checkin', 'scheduled_checkout', 'actual_checkin', 'actual_checkout']
    for col in date_cols:
        df[col] = pd.to_datetime(df[col], errors='coerce')

    # Data quality flags
    df['data_quality_missing_checkin'] = df['actual_checkin'].isna()
    df['data_quality_missing_checkout'] = df['actual_checkout'].isna()

    df['actual_checkin'] = df['actual_checkin'].fillna(df['scheduled_checkin'] + pd.Timedelta(hours=15))
    df['actual_checkout'] = df['actual_checkout'].fillna(df['scheduled_checkout'] + pd.Timedelta(hours=11))

    df['stay_duration'] = (df['actual_checkout'] - df['actual_checkin']).dt.days
    df['missing_guest_name'] = df['guest_name'].isna()
    df['status_inconsistent'] = ((df['status'] == 'checked-in') & df['data_quality_missing_checkin'])
    return df
