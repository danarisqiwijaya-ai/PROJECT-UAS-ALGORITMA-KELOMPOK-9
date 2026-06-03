def linear_search_recommendation(hp_list, max_harga, min_ram):
    hasil_filter = []
    for hp in hp_list:
        if hp.harga <= max_harga and hp.ram >= min_ram:
            hasil_filter.append(hp)
    return hasil_filter

def selection_sort_by_price(hp_list, ascending=True):
    n = len(hp_list)
    for i in range(n):
        min_max_idx = i
        for j in range(i + 1, n):
            if ascending:
                if hp_list[j].harga < hp_list[min_max_idx].harga:
                    min_max_idx = j
            else:
                if hp_list[j].harga > hp_list[min_max_idx].harga:
                    min_max_idx = j
        hp_list[i], hp_list[min_max_idx] = hp_list[min_max_idx], hp_list[i]
    return hp_list
