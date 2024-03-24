def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the mid of the array
        left_half = arr[:mid]  # Dividing the array elements
        right_half = arr[mid:]  # into 2 halves

        # Print the current sub-arrays
        print("Dividing:", arr)
        print("Left half:", left_half)
        print("Right half:", right_half)
        print()

        merge_sort(left_half)  # Sorting the first half
        merge_sort(right_half)  # Sorting the second half

        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Print the merged array at each step
        print("Merging:", arr)
        print()

# Taking input from the user for array elements
arr = list(map(int, input("Enter the array of numbers separated by space: ").split()))

# Calling merge_sort function to sort the input array
merge_sort(arr)

# Printing the final sorted array
print("Sorted array is:", arr)


