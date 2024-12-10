import unittest
from searching.program import SearchLibrary

class TestSearchLibrary(unittest.TestCase):

    def setUp(self):
        """Set up a SearchLibrary instance for testing."""
        self.search_lib = SearchLibrary()

        # Add some sample lists to the search library
        self.search_lib.add_list("unsorted_numbers", [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        self.search_lib.add_list("sorted_numbers", [1, 2, 3, 4, 5, 6, 9])
        self.search_lib.add_list("empty_list", [])

    # Test Search Algorithms
    def test_linear_search_found(self):
        result = self.search_lib.linear_search("unsorted_numbers", 5)
        self.assertEqual(result, "Found 5 at index 4 in list 'unsorted_numbers'.")

    def test_linear_search_not_found(self):
        result = self.search_lib.linear_search("unsorted_numbers", 10)
        self.assertEqual(result, "10 not found in list 'unsorted_numbers'.")

    def test_binary_search_found(self):
        result = self.search_lib.binary_search("sorted_numbers", 5)
        self.assertEqual(result, "Found 5 at index 4 in list 'sorted_numbers'.")

    def test_binary_search_not_found(self):
        result = self.search_lib.binary_search("sorted_numbers", 10)
        self.assertEqual(result, "10 not found in list 'sorted_numbers'.")

    def test_interpolation_search_found(self):
        result = self.search_lib.interpolation_search("sorted_numbers", 5)
        self.assertEqual(result, "Found 5 at index 4 in list 'sorted_numbers'.")

    def test_interpolation_search_not_found(self):
        result = self.search_lib.interpolation_search("sorted_numbers", 10)
        self.assertEqual(result, "10 not found in list 'sorted_numbers'.")

    def test_jump_search_found(self):
        result = self.search_lib.jump_search("unsorted_numbers", 5)
        self.assertEqual(result, "Found 5 at index 4 in list 'unsorted_numbers'.")

    def test_jump_search_not_found(self):
        result = self.search_lib.jump_search("unsorted_numbers", 10)
        self.assertEqual(result, "10 not found in list 'unsorted_numbers'.")

    def test_fibonacci_search_found(self):
        result = self.search_lib.fibonacci_search("sorted_numbers", 5)
        self.assertEqual(result, "Found 5 at index 4 in list 'sorted_numbers'.")

    def test_fibonacci_search_not_found(self):
        result = self.search_lib.fibonacci_search("sorted_numbers", 10)
        self.assertEqual(result, "10 not found in list 'sorted_numbers'.")

    # Test Sorting Algorithms
    def test_bubble_sort(self):
        result = self.search_lib.bubble_sort("unsorted_numbers")
        self.assertEqual(result, "Bubble Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_selection_sort(self):
        result = self.search_lib.selection_sort("unsorted_numbers")
        self.assertEqual(result, "Selection Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_insertion_sort(self):
        result = self.search_lib.insertion_sort("unsorted_numbers")
        self.assertEqual(result, "Insertion Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_merge_sort(self):
        result = self.search_lib.merge_sort("unsorted_numbers")
        self.assertEqual(result, "Merge Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_quick_sort(self):
        result = self.search_lib.quick_sort("unsorted_numbers")
        self.assertEqual(result, "Quick Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_heap_sort(self):
        result = self.search_lib.heap_sort("unsorted_numbers")
        self.assertEqual(result, "Heap Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    def test_radix_sort(self):
        result = self.search_lib.radix_sort("unsorted_numbers")
        self.assertEqual(result, "Radix Sort result for 'unsorted_numbers': [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]")

    # Test Edge Cases and Error Handling
    # def test_add_graph_invalid_type(self):
    #     with self.assertRaises(ValueError):
    #         self.search_lib.add_graph("invalid_graph", [("A", "B"), ("B", "C")])

    # def test_linear_search_invalid_type(self):
    #     with self.assertRaises(ValueError):
    #         self.search_lib.linear_search("empty_list", 5)

    # def test_binary_search_invalid_type(self):
    #     with self.assertRaises(ValueError):
    #         self.search_lib.binary_search("empty_list", 5)

    def test_empty_list_linear_search(self):
        result = self.search_lib.linear_search("empty_list", 5)
        self.assertEqual(result, "5 not found in list 'empty_list'.")

    def test_empty_list_binary_search(self):
        result = self.search_lib.binary_search("empty_list", 5)
        self.assertEqual(result, "5 not found in list 'empty_list'.")

    def test_empty_list_interpolation_search(self):
        result = self.search_lib.interpolation_search("empty_list", 5)
        self.assertEqual(result, "5 not found in list 'empty_list'.")

    def test_empty_list_jump_search(self):
        result = self.search_lib.jump_search("empty_list", 5)
        self.assertEqual(result, "5 not found in list 'empty_list'.")

    def test_empty_list_fibonacci_search(self):
        result = self.search_lib.fibonacci_search("empty_list", 5)
        self.assertEqual(result, "5 not found in list 'empty_list'.")

    def test_empty_list_sort(self):
        result = self.search_lib.bubble_sort("empty_list")
        self.assertEqual(result, "Bubble Sort result for 'empty_list': []")

    def test_empty_list_sort_error(self):
        result = self.search_lib.merge_sort("empty_list")
        self.assertEqual(result, "Merge Sort result for 'empty_list': []")


if __name__ == "__main__":
    unittest.main()