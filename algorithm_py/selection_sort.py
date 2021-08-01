def selection_sort(data_list):

    for i in range(0, len(data_list) - 1):
        min_idx = i
        for j in range(i + 1, len(data_list)):
            if data_list[j] < data_list[min_idx]:
                min_idx = j
                
        data_list[i],data_list[min_idx] = data_list[min_idx], data_list[i]
        
    return data_list

