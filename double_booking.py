import pandas as pd

def detect_double_bookings(df):
    conflicts = []
    for room in df['room_number'].unique():
        room_df = df[df['room_number'] == room].sort_values('actual_checkin')
        for i in range(len(room_df) - 1):
            current = room_df.iloc[i]
            next_booking = room_df.iloc[i + 1]
            if current['actual_checkout'] > next_booking['actual_checkin']:
                # Calculate priority: checked-in > confirmed, VIP higher, higher deposit
                def get_priority(row):
                    pri = 0
                    if row['status'] == 'checked-in':
                        pri += 10
                    elif row['status'] == 'confirmed':
                        pri += 5
                    if row['is_vip']:
                        pri += 5
                    pri += row['deposit_amount'] / 100  # scale deposit
                    return pri

                pri1 = get_priority(current)
                pri2 = get_priority(next_booking)
                higher_pri = current['booking_id'] if pri1 > pri2 else next_booking['booking_id']
                resolution = f"Cancel or reassign lower priority booking {next_booking['booking_id'] if pri1 > pri2 else current['booking_id']}. Consider upgrade if possible."

                conflicts.append({
                    'room_number': room,
                    'booking_1': current['booking_id'],
                    'guest_1': current['guest_name'],
                    'priority_1': pri1,
                    'booking_2': next_booking['booking_id'],
                    'guest_2': next_booking['guest_name'],
                    'priority_2': pri2,
                    'overlap_start': next_booking['actual_checkin'],
                    'overlap_end': current['actual_checkout'],
                    'higher_priority_booking': higher_pri,
                    'recommended_resolution': resolution
                })
    return pd.DataFrame(conflicts)
