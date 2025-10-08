def track_upgrades(df):
    df = df.copy()
    df['upgraded'] = df['room_type'] != df['actual_room_type']
    df['upgrade_opportunity'] = df['upgrade_requested'] & ~df['upgraded']
    return df[df['upgraded'] | df['upgrade_requested'].notna()]
