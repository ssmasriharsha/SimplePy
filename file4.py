class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        ls1, ls2 = len(nums1), len(nums2)
        if ls1 < ls2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, ls2 * 2
        while l <= r:
            mid2 = (l + r) >> 1
            R1 = sys.maxint if mid1 == 2 * ls1 else nums1[mid1 >> 1]
            R2 = sys.maxint if mid2 == 2 * ls2 else nums2[mid2 >> 1]
            if L1 > R2:
                l = mid2 + 1
            elif L2 > R1:
                r = mid2 - 1
            else:
                return (max(L1, L2) + min(R1, R2)) / 2.0
            int min = nums[0], max = nums[0], n = nums.length;
        for (int x : nums) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        if (min == max) return 0; // All elements are the same
        int bucketSize = (int) Math.ceil((double) (max - min) / (n - 1));
        int[] minBucket = new int[n];
        int[] maxBucket = new int[n];
        Arrays.fill(minBucket, Integer.MAX_VALUE);
        Arrays.fill(maxBucket, Integer.MIN_VALUE);
        for (int x : nums) {
            int idx = (x - min) / bucketSize;
            minBucket[idx] = Math.min(x, minBucket[idx]);
            maxBucket[idx] = Math.max(x, maxBucket[idx]);


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.findMedianSortedArrays([1, 1], [1, 2])
