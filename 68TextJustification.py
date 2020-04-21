'''
68. Text Justification
Hard

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left justified and no extra space is inserted between words.
Note:
	•	A word is defined as a character sequence consisting of non-space characters only.
	•	Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
	•	The input array words contains at least one word.
Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''


class Solution:

    # This is an example of text justification.
    # 4    2  2  7       2  4    15
    # maxLen = 16
    #
    # This is an -----> 16-4-2-2 = 8,   value,rest = divmod(8,2) = 4, 0
    # example of text -----> 16 - 7 - 2 - 4 = 3,   value, rest = divmod(3,2) = 1,1
    #                        add extra space first, then add value space
    # justification.  ----> if this is the last line or this is only one word, then add extra spaces at the end
    # Solutio is done, code is not done

    # Time O() Space O()
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
