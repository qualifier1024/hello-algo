'''
File: quick_sort.py
Created Time: 2022-11-25
Author: timi (xisunyy@163.com)
'''

import sys, os.path as osp
sys.path.append(osp.dirname(osp.dirname(osp.abspath(__file__))))
from include import *

""" 快速排序类 """
class QuickSort:
    """ 哨兵划分 """
    def partition(self, nums, left, right):
        # 以 nums[left] 作为基准数
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # 从右向左找首个小于基准数的元素
            while i < j and nums[i] <= nums[left]:
                i += 1  # 从左向右找首个大于基准数的元素
            # 元素交换
            nums[i], nums[j] = nums[j], nums[i]
        # 将基准数交换至两子数组的分界线
        nums[i], nums[left] = nums[left], nums[i]
        return i  # 返回基准数的索引

    """ 快速排序 """
    def quick_sort(self, nums, left, right):
        # 子数组长度为 1 时终止递归
        if left >= right:
            return
        # 哨兵划分
        pivot = self.partition(nums, left, right)
        # 递归左子数组、右子数组
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)

""" 快速排序类（中位基准数优化）"""
class QuickSortMedian:
    """ 选取三个元素的中位数 """
    def median_three(self, nums, left, mid, right):
        # 使用了异或操作来简化代码
        # 异或规则为 0 ^ 0 = 1 ^ 1 = 0, 0 ^ 1 = 1 ^ 0 = 1
        if (nums[left] > nums[mid]) ^ (nums[left] > nums[right]):
            return left
        elif (nums[mid] < nums[left]) ^ (nums[mid] > nums[right]):
            return mid
        return right

    """ 哨兵划分（三数取中值） """
    def partition(self, nums, left, right):
        # 以 nums[left] 作为基准数
        med = self.median_three(nums, left, (left + right) // 2, right)
        # 将中位数交换至数组最左端
        nums[left], nums[med] = nums[med], nums[left]
        # 以 nums[left] 作为基准数
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # 从右向左找首个小于基准数的元素
            while i < j and nums[i] <= nums[left]:
                i += 1  # 从左向右找首个大于基准数的元素
            # 元素交换
            nums[i], nums[j] = nums[j], nums[i]
        # 将基准数交换至两子数组的分界线
        nums[i], nums[left] = nums[left], nums[i]
        return i  # 返回基准数的索引

    """ 快速排序 """
    def quick_sort(self, nums, left, right):
        # 子数组长度为 1 时终止递归
        if left >= right: return
        # 哨兵划分
        pivot = self.partition(nums, left, right)
        # 递归左子数组、右子数组
        self.quick_sort(nums, left, pivot - 1)
        self.quick_sort(nums, pivot + 1, right)

""" 快速排序类（尾递归优化） """
class QuickSortTailCall:
    """ 哨兵划分 """
    def partition(self, nums, left, right):
        # 以 nums[left] 作为基准数
        i, j = left, right
        while i < j:
            while i < j and nums[j] >= nums[left]:
                j -= 1  # 从右向左找首个小于基准数的元素
            while i < j and nums[i] <= nums[left]:
                i += 1  # 从左向右找首个大于基准数的元素
            # 元素交换
            nums[i], nums[j] = nums[j], nums[i]
        # 将基准数交换至两子数组的分界线
        nums[i], nums[left] = nums[left], nums[i]
        return i   # 返回基准数的索引

    """ 快速排序（尾递归优化） """
    def quick_sort(self, nums, left, right):
        # 子数组长度为 1 时终止
        while left < right:
            # 哨兵划分操作
            pivot = self.partition(nums, left, right)
            # 对两个子数组中较短的那个执行快排
            if pivot - left < right - pivot:
                self.quick_sort(nums, left, pivot - 1)  # 递归排序左子数组
                left = pivot + 1     # 剩余待排序区间为 [pivot + 1, right]
            else:
                self.quick_sort(nums, pivot + 1, right)  # 递归排序右子数组
                right = pivot - 1    # 剩余待排序区间为 [left, pivot - 1]


""" Driver Code """
if __name__ == '__main__':
    # 快速排序 
    nums = [4, 1, 3, 1, 5, 2]
    QuickSort().quick_sort(nums, 0, len(nums) - 1)
    print("快速排序完成后 nums =", nums)

    # 快速排序（中位基准数优化）
    nums1 = [4, 1, 3, 1, 5, 2]
    QuickSortMedian().quick_sort(nums1, 0, len(nums1) - 1)
    print("快速排序（中位基准数优化）完成后 nums =", nums)

    # 快速排序（尾递归优化）
    nums2 = [4, 1, 3, 1, 5, 2]
    QuickSortTailCall().quick_sort(nums, 0, len(nums2) - 1)
    print("快速排序（尾递归优化）完成后 nums =", nums)
