class Location:

    def __init__(self, zip, lat, lon):
        self.zip = zip
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"Latitude: {self.lat}°, Longitude: {self.lon}°"