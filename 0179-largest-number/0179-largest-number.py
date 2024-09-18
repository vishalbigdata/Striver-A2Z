class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        # Convert all integers to strings for easy concatenation
        nums_as_str = [str(num) for num in nums]
      
        # Sort the list of strings, defining a custom comparator
        # that compares concatenated string combinations
        nums_as_str.sort(key=cmp_to_key(self._compare_numbers))
      
        # Special case: if the highest number is "0", the result is "0"
        # (happens when all numbers are zeros)
        if nums_as_str[0] == "0":
            return "0"
      
        # Join the numbers to form the largest number
        return "".join(nums_as_str)

    def _compare_numbers(self, a: str, b: str) -> int:
        # Custom comparator for sorting:
        # If the concatenation of a before b is less than b before a,
        # then we say a is "greater than" b in terms of the custom sorting.
        # That is, return -1 to indicate a should come before b.
        if a + b < b + a:
            return 1
        else:
            return -1