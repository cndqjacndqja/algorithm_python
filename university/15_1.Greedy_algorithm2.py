def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity - data[0] >= 0:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            print(fraction, total_value)
            print(capacity, data[0])
            print([data[0], data[1], fraction])
            break
    return total_value, details

if __name__ == "__main__":
    data_list = [(10, 5), (20, 10), (30, 20), (40, 30)]
    value, detail = get_max_value(data_list, 85)
    print(value, detail)

