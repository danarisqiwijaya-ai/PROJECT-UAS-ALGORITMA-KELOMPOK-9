liga_map = {}

def cari_club(data, keyword):

    hasil = []

    for c in data:
        if keyword.lower() in c.get_nama().lower():
            hasil.append(c)

    return hasil


def bubble_sort(data):

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            if data[j].get_poin() < data[j + 1].get_poin():
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def tambah_ke_liga(club):

    liga = club.get_liga()

    if liga not in liga_map:
        liga_map[liga] = []

    liga_map[liga].append(club)
