from models import Band, Venue, Concert

def main():
    # Example Instances
    band_name = 'The Rockers'
    venue_title = 'The Big Hall'
    concert_date = '2024-09-30'
    concert_id = 1  # Example concert ID

    # Band Operations
    band = Band(band_name)
    print("Band Concerts:", band.concerts())
    print("Band Venues:", band.venues())
    band.play_in_venue(venue_title, concert_date)
    print("All Introductions for Band:", band.all_introductions())
    print("Band with Most Performances:", Band.most_performances().name)

    # Venue Operations
    venue = Venue(venue_title)
    print("Venue Concerts:", venue.concerts())
    print("Venue Bands:", venue.bands())
    print("Concert on Date:", venue.concert_on(concert_date))
    print("Most Frequent Band at Venue:", venue.most_frequent_band().name)

    # Concert Operations
    concert = Concert(concert_id)
    print("Concert Band:", concert.band().name)
    print("Concert Venue:", concert.venue().title)
    print("Hometown Show:", concert.hometown_show())
    print("Concert Introduction:", concert.introduction())

if __name__ == "__main__":
    main()

