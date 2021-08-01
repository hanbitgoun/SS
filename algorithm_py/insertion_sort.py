def insertion_sort(data_list):
    for n in range(1, len(data_list)):
        for i in range(n, 0, -1):
            if data_list[i - 1] > data_list[i]:
                data_list[i - 1], data_list[i] = data_list[i], data_list[i - 1]
                
    return data_list

def insertion_sort_2(data_list):
    for i in range(1, len(data_list)):
        value = data_list[i]
        while i > 0 and data_list[i - 1] > value:
            data_list[i] = data_list[i - 1]
            i -= 1
        data_list[i] = value
    return data_list
