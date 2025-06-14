import random  # Import the random module for selecting a random pivot
import time
import tracemalloc

def randomized_quicksort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)  # Choosing a random element from the array as the pivot

    equal = [x for x in array if x == pivot]
    less = [x for x in array if x < pivot]
    greater = [x for x in array if x > pivot]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)    

def measure_performance(array, description):
    print(f"\n{description} array:")
    print("Original array :", array[:10], "..." if len(array) > 10 else "")
    tracemalloc.start()

    start_time = time.perf_counter()
    sorted_array = randomized_quicksort(array)

    end_time = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print("Sorted array :  ", sorted_array[:10], "..." if len(sorted_array) > 10 else "")
    print(f"Execution time: {end_time - start_time:.8f} seconds")
    print(f"Peak memory usage: {peak / 1024:.2f} KiB")

if __name__ == "__main__":

    n = int(input("Enter the size of the array: "))

    random_array = [random.randint(1, 100) for _ in range(n)]
    measure_performance(random_array, "Randomly generated array")

    sorted_array = list(range(1, n + 1))
    measure_performance(sorted_array, "Already sorted array")

    reverse_sorted_array = list(range(n, 0, -1))
    measure_performance(reverse_sorted_array, "Reverse sorted array")

    repeated_element = random.randint(1, 100)
    repeated_array = [repeated_element for _ in range(n)]
    measure_performance(repeated_array, f"Array with repeated element ({repeated_element})")
