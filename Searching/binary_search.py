TARGET_NOT_FOUND = -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # requires O(logn) so lets use recursion
        # T(N) = 1 + 2T(n/2)
        if (len(nums) == 0) or \
            (len(nums) == 1 and nums[0] != target):
            return TARGET_NOT_FOUND 
        # halfway point check also works for list with 1 item
        middle_index = len(nums) // 2
        if target == nums[middle_index]:
            return middle_index
        # since our sentinel is negative...
        # any "found" index (>=) would be the result
        return max(
            self.search(nums[0:middle_index], target),
            # attempt 2 - add on the middle_index to the "return" value 
            # so it doesn't lose track of what indexes it just came from
            middle_index + self.search(nums[middle_index:], target)
        )