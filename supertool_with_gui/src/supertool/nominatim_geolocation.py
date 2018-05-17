import requests


def nominatim_request(address: str)-> dict:
    """
    Function which creates nominatim requests and gets data

    :param address:
    :return:
    """
    url = "http://nominatim.openstreetmap.org"
    postfix_url = "/search"

    query_params = {
        "q": address,
        'format': 'json'
    }
    response = requests.get(url + postfix_url, params=query_params)
    return response


def get_coordinates(address: str)-> dict:
    """
    Function which return from data coordinates and name

    :param data:
    :return:
    """
    response = nominatim_request(address).json()

    if not response:
        raise ValueError(f'Incorrect address: {address}')

    data = {
        "display_name": response[0]['display_name'],
        "coordinates": {"lat": response[0]['lat'],
                        "lon": response[0]['lon']
                        }
    }
    return data


if __name__ == '__main__': #pragma no cover
    pass
