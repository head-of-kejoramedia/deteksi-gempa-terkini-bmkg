import requests
from bs4 import BeautifulSoup


def ekstraksi_data():
    """
    Waktu: 30 Januari 2023
    Waktu: 13: 24:19 WIB
    Magnitudo: 3.2
    Kedalaman: 3 km
    Lokasi: LS=3.33 LS BT=128.35
    Pusat Gempa: Pusat gempa berada di darat 1 km Utara Kairatu
    Dirasakan: Dirasakan(Skala MMI): III Kairatu
    :return:
    """
    try:
        content = requests.get("https://bmkg.go.id")
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')

        result = soup.find('div',{'class':'col-md-6 col-xs-6 gempabumi-detail no-padding'})
        result = result.findChildren('li')

        tanggal_waktu = result[0].text
        tanggal = tanggal_waktu.split(',')[0]
        waktu = tanggal_waktu.split(',')[1]
        magnitude =  result[1].text
        kedalaman =  result[2].text
        lokasi =  result[3].text
        pusat_gempa =  result[4].text
        dirasakan =  result[5].text

        hasil = {'Tanggal': tanggal,
                 'Waktu': waktu,
                 'Magnitudo': magnitude,
                 'Kedalaman': kedalaman,
                 'Lokasi': lokasi,
                 'Pusat Gempa': pusat_gempa,
                 'Dirasakan': dirasakan}
        return hasil

    else:
        return None

def tampilkan_data(result):
    """ Tampilakn Data Result"""
    if result is None:
        print('Data Tidak ada gempa dari BMKG')
        return

    print('Gempa terkini  berdasarkan BMKG')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lokasi {result['Lokasi']}")
    print(f"{result['Pusat Gempa']}")
    print(f"{result['Dirasakan']}")
    print('\nSelalu Waspada Untuk Penduduk Area Di Atas')


