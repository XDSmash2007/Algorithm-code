import random
import time
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plot

#Creating the Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

#Creating the Radix Sort
def radix_sort(arr):
    if not arr:
        return arr

    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        arr = counting_sort_radix(arr, exp)
        exp *= 10
    return arr

#Specifying the Radix sort to Counting Radix Sort
def counting_sort_radix(arr, exp):
   
    n = len(arr)
    output = [0] * n 
    count = [0] * 10

    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output(count[index] - 1) = arr(i)
        count(index) -= 1

    return output

#Getting the time from the two algorithms
def time_sorting_algorithm(sort_func, arr, trials=5):
   
    time = sum(time_sort(sort_func, arr) for _ in range(trials))
    return time / trials

def time_sort(sort_func, arr):
   
    start_time = time.time()
    sort_func(arr.copy())  
    return time.time() - start_time

def random_arrays(size, range_start, range_end):
  
    return (random.randint(range_start, range_end) for _ in range(size))

def the_arrays():
  
    array_sizes = [5, 10, 100, 250, 500, 1000, 2500, 5000, 10000, 20000, 50000, 100000]
    arrays_1mill = (random_arrays(array_size, 1, 1000000) for array_size in array_sizes)
    arrays_100bill = (random_arrays(array_size, 1, 100000000000) for array_size in array_sizes)
    return arrays_1mill, arrays_100bill, array_sizes

def time_sorting_algorithms(arrays):
    
    quick_sort_times = []
    radix_sort_times = []
    
    for array in arrays:
        
        quick_sort_time = time_sorting_algorithm(quick_sort, array)
        radix_sort_time = time_sorting_algorithm(radix_sort, array)
        quick_sort_times.append(quick_sort_time)
        radix_sort_times.append(radix_sort_time)
        print(f"Quick sort Times: {quick_sort_times}")
        print(f"Radix Sort Times: {radix_sort_times}")
    
    return quick_sort_times, radix_sort_times

def plotting_times(sizes, quick_sort_times_1mill, radix_sort_times_1mill, quick_sort_times_100bill, radix_sort_times_100bill):
 
    plot.figure(figsize=(12, 8))
    plot.plot(sizes, quick_sort_times_1mill, marker='o', label='Quick Sort (1 to 1M)')
    plot.plot(sizes, radix_sort_times_1mill, marker='o', label='Radix Sort (1 to 1M)')
    plot.plot(sizes, quick_sort_times_100bill, marker='o', linestyle='--', label='Quick Sort (1 to 100B)')
    plot.plot(sizes, radix_sort_times_100bill, marker='o', linestyle='--', label='Radix Sort (1 to 100B)')
    plot.title('Sorting Algorithm Quick sort vs Radix Counting sort')
    plot.xlabel('Array Size')
    plot.ylabel('Time in seconds')
    plot.xticks(sizes)
    plot.legend()
    plot.grid(True)
    plot.tight_layout() 
    plot.show()

def show_array(title, array):
   
    messagebox.showinfo(title, str(array))

def GUI(arrays):
 
    root = tk.Tk()
    root.title("Unsorted and Sorted Arrays")

    for i, array in enumerate(arrays):
        unsorted_button = tk.Button(
            root, text=f"Unsorted Array {i + 1} (size: {len(array)})", 
            command=lambda i=i: show_array(f"Unsorted Array {i + 1}", arrays[i])
        )
        unsorted_button.grid(row=i, column=0, padx=10, pady=5)

        quick_sort_button = tk.Button(
            root, text=f"Quick Sort Array {i + 1}", 
            command=lambda i=i: show_array(f"Quick Sort Array {i + 1}", quick_sort(arrays[i].copy()))
        )
        quick_sort_button.grid(row=i, column=1, padx=10, pady=5)

        radixsort_button = tk.Button(
            root, text=f"Radix Sort Array {i + 1}", 
            command=lambda i=i: show_array(f"Radix Sort Array {i + 1}", radix_sort(arrays[i].copy()))
        )
        radixsort_button.grid(row=i, column=2, padx=10, pady=5)

    root.mainloop()



arrays_1mill, arrays_100bill, sizes = the_arrays()
quick_sort_times_1m, radix_sort_times_1m = time_sorting_algorithms(arrays_1mill)
quick_sort_times_100b, radix_sort_times_100b = time_sorting_algorithms(arrays_100bill)


plotting_times(sizes, quick_sort_times_1m, radix_sort_times_1m, quick_sort_times_100b, radix_sort_times_100b)


GUI(arrays_1mill + arrays_100bill)