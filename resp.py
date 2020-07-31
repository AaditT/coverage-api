import requests
import reverse_geocoder as rg

def get_location_data(lat, longitude):
    lat_str= str(lat)
    long_str = str(longitude)

    fips_data = requests.get("https://geo.fcc.gov/api/census/area?lat=" + lat_str + "&lon=" + long_str + "&format=json")
    fips_json = fips_data.json()
    if(len(fips_json['results']) == 0):
        coordinates = (lat, longitude)
        results = rg.search(coordinates,mode=1)
        return results[0]['name'], results[0]['cc']
    return fips_json.get('results')[0].get('county_name')
