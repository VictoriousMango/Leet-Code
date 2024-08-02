class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new_index, index1, index2 = 0, 0, 0
        new_list = list()
        while (index1 < len(nums1)) and (index2 < len(nums2)) :
            if new_index > (len(nums1) + len(nums2))//2:
                break 
            if nums1[index1] < nums2[index2]:
                new_list.append(nums1[index1])
                new_index, index1 = new_index+1, index1+1
            else:
                new_list.append(nums2[index2])
                new_index, index2 = new_index+1, index2+1
        while (index1 < len(nums1)):
            if new_index > (len(nums1) + len(nums2))//2:
                break 
            new_list.append(nums1[index1])
            new_index, index1 = new_index+1, index1+1
        while (index2 < len(nums2)):
            if new_index > (len(nums1) + len(nums2))//2:
                break 
            new_list.append(nums2[index2])
            new_index, index2 = new_index+1, index2+1
        print(new_list)

        return new_list[-1] if (len(nums1) + len(nums2))%2==1 else (new_list[-1] + new_list[-2])/2
        