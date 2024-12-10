import heapq
import math
from collections import deque

class SearchLibrary:
    def __init__(self):
        self.data_structures = {}

    def add_list(self, name, values):
        """Add a list to the library."""
        self.data_structures[name] = sorted(values) if name.startswith("sorted_") else values

    def add_graph(self, name, edges):
        """Add a graph to the library with detailed steps."""
        graph = {}

        for edge in edges:
            u, v = edge

            if u not in graph:
                print(f"Node {u} not found in graph, adding it.")
                graph[u] = []
            else:
                print(f"Node {u} already exists in graph.")

            if v not in graph:
                print(f"Node {v} not found in graph, adding it.")
                graph[v] = []
            else:
                print(f"Node {v} already exists in graph.")
            
            graph[u].append(v)
            graph[v].append(u)

            print(f"Added edge ({u}, {v}). Current graph state: {graph}")

        if name in self.data_structures:
            print(f"Warning: A graph with the name '{name}' already exists. It will be overwritten.")
        
        self.data_structures[name] = graph
        print(f"Graph '{name}' has been added to the library.")

    def binary_search(self, name, target):
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        if data != sorted(data):
            raise ValueError(f"List '{name}' must be sorted for binary search.")
        low, high = 0, len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return f"Found {target} at index {mid} in list '{name}'."
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return f"{target} not found in list '{name}'."

    def interpolation_search(self, name, target):
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        low, high = 0, len(data) - 1
        while low <= high and data[low] <= target <= data[high]:
            if low == high:
                if data[low] == target:
                    return f"Found {target} at index {low} in list '{name}'."
                return f"{target} not found in list '{name}'."
            mid = low + ((target - data[low]) * (high - low)) // (data[high] - data[low])
            if data[mid] == target:
                return f"Found {target} at index {mid} in list '{name}'."
            elif data[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return f"{target} not found in list '{name}'."

    import math

    def jump_search(self, name, target):
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        
        n = len(data)
        if n == 0: 
            return f"{target} not found in list '{name}'."
        
        step = int(math.sqrt(n))
        prev = 0
        
        while data[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return f"{target} not found in list '{name}'."
        
        while data[prev] < target:
            prev += 1
            if prev == min(step, n):
                return f"{target} not found in list '{name}'."
        
        if data[prev] == target:
            return f"Found {target} at index {prev} in list '{name}'."
        
        return f"{target} not found in list '{name}'."

    def fibonacci_search(self, name, target):
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        n = len(data)
        fib_m_2 = 0
        fib_m_1 = 1
        fib = fib_m_1 + fib_m_2
        while (fib < n):
            fib_m_2 = fib_m_1
            fib_m_1 = fib
            fib = fib_m_1 + fib_m_2
        offset = -1
        while (fib > 1):
            i = min(offset + fib_m_2, n-1)
            if (data[i] < target):
                fib = fib_m_1
                fib_m_1 = fib_m_2
                fib_m_2 = fib - fib_m_1
                offset = i
            elif (data[i] > target):
                fib = fib_m_2
                fib_m_1 = fib_m_1 - fib_m_2
                fib_m_2 = fib - fib_m_1
            else:
                return f"Found {target} at index {i} in list '{name}'."
        if (fib_m_1 and offset + 1 < n and data[offset + 1] == target):
            return f"Found {target} at index {offset+1} in list '{name}'."
        return f"{target} not found in list '{name}'."

    def linear_search(self, name, target):
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        for i, value in enumerate(data):
            if value == target:
                return f"Found {target} at index {i} in list '{name}'."
        return f"{target} not found in list '{name}'."

    def bubble_sort(self, name):
        """Bubble Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
        return f"Bubble Sort result for '{name}': {data}"

    def selection_sort(self, name):
        """Selection Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        n = len(data)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if data[j] < data[min_idx]:
                    min_idx = j
            data[i], data[min_idx] = data[min_idx], data[i]
        return f"Selection Sort result for '{name}': {data}"

    def insertion_sort(self, name):
        """Insertion Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return f"Insertion Sort result for '{name}': {data}"

    def merge_sort(self, name):
        """Merge Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        
        def merge(left, right):
            result = []
            while left and right:
                if left[0] < right[0]:
                    result.append(left.pop(0))
                else:
                    result.append(right.pop(0))
            result.extend(left)
            result.extend(right)
            return result

        def sort(data):
            if len(data) <= 1:
                return data
            mid = len(data) // 2
            left = sort(data[:mid])
            right = sort(data[mid:])
            return merge(left, right)

        sorted_data = sort(data)
        return f"Merge Sort result for '{name}': {sorted_data}"

    def quick_sort(self, name):
        """Quick Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        
        def sort(data):
            if len(data) <= 1:
                return data
            pivot = data[0]
            less = [x for x in data[1:] if x <= pivot]
            greater = [x for x in data[1:] if x > pivot]
            return sort(less) + [pivot] + sort(greater)

        sorted_data = sort(data)
        return f"Quick Sort result for '{name}': {sorted_data}"

    def heap_sort(self, name):
        """Heap Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        
        def heapify(data, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and data[i] < data[left]:
                largest = left
            if right < n and data[largest] < data[right]:
                largest = right
            if largest != i:
                data[i], data[largest] = data[largest], data[i]
                heapify(data, n, largest)
        
        n = len(data)
        for i in range(n // 2 - 1, -1, -1):
            heapify(data, n, i)
        for i in range(n - 1, 0, -1):
            data[i], data[0] = data[0], data[i]
            heapify(data, i, 0)
        return f"Heap Sort result for '{name}': {data}"

    def radix_sort(self, name):
        """Radix Sort Algorithm."""
        data = self.data_structures.get(name)
        if not isinstance(data, list):
            raise ValueError(f"'{name}' is not a list.")
        
        def counting_sort(data, exp):
            n = len(data)
            output = [0] * n
            count = [0] * 10
            for i in range(n):
                index = data[i] // exp
                count[index % 10] += 1
            for i in range(1, 10):
                count[i] += count[i - 1]
            for i in range(n - 1, -1, -1):
                index = data[i] // exp
                output[count[index % 10] - 1] = data[i]
                count[index % 10] -= 1
            for i in range(n):
                data[i] = output[i]
        
        max_num = max(data)
        exp = 1
        while max_num // exp > 0:
            counting_sort(data, exp)
            exp *= 10
        return f"Radix Sort result for '{name}': {data}"

search_lib = SearchLibrary()

search_lib.add_list("unsorted_numbers", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
search_lib.add_list("sorted_numbers", [1, 2, 3, 4, 5, 6, 9])

print(search_lib.linear_search("unsorted_numbers", 5))
print(search_lib.binary_search("sorted_numbers", 5))
print(search_lib.jump_search("unsorted_numbers", 5))
print(search_lib.interpolation_search("sorted_numbers", 5))
print(search_lib.fibonacci_search("sorted_numbers", 5))

print(search_lib.bubble_sort("unsorted_numbers"))
print(search_lib.selection_sort("unsorted_numbers"))
print(search_lib.insertion_sort("unsorted_numbers"))
print(search_lib.merge_sort("unsorted_numbers"))
print(search_lib.quick_sort("unsorted_numbers"))
print(search_lib.heap_sort("unsorted_numbers"))
print(search_lib.radix_sort("unsorted_numbers"))