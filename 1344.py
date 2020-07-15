'''
1344. Angle Between Hands of a Clock
Medium

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
 
Example 1:

Input: hour = 12, minutes = 30
Output: 165
Example 2:

Input: hour = 3, minutes = 30
Output: 75
Example 3:

Input: hour = 3, minutes = 15
Output: 7.5
Example 4:
Input: hour = 4, minutes = 50
Output: 155
Example 5:
Input: hour = 12, minutes = 0
Output: 0
 
Constraints:
	•	1 <= hour <= 12
	•	0 <= minutes <= 59
	•	Answers within 10^-5 of the actual value will be accepted as correct.
'''


class Solution:

    #         min:    0   15  30  45  60
    #         angle:  0       180     360
    #
    #         hour:   0   3   6   9   12
    #         angle:  0       180     360
    #         hour:   0:00    0:15    0:30    0:45    1:00
    #         angle:  0               360/12/2       360/12

    # Time O(1) Space O(1), runtime = 24 ms
    def angleClock(self, hour: int, minutes: int) -> float:
        min_angle = minutes / 60
        hour_angle = (hour % 12) / 12 + min_angle / 12
        diff = abs(min_angle - hour_angle)

        return min(diff, 1 - diff) * 360


'''  
    # Time O(1) Space O1(), runtime = 24 ms
    def angleClock(self, hour: int, minutes: int) -> float:


        min_angle = 360//60*minutes
        hour_angle = 360//12 * (hour%12) + 360//12 * (minutes/60)

        diff = abs(min_angle - hour_angle)

        if diff > 180: return 360 - diff
        return diff
'''
