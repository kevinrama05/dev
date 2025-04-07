def insertion_sort(my_array):
    
    n = len(my_array)
    for i in range(1, n):
        index = i
        element = my_array.pop(i)
        for j in range(i - 1, -1, -1):
            if my_array[j] > element:
                index = j

        my_array.insert(index, element)

    return my_array

def bubble_sort(my_array):

    n = len(my_array)


    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

    return my_array



my_array = [5, 6, 7 ,1, 3, 8, 41, 15, 42, 62, 1, 12, 12]


print(bubble_sort(my_array))