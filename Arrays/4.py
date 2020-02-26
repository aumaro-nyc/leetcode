class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        count = 0
        result = []
        length = len(nums1) + len(nums2)
        target = length // 2
        i,j = 0,0

        while i < len(nums1) and j < len(nums2):
            count += 1
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
            if count == target + 1:
                if length % 2 != 0:
                    return result.pop()
                else:
                    return (result.pop() + result.pop()) / 2

        while i < len(nums1):
            count += 1
            result.append(nums1[i])
            i += 1
            if count == target + 1:
                if length % 2 != 0:
                    return result.pop()
                else:
                    return (result.pop() + result.pop()) / 2
        while j < len(nums2):
            count += 1
            result.append(nums2[j])
            j += 1
            if count == target + 1:
                if length % 2 != 0:
                    return result.pop()
                else:
                    return (result.pop() + result.pop()) / 2
