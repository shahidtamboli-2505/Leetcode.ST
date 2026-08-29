class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        # Binary search smaller array par
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)

        left = 0
        right = m

        while left <= right:

            # nums1 ka partition
            i = (left + right) // 2

            # nums2 ka partition
            j = (m + n + 1) // 2 - i

            # Boundary values
            Aleft = float('-inf') if i == 0 else nums1[i - 1]
            Aright = float('inf') if i == m else nums1[i]

            Bleft = float('-inf') if j == 0 else nums2[j - 1]
            Bright = float('inf') if j == n else nums2[j]

            # Correct partition
            if Aleft <= Bright and Bleft <= Aright:

                # Odd total elements
                if (m + n) % 2 == 1:
                    return max(Aleft, Bleft)

                # Even total elements
                return (max(Aleft, Bleft) +
                        min(Aright, Bright)) / 2

            # nums1 ka partition right side le jao
            elif Aleft > Bright:
                right = i - 1

            # nums1 ka partition left side le jao
            else:
                left = i + 1