from datetime import timedelta
import pandas as pd

def occupancy_calendar(df):
    calendar = []
    for _, row in df.iterrows():
        for d in pd.date_range(row['actual_checkin'].date(), row['actual_checkout'].date() - timedelta(days=1)):
            calendar.append({'date': d, 'room_number': row['room_number'], 'status': row['status']})
    return pd.DataFrame(calendar)
