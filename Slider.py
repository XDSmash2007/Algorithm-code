import random
import time
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def generate_random_array(size, range_start, range_end):
    return [random.randint(range_start, range_end) for _ in range(size)]


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
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output

    
def time_sorting_algorithm(sort_func, arr, trials=5):
    total_time = sum(time_sort(sort_func, arr) for _ in range(trials))
    return total_time / trials

def time_sort(sort_func, arr):
    start_time = time.time()
    sort_func(arr.copy())
    return time.time() - start_time


def interactive_plot():
  
    initial_size = 100
    array_range = (1, 1000000)
    
    fig, ax = plt.subplots()
    plt.subplots_adjust(left=0.1, bottom=0.3)

    sizes = [initial_size]
    quick_sort_times = [time_sorting_algorithm(quick_sort, generate_random_array(initial_size, *array_range))]
    radix_sort_times = [time_sorting_algorithm(radix_sort, generate_random_array(initial_size, *array_range))]
    
    quick_sort_line, = plt.plot(sizes, quick_sort_times, label='Quick Sort', marker='o')
    radix_sort_line, = plt.plot(sizes, radix_sort_times, label='Radix Sort', marker='o')
    
    plt.title("Sorting Algorithm Time Comparison")
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.legend()
    plt.grid(True)


    ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
    slider = Slider(ax_slider, 'Array Size', 10, 50000, valinit=initial_size, valstep=10)

    def update(val):
        size = int(slider.val)


        while sizes and sizes[-1] > size:
            sizes.pop()
            quick_sort_times.pop()
            radix_sort_times.pop()


        if not sizes or sizes[-1] != size:
            new_array = generate_random_array(size, *array_range)
            quick_sort_time = time_sorting_algorithm(quick_sort, new_array)
            radix_sort_time = time_sorting_algorithm(radix_sort, new_array)

            sizes.append(size)
            quick_sort_times.append(quick_sort_time)
            radix_sort_times.append(radix_sort_time)


        quick_sort_line.set_xdata(sizes)
        quick_sort_line.set_ydata(quick_sort_times)
        radix_sort_line.set_xdata(sizes)
        radix_sort_line.set_ydata(radix_sort_times)

        ax.relim()
        ax.autoscale_view()
        plt.draw()

    slider.on_changed(update)
    plt.show()


interactive_plot()