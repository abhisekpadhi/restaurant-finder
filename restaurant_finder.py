import os
import requests

MAPS_API_KEY = os.environ['MAPS_API_KEY']
ZOMATO_API_KEY = os.environ['ZOMATO_API_KEY']
headers = {"user-key": ZOMATO_API_KEY, "Accept": "application/json"}

# Test data
# lat, lng = 12.9199409, 77.61065119999999
# city_id = 4
# cuisine_id = 1024

def find_geocode_by_name(name):
    """
    Returns geocode (lat, lng) from location name
    """
    address = name.replace(' ', '+')
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={MAPS_API_KEY}'
    response = requests.get(url)
    lat, lng = response.json()['results'][0]['geometry']['location']['lat'], response.json()['results'][0]['geometry']['location']['lng']
    return (lat, lng)


def get_city_by_geocode(lat, lng):
    """
    Returns (city_id, city_name) for geocode (lat, lng)
    """
    url = f'https://developers.zomato.com/api/v2.1/cities?lat={lat}&lon={lng}'
    response = requests.get(url, headers=headers)
    return (response.json()['location_suggestions'][0]['id'], response.json()['location_suggestions'][0]['name'])


def get_cusines_by_city(city_id):
    """
    Returns cuisines for city_id
    """
    url = f'https://developers.zomato.com/api/v2.1/cuisines?city_id={city_id}'
    response = requests.get(url, headers=headers)
    return response.json()

def search_restaurant(city_id, cuisine_ids):
    """
    Returns restaurants in a city who server cuisine
    """
    cuisine_ids_comma_separated = ','.join(cuisine_ids)
    url = f'https://developers.zomato.com/api/v2.1/search?entity_id={city_id}&entity_type=city&cuisines={cuisine_ids_comma_separated}'
    response = requests.get(url, headers=headers)
    return response.json()

def get_best_restaurants(search_results):
    best_restaurants = []
    for restaurant in search_results['restaurants']:
        if float(restaurant['restaurant']['user_rating']['aggregate_rating']) > 4.5:
            best_restaurants.append(restaurant)
    return best_restaurants

def get_google_maps_url(address):
    cleaned_address = address.replace(',', '').replace(' ', '+')
    return f'https://maps.google.com/?q={cleaned_address}'

if __name__ == '__main__':
    location = input("What is your location? \n")
    lat, lng = find_geocode_by_name(location)
    city_id, city_name = get_city_by_geocode(lat, lng)
    print(f'-> You are in {city_name}')
    print(f'Here are the cuisines in {city_name}, select your preference:')
    cuisines = get_cusines_by_city(city_id)['cuisines']
    for cuisine in cuisines:
        print(f'{cuisine["cuisine"]["cuisine_id"]}: {cuisine["cuisine"]["cuisine_name"]}')
    cuisine_ids = input("What cusines are in you mood for? \n").split(' ')
    print('Here is the best restaurant we found for you:\n')
    search_results = search_restaurant(city_id, cuisine_ids)
    best_restaurants = get_best_restaurants(search_results)
    if best_restaurants:
        print('Name: ' + best_restaurants[0]['restaurant']['name'])
        print('Find on Zomato: ' + best_restaurants[0]['restaurant']['url'])
        print('Address: ' + best_restaurants[0]['restaurant']['location']['address'])
        print('Find on Maps: ' + get_google_maps_url(best_restaurants[0]['restaurant']['location']['address']))
    else:
        print('No good restaurants found. Try with another cusine or location.')
