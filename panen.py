# data panen
data_panen = {
    "lokasi1": {
        "padi": 1000,
        "jagung": 500,
        "kedelai": 250
    },
    "lokasi2": {
        "padi": 1500,
        "jagung": 900,
        "kedelai": 400
    },
    "lokasi3": {
        "padi": 1200,
        "jagung": 450,
        "kedelai": 300
    }
}

# 1. tampilkan seluruh data
for lokasi, hasil in data_panen.items():
    print("Lokasi:", lokasi)
    print("Padi:", hasil["padi"])
    print("Jagung:", hasil["jagung"])
    print("Kedelai:", hasil["kedelai"])
    print("-----")

# 2. jumlah hasil panen jagung dari lokasi2
print("Jagung lokasi2:", data_panen["lokasi2"]["jagung"])

# 3. tampilkan nama lokasi dari lokasi3
print("Nama lokasi:", "lokasi3")

# 4 & 5. simpan padi dan kedelai ke variabel berbeda
padi_lokasi1 = data_panen["lokasi1"]["padi"]
kedelai_lokasi1 = data_panen["lokasi1"]["kedelai"]

padi_lokasi2 = data_panen["lokasi2"]["padi"]
kedelai_lokasi2 = data_panen["lokasi2"]["kedelai"]

padi_lokasi3 = data_panen["lokasi3"]["padi"]
kedelai_lokasi3 = data_panen["lokasi3"]["kedelai"]

# 6. percabangan perhatian khusus
for lokasi, hasil in data_panen.items():
    if hasil["padi"] > 1300 or hasil["jagung"] > 800:
        print(lokasi, "perlu perhatian khusus")
    else:
        print(lokasi, "kondisi baik")
