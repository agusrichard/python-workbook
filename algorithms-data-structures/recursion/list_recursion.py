def normalrevlist(lst):
    accumulator = []
    for x in lst:
        accumulator = [x] + accumulator

    return accumulator

def recrevlist(lst):
    if lst == []:
        return []

    restrev = recrevlist(lst[1:])
    first = lst[0:1]
    result = restrev + first
    
    return result

def recrevlist2(lst):
    def helper(index):
        if index == -1:
            return []

        restrev = helper(index-1)
        first = [lst[index]]

        result = first + restrev

        return result

    return helper(len(lst) - 1)

if __name__ == '__main__':
    print(normalrevlist([1, 2, 3, 4, 5]))
    print(recrevlist([1, 2, 3, 4, 5]))
    print(recrevlist2([1, 2, 3, 4, 5]))