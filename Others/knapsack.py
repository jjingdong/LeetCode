'''
220 = 100 + 120
       |      |
       20     30


10 weight, 5 times = 50kg
60*5 = 300 = value

Knapsack
pick each item once, quantity = 1

dp table bottom up
                 -------------- kg column --------------------
                0kg ...  10kg ...  20kg .... 30kg ...  40kg ...  50kg limit
weight value
10kg     $60     $0      $60       $60       $60       $60       $60

20kg     $100    $0      $60       $100      $160      $160      $160
                 --      ---       ----
                                   dp[i][j] = dp[r][c] = $60 or $100
                                   20kg >= weight[i] = 20kg

                                   $160 = $60 or         $100 + $60
                                          ----
                                          dp[r-1][c]     value[r] + dp[r-1][c-weight[r]]
                                                                            c = 30kg, weight[r] = 20kg

w=30kg  v=$120
=weight[r]
values[r]
r = 2
              $0       $60        $100      $160        ?????=$180   *******=$220
                                          option1 = $160      ==> dp[r-1][c], r = 2, c = 30
                                          option2 = $120 + $0 ==> value[r] + dp[r-1][c-w], c = 30, w = 30


                                          ????
                                          option1 = $160 ==> dp[r-1][c], r = 2, c = 40kg
                                          option2 = $120 + $60    ==> value[r] + dp[r-1][c-w], c = 40, w = 30
                                                     30kg  ----       -------
                                                          10kg



                                          *****
                                          option1 = $160    not take myself
                                          option2 = $120 + $100   ==> value[r] + dp[r-1][c-w], c = 50, w = 30
                                                    ----    ----      --------
                                                    30kg   $20kg     value for 30kg = $120

                                                                   |
                                                                   ans = $220
cell = value, maximum value so far


                            30kg
                            /                    \
                       $60   10kg            $60, 10kg,   $100, 20kg



                            0kg, rest = 50kg
                            / \
                        10kg,rest k= 40kg    not take 10kg
                    $60
                    /                      \
                20kg, rest, 20kg         not take 20kg

             helper():
                helper()
                helper()


  greedy
  item       ->          value/weight

'''
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50


# Time O(MN) Space O(MN)
def knacksack(values, weights, capacity):
    col_size = capacity + 1
    size = len(weights)
    dp = [[0 for _ in range(col_size)] for _ in range(size)]

    for r in range(size):
        for c in range(col_size):
            w = weights[r]
            if c >= w:
                dp[r][c] = max(dp[r - 1][c], values[r] + dp[r - 1][c - w])
            else:
                dp[r][c] = dp[r - 1][c]

    # for r in range(size):
    #     print(dp[r])
    return dp[-1][-1]


ans = knacksack(values, weights, capacity)
print(ans)
output = 220



