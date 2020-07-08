'''
957. Prison Cells After N Days
Medium

There are 8 prison cells in a row, and each cell is either occupied or vacant.
Each day, whether the cell is occupied or vacant changes according to the following rules:
	•	If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
	•	Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)
We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.
Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
 
	1.
Example 1:
Input: cells = [0,1,0,1,1,0,0,1], N = 7
Output: [0,0,1,1,0,0,0,0]
Explanation:
The following table summarizes the state of the prison on each day:
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

Example 2:
Input: cells = [1,0,0,1,0,0,1,0], N = 1000000000
Output: [0,0,1,1,1,1,1,0]
 
Note:
	1.	cells.length == 8
	2.	cells[i] is in {0, 1}
	3.	1 <= N <= 10^9
'''


class Solution:

    # Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
    # Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
    # Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
    # Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
    # Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
    # Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
    # Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
    # Day 7: [0, 0, 1, 1, 0, 0, 0, 0]

    # Time O(min(N, 2^K)) Space O(K* 2^K ), using cache, runtime = 48 ms
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        cache_day = collections.defaultdict(list)
        cache = collections.Counter()
        noDays = 0
        size = len(cells)
        while noDays < N:

            temp = [0] * size
            for i in range(1, size - 1):
                if cells[i - 1] == cells[i + 1]:
                    temp[i] = 1
            cells = temp
            noDays += 1

            if tuple(cells) in cache:
                break
            else:
                cache[tuple(cells)] = noDays
                cache_day[noDays] = cells

        if noDays == N:
            return cells

        start_day = cache[tuple(cells)]
        cycle_len = noDays - start_day
        final_day = (N - start_day) % cycle_len + start_day
        return cache_day[final_day]


'''
    # Time O(min(N, 2^K)) Space O(K* 2^K ), using cache, runtime = 64 ms
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        cache_day = collections.defaultdict(list)
        cache = collections.Counter()
        arr = [0] * len(cells)
        noDays = 0
        for j in range(N):
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    arr[i] = 1
            cells = arr
            noDays += 1

            if tuple(cells) in cache:
                start_day = cache[tuple(cells)]
                cycle_len = noDays - start_day
                final_day = (N-start_day) % cycle_len + start_day
                return cache_day[final_day]

            else:
                cache[tuple(cells)] = noDays
                cache_day[noDays] = cells     

            arr = [0] * len(cells)

        return cells 
'''

'''    
    # Time O(MN) Space O(N), Time Limit Exceeded
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        arr = [0] * len(cells)
        for j in range(N):
            for i in range(len(cells)):
                if i == 0 or i == len(cells) - 1:
                    arr[i] = 0
                elif cells[i-1] == cells[i+1]:
                    arr[i] = 1
                else:
                    arr[i] = 0
            cells = arr
            arr = [0] * len(cells)

        return cells
'''