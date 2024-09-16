def get_venues_for_band(conn, band_name):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT venues.title, venues.city
        FROM concerts
        JOIN venues ON concerts.venue_title = venues.title
        WHERE concerts.band_name = ?
    """, (band_name,))
    return cursor.fetchall()
