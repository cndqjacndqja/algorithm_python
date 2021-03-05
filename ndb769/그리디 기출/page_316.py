def solved(food_times, k):
    food_len = len(food_times)
    index = 0
    i = 0
    while i < k:
        if food_times[i % food_len] >= 0:
            food_times[i % food_len] -= 1
            i += 1
            index = i % food_len
    print((index + 1) % food_len + 1)


solved([3, 1, 2], 5)
