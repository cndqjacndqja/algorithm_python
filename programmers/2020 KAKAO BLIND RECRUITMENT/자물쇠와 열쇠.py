def solution(key, lock):
    stand_zip = find_lock(lock)
    result = find_key(key, stand_zip)
    print(result)


def find_stand_lock(lock):
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0:
                return i, j


def find_lock(lock):
    stand_x, stand_y = find_stand_lock(lock)
    stand_zip = []
    for i in range(len(lock)):
        for j in range(len(lock)):
            if lock[i][j] == 0 and not stand_x == i and not stand_y == j:
                stand_zip.append((stand_x - i, stand_y - j))
    return stand_zip


def find_key(key, stand_zip):
    for i in range(len(key)):
        for j in range(len(key)):
            if key[i][j] == 1:
                for z in stand_zip:
                    x, y = z
                    if key[i - x][j - y] == 0:
                        continue
                    return True
    return False


solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])
