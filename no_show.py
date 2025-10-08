def analyze_no_shows(df):
    no_shows = df[df['status'] == 'no-show']
    cancelled = df[df['status'] == 'cancelled']
    no_show_deposit = no_shows['deposit_amount'].sum()
    cancelled_deposit = cancelled['deposit_amount'].sum()
    total_forfeited = no_show_deposit  # deposits forfeited for no-shows
    total_refunded = cancelled_deposit  # deposits refunded for cancellations
    summary = {
        'no_show_count': len(no_shows),
        'cancelled_count': len(cancelled),
        'total_deposit_forfeited': total_forfeited,
        'total_deposit_refunded': total_refunded
    }
    return no_shows, summary
