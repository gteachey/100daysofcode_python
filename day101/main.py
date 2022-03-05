def sym(*args):
    new_array = args[0]
    count = 1
    while count < len(args):
        for item in args[count]:
            if item in new_array:
                new_array.pop(new_array.index(item))
            else:
                new_array.append(item)
        count += 1
        new_array.sort()
    return new_array

    # print(len(args))


print(sym([1, 2, 3], [5, 2, 1, 4]))
