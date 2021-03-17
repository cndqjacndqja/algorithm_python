from bisect import bisect_left, bisect_right


def solution(words, queries):
    list_words = [[] for _ in range(100001)]
    reverse_list_words = [[] for _ in range(100001)]
    for i in words:
        list_words[len(i)].append(i)
        reverse_list_words[len(i)].append(i[::-1])

    for i in range(100001):
        list_words[i].sort()
        reverse_list_words[i].sort()

    result = []

    for i in queries:
        if i[0] != '?':
            count = bisect_count_range(list_words[len(i)], i.replace('?', 'a'), i.replace('?', 'z'))
        else:
            count = bisect_count_range(reverse_list_words[len(i)], i[::-1].replace('?', 'a'), i[::-1].replace('?', 'z'))
        result.append(count)
    return result


def bisect_count_range(a, left, right):
    left_word = bisect_left(a, left)
    right_word = bisect_right(a, right)
    return right_word - left_word


print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "????o", "fr???", "fro???", "pro?"]))
