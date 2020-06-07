'''
528. Random Pick with Weight
Medium

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.
Note:
	1.	1 <= w.length <= 10000
	2.	1 <= w[i] <= 10^5
	3.	pickIndex will be called at most 10000 times.
Example 1:
Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any.

'''


class Solution:

    # ["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
    # [[[1,3,5,7]],[],[],[],[],[]]
    # w = [1,3,5,7]
    # accumulated_sum = [1,4,9,16]
    # random_num = 1,2,3,4,5,...,17
    # random in [1,2,3] --> return 0
    # random in [4,5,6,7,8] --> return 1
    # random in [9,10,11,12,13,14,15,16] --> return 3

    # Time O(N) Space O(N), runtime = 180 ms
    def __init__(self, w: List[int]):
        self.acc_sum = list(itertools.accumulate(w))

    # Time O(logN) Space O(1)
    def pickIndex(self) -> int:
        ran_num = random.random() * self.acc_sum[-1]
        return bisect.bisect_left(self.acc_sum, ran_num)


'''
    # Time O(N) Space O(N), Time Limit Exceeded
    def __init__(self, w: List[int]):

        self.acc_sum = []
        count = 0
        for num in w:
            count += num
            self.acc_sum.append(count)

    # Time O(N) Space O(1)
    def pickIndex(self) -> int:

        ran_num = random.random() * self.acc_sum[-1]
        for i in range(len(self.acc_sum)):
            if ran_num < self.acc_sum[i]:
                return i
        return None
'''

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()