class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        short_list = nums1 if len(nums1) <= len(nums2) else nums2
        long_list = nums1 if len(nums1) > len(nums2) else nums2
        result = []
        index_map = {}
        for i in range(len(short_list)):
            if short_list[i] in index_map:
                index_map[short_list[i]].append(i)
            else:
                index_map[short_list[i]] = [i]
        print(index_map)

        for i in range(len(long_list)):
            if long_list[i] in index_map:
                for indx in index_map[long_list[i]]:
                    start_short = indx
                    start_long = i
                    curr = []
                    while (start_long < len(long_list) and start_short < len(short_list)) and long_list[start_long] == short_list[start_short]:
                        curr.append(long_list[start_long])
                        start_long += 1
                        start_short += 1
                    if len(curr) > len(result):
                        result = curr

        return result
