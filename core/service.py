import requests

API_URL = "https://recruitment.fastprint.co.id/tes/programmer"
USERNAME = "tesprogrammer030226C12"
PASSWORD = "bisacoding-3-2-26"

def fetch_produk_api():
    payload = {
        "username": USERNAME,
        "password": PASSWORD
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()  # error kalau status bukan 200
        return response.json()
    except requests.exceptions.HTTPError as errh:
        print("HTTP Error:", errh)
    except requests.exceptions.ConnectionError as errc:
        print("Error Connecting:", errc)
    except requests.exceptions.Timeout as errt:
        print("Timeout Error:", errt)
    except requests.exceptions.RequestException as err:
        print("Something went wrong:", err)
