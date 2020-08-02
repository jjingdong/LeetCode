'''
65. Valid Number
Hard

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements
up front before implementing one. However, here is a list of characters that can be in a valid decimal
number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.
'''


class Solution:

    # Time O(1) Space O(1), runtime = 28 ms
    def isNumber(self, s: str) -> bool:
        # 1       "0" =>          [0]
        #         " 0.1 " =>      [0-9]+\.[0-9]
        #         "2e10" =>       [0-9]+e?[0-9]+
        #         " -90e3   " =>  -?[0-9]+e?[0-9]+
        #         " 6e-1" =>      -?[0-9]+e-[0-9]+
        #         "53.5e93" =>    [0-9]+\.[0-9]e?[0-9]+
        #
        # ans1:     '\s*([+-]?[0-9]+(e[+-]?[0-9]+)?|[+-]?(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*))(e[+-]?[0-9]+)?)\s*'
        # ans2:     '\s*([+-]?(([0-9]+)|([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*))(e[+-]?[0-9]+)?)\s*'
        # ans3:     '\s*([+-]?((\d+)|(\d*\.\d+)|(\d+\.\d*))(e[+-]?\d+)?)\s*'
        # ans4:     '\s*([+-]?((\d*\.\d+)|(\d+\.?\d*))(e[+-]?\d+)?)\s*'

        pattern = '\s*([+-]?((\d*\.\d+)|(\d+\.?\d*))(e[+-]?\d+)?)\s*'

        return re.fullmatch(pattern, s)