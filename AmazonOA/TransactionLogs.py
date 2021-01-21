'''
A Company parses logs of online store user transactions/activity to flag fraudulent activity.

The log file is represented as an Array of arrays. The arrays consist of the following data:

[ <# of transactions>]

For example:

[345366 89921 45]

Note: the data is space delimited

So, the log data would look like:

[
[345366 89921 45],
[029323 38239 23]
...
]
Write a function to parse the log data to find distinct users that meet or cross a certain
threshold.

The function will take in 2 inputs:
logData: Log data in form an array of arrays

threshold: threshold as an integer

Output:
It should be an array of userids that are sorted.

If same userid appears in the transaction as userid1 and userid2, it should count as one
occurrence, not two.

Example:
Input:
logData:

[
[345366 89921 45],
[029323 38239 23],
[38239 345366 15],
[029323 38239 77],
[345366 38239 23],
[029323 345366 13],
[38239 38239 23]
...
]
threshold: 3

Output: [345366 , 38239, 029323]
Explanation:
Given the following counts of userids, there are only 3 userids that meet or exceed the threshold of 3.

345366 -4 , 38239 -5, 029323-3, 89921-1

'''


# Diagram:
# [345366     89921       45]
#   |           |          |
# sender_id  receiver_id  log
#
# id      occurance
# 345366  4
# 89921   1
# 029323  3
# 38239   5

import collections

''' Solution I ---------------------------------- '''
def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    # Time O(3M) = O(M), M = no. of lines
    for [log] in logData:
        [s_id, r_id, log_id] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []

    # Time O(NlogN), N = no. of user_ids
    for k, v in sorted(log_dict.items(), key=lambda item: item[1], reverse=True):
        if v >= threshold:
            results.append(k)

    return results

''' Solution II ---------------------------------- '''
def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    # Time O(3M) = O(M), M = no. of lines
    for [log] in logData:
        [s_id, r_id, log_id] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []

    # Time O(N)
    d_dict = {}
    for k, v in log_dict.items():
        if v >= threshold:
            d_dict[k] = v

    # Time O(KlogK), K is no. of items, which count is bigger than and equals to threshold
    a = sorted(d_dict.items(), key=lambda x: x[1], reverse=True)
    return [x[0] for x in a]


''' Solution III ---------------------------------- '''
def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    # Time O(3M) = O(M), M = no. of lines
    for [log] in logData:
        [s_id, r_id, log_id] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    # print(log_dict)
    results = []

    # Time O(N)
    a_set = set()
    for k, v in log_dict.items():
        if v >= threshold:
            a_set.add((k, v))

    # Time O(KlogK), K is no. of items, which count is bigger than and equals to threshold
    a_set = sorted(a_set, key=lambda x: x[1], reverse=True)
    return [x[0] for x in a_set]


''' Solution IV ---------------------------------- '''
def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []
    # Time O(NlogN), N = no. of user_ids
    for k in sorted(log_dict, key=log_dict.get, reverse=True):
        if log_dict[k] >= threshold:
            results.append(k)

    return results


''' Solution V ---------------------------------- '''
def get_userids(logData, threshold):
    log_dict = collections.Counter()
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []
    # Time O(NlogN), N = no. of user_ids
    for k, v in log_dict.most_common():
        if v >= threshold:
            results.append(k)

    return results


''' Solution VI ---------------------------------- '''
import heapq
def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []
    a = []
    # Time O(N), N = no. of user_ids
    for k, v in log_dict.items():
        if v >= threshold:
            heapq.heappush(a, (-v, k))

    # use maxheap, and swap (k,v) to (-v,k)
    # Time O(KlogK), K = no. of items, which count is bigger than and equals to threshold
    while a:
        top = heapq.heappop(a)
        results.append(top[1])

    return results


''' Solution V ---------------------------------- '''
def get_userids(logData, threshold):
    def quicksort(input):
        def divide(start, finish):
            if (start >= finish):
                return

            mid = start
            pivot = finish
            for i in range(start, finish):
                if input[i][1] >= input[pivot][1]:
                    input[i], input[mid] = input[mid], input[i]
                    mid += 1

            input[mid], input[pivot] = input[pivot], input[mid]
            divide(start, mid - 1)
            divide(mid + 1, finish)

        divide(0, len(input) - 1)
        return input

    log_dict = collections.defaultdict(int)
    # Time O(3M) = O(M), M = no. of lines
    for [log] in logData:
        [s_id, r_id, log_id] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    results = []

    # Time O(N)
    a_list = []
    for k, v in log_dict.items():
        if v >= threshold:
            a_list.append((k, v))

    # Average Time O(Klog(K)) Worse Time O(K^2)
    a_list = quicksort(a_list)
    return [x[0] for x in a_list]




'''
Note. collections.Counter() is same as collections.defaultdict()
      but they have different functions
'''


'''
Testing
'''

logData = [
    ['345366 89921 45'],
    ['029323 38239 23'],
    ['38239 345366 15'],
    ['029323 38239 77'],
    ['345366 38239 23'],
    ['029323 345366 13'],
    ['38239 38239 23']
]
threshold = 3
results = get_userids(logData, threshold)
print(results)
expected_results = ['38239', '345366', '029323']
print(expected_results == results)
