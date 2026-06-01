def cari_club(data, keyword):
    return [c for c in data if keyword.lower() in c.nama.lower()]


def bubble_sort_poin(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j].poin < data[j + 1].poin:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data


def rekomendasi_top(data, top_n=3):
    data = bubble_sort_poin(data)
    return data[:top_n]


def rekomendasi_liga(data, liga):
    filtered = [c for c in data if c.liga.lower() == liga.lower()]
    return bubble_sort_poin(filtered)
