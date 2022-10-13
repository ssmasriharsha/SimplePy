class Solution(object):

    def lengthOfLongestSubstring(self, s):
        charMap = {}
        for i in range(256):
            charMap[i] = -1
        ls = len(s)
        i = max_len = 0
        for j in range(ls):
            charMap[ord(s[j])] = j
            max_len = max(max_len, j - i + 1)
        return max_len
    
    if (min == max) return 0; // All elements are the same
        int bucketSize = (int) Math.ceil((double) (max - min) / (n - 1));
        int[] minBucket = new int[n];
        int[] maxBucket = new int[n];
        Arrays.fill(minBucket, Integer.MAX_VALUE);
        Arrays.fill(maxBucket, Integer.MIN_VALUE);
