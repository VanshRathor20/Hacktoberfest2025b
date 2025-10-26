class Solution:
    def sortInWave(self, arr):
        # Step 1: Sort the array
        arr.sort()
        
        # Step 2: Swap adjacent elements in pairs
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        return arr
