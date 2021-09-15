class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)/2
            if high - low == 1:
                if nums[high] > nums[low]:
                    return high
                else:
                    return low
            if mid+1 < len(nums) and mid-1 >= 0 and nums[mid] > nums[mid+1] and nums[mid] > nums[mid-1]:
                return mid
            elif mid+1 < len(nums) and nums[mid] < nums[mid+1]:
                low = mid+1
            elif mid-1 >= 0 and nums[mid] < nums[mid-1]:
                high = mid-1
        return (low + high)/2
