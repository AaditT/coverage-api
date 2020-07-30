import requests

def get_location_data(lat, longitude):
    lat= str(lat)
    longitude = str(longitude)

    fips_data = requests.get("https://geo.fcc.gov/api/census/area?lat=" + lat + "&lon=" + longitude + "&format=json")
    fips_json = fips_data.json()
    # print(fips_json)


    return fips_json.get('results')[0].get('county_name')
print(get_location_data(32.7157, -117.1611)) #! testing => san diego
