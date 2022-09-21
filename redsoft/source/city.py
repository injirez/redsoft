from geopy.geocoders import Nominatim
import requests as req


def get_coord(city: str) -> list:
    cord = []
    geolocator = Nominatim(user_agent='redsoft')
    location = geolocator.geocode(city)
    cord.append(location.latitude)
    cord.append(location.longitude)

    return cord

url_yandex = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Moscow/2022-09-21/2022-09-21?unitGroup=metric&include=alerts%2Cdays&key=BP8KPU35BEDZTTJCAMTNQVRX4&contentType=json'
yandex_req = req.get(url_yandex, verify=False)
print(yandex_req.text['address'], yandex_req.text['days'], yandex_req.text['temp'], yandex_req.text['temp'], )