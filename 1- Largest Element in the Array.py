'''

Find the Largest element in an array



Brute Force Approach
Algorithm / Intuition
Solution1: Sorting
Intuition:
We can sort the array in ascending order, hence the largest element will be at the last index of the array. 

Approach: 
Sort the array in ascending order.
Print the (size of the array -1)th index.
DryRun: 
Before sorting: arr[] = {2,5,1,3,0};

After sorting: arr[] = {0,1,2,3,5};

Hence answer : arr[sizeofthearray-1] =5

'''


from typing import List
def sortArr(arr: List[int]) -> int:
    arr.sort()
    return arr[-1]
if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    arr2 = [8, 10, 5, 7, 9]
    print("The Largest element in the array is:", sortArr(arr1))
    print("The Largest element in the array is:", sortArr(arr2))


'''


Solution2: Using a max variable

Intuition:
We can maintain a max variable that will update whenever the current value is greater than the value in the max variable.  

Approach: 
Create a max variable and initialize it with arr[0].
Use a for loop and compare it with other elements of the array
If any element is greater than the max value, update max value with the element’s value
Print the max variable.


'''
def findLargestElement(arr, n):


    max = arr[0]
    for i in range(0, n):
        if (max < arr[i]):
            max = arr[i]
    return max




if __name__ == "__main__":
    arr1 = [2, 5, 1, 3, 0]
    n = 5
    max = findLargestElement(arr1, n)
    print("The largest element in the array is:", max)


    arr2 = [8, 10, 5, 7, 9]
    n = 5
    max = findLargestElement(arr2, n)
    print("The largest element in the array is:", max)