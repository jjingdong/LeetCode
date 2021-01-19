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

import collections


def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    print(log_dict)
    results = []
    for k, v in sorted(log_dict.items(), key=lambda item: item[1], reverse=True):
        if v >= threshold:
            results.append(k)

    return results


def get_userids(logData, threshold):
    log_dict = collections.defaultdict(int)
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    print(log_dict)
    results = []
    for k in sorted(log_dict, key=log_dict.get, reverse=True):
        if log_dict[k] >= threshold:
            results.append(k)

    return results


def get_userids(logData, threshold):
    log_dict = collections.Counter()
    for [log] in logData:
        [s_id, r_id, log] = log.split()

        log_dict[s_id] += 1
        if s_id != r_id:
            log_dict[r_id] += 1

    print(log_dict)
    results = []
    for k, v in log_dict.most_common():
        if v >= threshold:
            results.append(k)

    return results


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
