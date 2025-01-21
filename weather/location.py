class Location:

    def __init__(self, name, zip, lat, lon):
        self.name = name
        self.zip = zip
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return self.name + ", " + self.zip + ", lat: " + self.lat + ", lon: " + self.lon