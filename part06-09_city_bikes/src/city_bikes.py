def file_to_dict(filename: str):
    file_to_list = []
    file_to_dict = {}
    with open(filename) as new_file:
        for row in new_file:
            if "Longitude" not in row:
                row = row.replace("\n", "")
                file_to_list.append(row.split(";"))
        for station in file_to_list:
            file_to_dict[station[3]] = station
    return file_to_dict

def get_station_data(filename: str):
    station_data = file_to_dict(filename)
    station_location = {}
    for key, value in station_data.items():
        station_location[key] = (float(value[0]), float(value[1]))
    return station_location
    
def distance(stations: dict, station1: str, station2: str):
    import math
    x_km = (stations[station1][0] - stations[station2][0]) * 55.26
    y_km = (stations[station1][1] - stations[station2][1]) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)
    return distance_km
  
def greatest_distance(stations: dict):
    max_distance = 0.0
    for key in stations:
        for key2 in stations:
            if distance(stations, key, key2) > max_distance:
                max_distance = distance(stations, key, key2)
                station_max_distance = (key, key2, max_distance)
    return station_max_distance
    
if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)