def bubble_sort(my_array):

    n = len(my_array)
    x = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if my_array[j] > my_array[j+1]:
                my_array[j], my_array[j+1] = my_array[j+1], my_array[j]
                x += 1

    return my_array, x

my_array = [7, 2, 4, 1, 5]

sorted, times = bubble_sort(my_array)
print(f"Sorted Numbers: {sorted}")
print(f"Number of swaps: {times}")