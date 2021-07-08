def solution(record):
    dic = {}
    result = []
    for com in record:
        if com.split(" ")[0] == "Enter" or com.split(" ")[0] == "Change":
            dic[com.split(" ")[1]] = com.split(" ")[2]

    for com in record:
        if com.split(" ")[0] == "Enter":
            result.append("{}님이 들어왔습니다.".format(dic[com.split(" ")[1]]))
        elif com.split(" ")[0] == "Leave":
            result.append("{}님이 나갔습니다.".format(dic[com.split(" ")[1]]))

    return result

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])