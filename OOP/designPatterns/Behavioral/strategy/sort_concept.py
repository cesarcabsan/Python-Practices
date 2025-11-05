# Let’s consider a sorting application where we need to sort a list of integers. 
# However, the sorting algorithm to be used may vary depending on factors such as the size of the list and the desired performance characteristics. 

from abc import ABC, abstractmethod

# Interface
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, array):
        pass

# Concrete strategies
class BubbleSortStrategy(SortingStrategy):
    def sort(self, array):
        # Implement the Bubble Sort algorithm here
        print("Sorting with bubble sort") 
        # Actual Bubble Sort Logic here

class MergeSortStrategy(SortingStrategy):
    def sort(self, array):
        # Implement the Merge Sort algorithm here
        print("Sorting with merge sort") 
        # Actual Merge Sort Logic here

class QuickSortStrategy(SortingStrategy):
    def sort(self, array):
        # Implement the Quick Sort algorithm here
        print("Sorting with quick sort") 
        # Actual Quick Sort Logic here


# Sorting Context class
class SortingContext:
    def __init__(self, sorting_strategy: SortingStrategy):
        self.sorting_strategy = sorting_strategy
    
    def set_sorting_strategy(self, sorting_strategy: SortingStrategy):
        self.sorting_strategy = sorting_strategy

    def perform_sort(self, array):
        self.sorting_strategy.sort(array)


# Usage

# Create SortingContext with BubbleSortStrategy
sorting_context = SortingContext(BubbleSortStrategy())
array1 = [5, 2, 9, 1, 5]
sorting_context.perform_sort(array1)

# Change strategy with the other sorting algorithms
sorting_context.set_sorting_strategy(MergeSortStrategy())
array2 = [8, 3, 7, 4, 2]
sorting_context.perform_sort(array2)

sorting_context.set_sorting_strategy(QuickSortStrategy())
array3 = [6, 1, 3, 9, 5]
sorting_context.perform_sort(array3)