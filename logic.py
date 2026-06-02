def cari_club(data, key):
    return [c for c in data if key.lower() in c.nama.lower()]


def bubble_sort(data):
    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):
            if data[j].poin < data[j + 1].poin:
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def binary_search(data, key):
    data = sorted(data, key=lambda x: x.nama.lower())

    l, r = 0, len(data) - 1

    while l <= r:
        m = (l + r) // 2

        if key.lower() in data[m].nama.lower():
            return data[m]

        elif key.lower() < data[m].nama.lower():
            r = m - 1
        else:
            l = m + 1

    return None
