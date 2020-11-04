# !/usr/bin/python3
# _*_ coding:utf-8 _*_
# https://leetcode-cn.com/problems/zai-pai-xu-shu-zu-zhong-cha-zhao-shu-zi-lcof/
from collections import Counter


class Solution:
    def search(self, nums, target) -> int:
        return nums.count(target)

    def search_01(self, nums, target):
        dic = Counter(nums)
        return dic.get(target, 0)

    def search_02(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] <= target:
                i = m + 1
            else:
                j = m - 1

        right = i
        if j >= 0 and nums[j] != target:
            return  0

        i = 0
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        left = j

        return right - left - 1

    def search_03(self, nums, target) -> int:

        def helper(tar):
            i, j = 0, len(nums) - 1
            while i <= j:
                m = (i + j) // 2
                if nums[m] <= tar:
                    i = m + 1
                else:
                    j = m - 1
            return i

        return helper(target) - helper(target - 1)

if __name__ == "__main__":
    test = Solution()
    inp = [5,7,7,8,8,10]
    # out = test.search(inp, 8)
    # out = test.search_01(inp, 8)
    # out = test.search_02(inp, 8)
    out = test.search_03(inp, 8)
    print(out)
