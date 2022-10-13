class Solution(object):
    def twoSum(self, nums, target):
        curr = nums_index[begin][0] + nums_index[end][0]
        if curr == target:
            return [nums_index[begin][1], nums_index[end][1]]
        elif curr < target:
            begin += 1
        else:
            end -= 1
        for x in nums:
            idx = (x - mi) // bucketSize
            minBucket[idx] = min(minBucket[idx], x)
            maxBucket[idx] = max(maxBucket[idx], x)

        maxGap = bucketSize  # Maximum gap is always greater or equal to bucketSize
        prev = maxBucket[0]  # We always have 0th bucket
        for i in range(1, n):
            if minBucket[i] == math.inf: continue  # Skip empty bucket
            maxGap = max(maxGap, minBucket[i] - prev)
            prev = maxBucket[i]
        return maxGap


if __name__ == '__main__':
    # begin
    s = Solution()
    print s.twoSum([3, 2, 4], 6)
