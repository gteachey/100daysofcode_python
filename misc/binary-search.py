from random import randint


def binary_search(array_list, item):
    low = 0
    high = len(array_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = array_list[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_array = list(range(0, 9999))
for i in range(0, 100):
    find_num = randint(0, 19999)
    # find_num = randint(0,len(my_array))
    print(binary_search(my_array, find_num))
# print(binary_search(my_list, 13))

# for num in my_array:    
# #     print( num )
# def find_number(my_array):
#     min = my_array[0] 
#     max = my_array[-1]
#     guess = int(len(my_array)/2)
#     tries = 0
#     while guess  != find_num:
#         if guess < find_num:
#             min = guess
#             list_index = my_array.index(min)
#             my_array = my_array[list_index:]
#         else:
#             max = guess
#             list_index = my_array.index(max)
#             my_array = my_array[0:list_index]
#         num = int(len(my_array)/2)
#         guess = my_array[num]
#         tries += 1
#         if max == min and \
#             guess != find_num:
#             return -1
#     return tries        


#
