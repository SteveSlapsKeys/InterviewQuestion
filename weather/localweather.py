class LocalWeather:

    def __init__(self, location_name, temp_high, temp_low):
        self.location_name = location_name,
        self.temp_high = temp_high,
        self.temp_low = temp_low


    def __str__(self):
        return f"Location: {self.location_name}, Temp High: {self.temp_high}°F, Temp Low: {self.temp_low}°F"