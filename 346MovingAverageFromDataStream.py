'''
346. Moving Average from Data Stream
Easy

Given a stream of integers and a window size, calculate the moving average of
all integers in the sliding window.

Example:

MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3
'''


class MovingAverage:

    # Solution I: queue
    #
    # Solution II: circular queue

    #         1:
    #             output: 1
    #         10:
    #             output: (1+10)/2
    #         3:
    #             output: (1+10+3)/3  1/3+10/3+3/3
    #         5:
    #             output: (10+3+5)/3
    #
    #             queue definite work
    #             accumulated sum
    #             1   10  3   5
    #             1   11  14  18=14+5-1

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque([])
        self.acc_sum = 0
        self.capacity = size
        self.cur_size = 0

    # Time O(1) Space O(size), runtime = 68 ms
    def next(self, val: int) -> float:
        self.cur_size += 1
        self.queue.append(val)
        self.acc_sum += val
        if self.cur_size > self.capacity:
            self.acc_sum -= self.queue.popleft()
            self.cur_size -= 1

        return self.acc_sum / self.cur_size

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)