import pandas as pd

ROOM_RATES = {'Standard': 3000, 'Deluxe': 4500, 'Suite': 8000}

def early_checkout(df):
    df = df.copy()
    df['early_checkout'] = (df['actual_checkout'] < df['scheduled_checkout']) & ~df['data_quality_missing_checkout']
    df['lost_days'] = (df['scheduled_checkout'] - df['actual_checkout']).dt.days
    df['lost_revenue'] = df['lost_days'] * df['room_type'].map(ROOM_RATES)
    return df[df['early_checkout']]

def late_checkout(df):
    df = df.copy()
    standard_checkout = pd.to_datetime('11:00:00').time()
    df['late_checkout'] = (df['actual_checkout'].dt.time > standard_checkout) & ~df['data_quality_missing_checkout']
    df['hours_late'] = (df['actual_checkout'] - df['scheduled_checkout']).dt.total_seconds() / 3600
    def calculate_fee(row):
        h = row['hours_late']
        rate = ROOM_RATES[row['room_type']]
        if h <= 1:
            return 0
        elif 1 < h <= 2:
            return 0.25 * rate
        elif 2 < h <= 4:
            return 0.25 * rate  # as per prompt, but perhaps intended 0.5
        elif 4 < h <= 6:
            return 0.5 * rate
        else:
            return rate
    df['late_fee'] = df.apply(calculate_fee, axis=1)
    return df[df['late_checkout']]
