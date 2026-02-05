import requests
from .models import Produk, Kategori, Status

API_URL = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
USERNAME = "tesprogrammer040226C15"
PASSWORD = "4003304cd3cc911ee562a8fb0392390c"

def fetch_and_save_produk():
    payload = {"username": USERNAME, "password": PASSWORD}

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        # Gunakan form-urlencoded
        response = requests.post(API_URL, data=payload, headers=headers, timeout=10)
        print("HTTP status code:", response.status_code)
        print("Raw response text:", response.text[:500])

        response.raise_for_status()
        data = response.json()
        print("Parsed JSON:", data)

        for item in data.get("data", []):
            # Ubah tipe id_produk & harga ke integer
            id_produk = int(item["id_produk"])
            harga = int(item["harga"])

            # Ambil atau buat kategori
            kategori_obj, _ = Kategori.objects.get_or_create(
                nama_kategori=item["kategori"]
            )

            # Ambil atau buat status
            status_obj, _ = Status.objects.get_or_create(
                nama_status=item["status"]
            )

            # Simpan / update produk
            Produk.objects.update_or_create(
                id_produk=id_produk,
                defaults={
                    "nama_produk": item["nama_produk"],
                    "harga": harga,
                    "kategori": kategori_obj,
                    "status": status_obj
                }
            )
            print(f"Produk disimpan/update: {item['nama_produk']}")

        return True

    except requests.exceptions.RequestException as e:
        print("Error fetching API:", e)
        return False
    except ValueError as e:
        print("Error parsing JSON:", e)
        print("Response text:", response.text)
        return False
