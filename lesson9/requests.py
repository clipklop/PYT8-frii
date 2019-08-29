#
import requests


def find_pet_by_status(status):
    params = {'status': status}
    headers = {
        'Accept': 'application/json'
    }
    url = 'http://petstore.swagger.io/v2/pet/findByStatus'
    r = requests.get(url, params=params, headers=headers)
    print(r.status_code, r.headers)
    print(r.content)

    # s = 'http://petstore.swagger.io/v2/pet/findByStatus?status=sold'


if __name__ == '__main__':
    find_pet_by_status('sold')
