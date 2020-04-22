def solution(record):
    answer = []
    d = {}
    for x in record:      
        tmp = x.split(' ')
        if tmp[0] == "Enter" or tmp[0] == "Change":
            d[tmp[1]] = tmp[2]
    for x in record:
        tmp = x.split(' ')
        name = d[tmp[1]]
        if tmp[0] == "Enter":
            answer.append(name + "님이 들어왔습니다.")
        elif tmp[0] == "Leave":
            answer.append(name + "님이 나갔습니다.")
        else:
            continue
    return answer