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


'''
DFA solution from Steven:

var isNumber = function(s) {
    const dfa = [false,
                 {blank:  1, sign: 2, decimal: 3, number: 4, e: 0}, // 1.blank
                 {blank:  0, sign: 0, decimal: 3, number: 4, e: 0}, // 2.sign
                 {blank:  0, sign: 0, decimal: 0, number: 6, e: 0}, // 3.decimal
                 {blank: 10, sign: 0, decimal: 5, number: 4, e: 7}, // 4.number
                 {blank: 10, sign: 0, decimal: 0, number: 6, e: 7}, // 5.decimal
                 {blank: 10, sign: 0, decimal: 0, number: 6, e: 7}, // 6.number
                 {blank:  0, sign: 8, decimal: 0, number: 9, e: 0}, // 7.e
                 {blank:  0, sign: 0, decimal: 0, number: 9, e: 0}, // 8.sign
                 {blank: 10, sign: 0, decimal: 0, number: 9, e: 0}, // 9.number
                 {blank: 10, sign: 0, decimal: 0, number: 0, e: 0}] // 10.blank
    let curr = 1;
    for (let i = 0; i < s.length; i++) {
        if (!curr) return false;
        let key
        const char = s[i];
        if ('+-'.includes(char)){
            key = 'sign';
        } else if ('0123456789'.includes(char)) {
            key = 'number';
        } else if (char === 'e') {
            key = 'e';
        } else if (char === '.') {
            key = 'decimal'
        } else if (char === ' ') {
            key = 'blank'
        } else {
            return false;
        }
        curr = dfa[curr][key];
    }
    return [10,9,6,5,4].includes(curr)
};

'''