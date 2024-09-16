def get_band_for_concert(conn, concert_id):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT bands.name, bands.hometown
        FROM concerts
        JOIN bands ON concerts.band_name = bands.name
        WHERE concerts.id = ?
    """, (concert_id,))
    return cursor.fetchone()
