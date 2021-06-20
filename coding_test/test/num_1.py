def solution(S, C):
    data = S.split("; ")
    lower_data = [i.lower() for i in data]
    result = []
    for i in lower_data:
        add_data = ""
        split_data = i.split(" ")
        for j in range(len(split_data)):
            if j == 1 and len(split_data) == 3:
                continue
            else:
                if split_data[j].count("-") > 0:
                    split_data[j] = space_num(split_data[j])
            add_data += split_data[j]
            if j == 0:
                add_data += "."
        result.append(add_data)
    print(result)





def space_num(s):
    data = ""
    for i in s:
        if i == '-':
            continue
        else:
            data+=i
    return data



