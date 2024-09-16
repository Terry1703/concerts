def get_bands_for_venue(conn, venue_title):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT bands.name, bands.hometown
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        WHERE concerts.venue_title = ?
    """, (venue_title,))
    return cursor.fetchall()
