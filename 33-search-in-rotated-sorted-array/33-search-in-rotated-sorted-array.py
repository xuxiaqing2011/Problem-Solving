class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid
                else:
                    l = mid + 1
        return -1
        
        