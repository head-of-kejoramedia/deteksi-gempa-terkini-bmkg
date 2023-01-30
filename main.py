"""
Aplikasi Deteksi Gempa Terkini
MODULARISASI DENGAN FUNCTION
"""

def ekstraksi_data():
    """
    Tanggal: 30 Januari 2023
    Waktu: 13: 24:19 WIB
    Magnitudo: 3.2
    Kedalaman: 3 km
    Lokasi: LS=3.33 LS BT=128.35
    Pusat Gempa: Pusat gempa berada di darat 1 km Utara Kairatu
    Dirasakan: Dirasakan(Skala MMI): III Kairatu
    :return:
    """
    hasil = dict()
    hasil['Tanggal'] = '30 Januari 2023'
    hasil['Waktu'] = '13: 24:19 WIB'
    hasil['Magnitudo'] = '3.2'
    hasil['Kedalaman'] = '3 km'
    hasil['Lokasi'] = {'LS': 3.33, 'BT': 128.35}
    hasil['Pusat Gempa'] = 'Pusat gempa berada di darat 1 km Utara Kairatu'
    hasil['dirasakan'] = "Dirasakan (Skala MM1): III kairatu"

    return hasil

def tampilkan_data(result):
    print('Gempa terkini  berdasarkan BMKG')
    print(f"Tanggal {result['Tanggal']}")
    print(f"Waktu {result['Waktu']}")
    print(f"Magnitudo {result['Magnitudo']}")
    print(f"Kedalaman {result['Kedalaman']}")
    print(f"Lokasi: LS= {result['Lokasi']['LS']}, BT= {result['Lokasi']['BT']}")
    print(f"Pusat Gempa {result['Pusat Gempa']}")
    print(f"dirasakan {result['dirasakan']}")

if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)

    
