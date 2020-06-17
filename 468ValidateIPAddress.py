'''
468. Validate IP Address
Medium

Write a function to check whether an input string is a valid IPv4 address or IPv6 address or neither.
IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, each ranging from 0 to 255, separated by dots ("."), e.g.,172.16.254.1;
Besides, leading zeros in the IPv4 is invalid. For example, the address 172.16.254.01 is invalid.
IPv6 addresses are represented as eight groups of four hexadecimal digits, each group representing 16 bits. The groups are separated by colons (":"). For example, the address 2001:0db8:85a3:0000:0000:8a2e:0370:7334 is a valid one. Also, we could omit some leading zeros among four hexadecimal digits and some low-case characters in the address to upper-case ones, so 2001:db8:85a3:0:0:8A2E:0370:7334 is also a valid IPv6 address(Omit leading zeros and using upper cases).
However, we don't replace a consecutive group of zero value with a single empty group using two consecutive colons (::) to pursue simplicity. For example, 2001:0db8:85a3::8A2E:0370:7334 is an invalid IPv6 address.
Besides, extra leading zeros in the IPv6 is also invalid. For example, the address 02001:0db8:85a3:0000:0000:8a2e:0370:7334 is invalid.
Note: You may assume there is no extra space or special characters in the input string.
Example 1: 
Input: "172.16.254.1"

Output: "IPv4"

Explanation: This is a valid IPv4 address, return "IPv4".

Example 2: 
Input: "2001:0db8:85a3:0:0:8A2E:0370:7334"

Output: "IPv6"

Explanation: This is a valid IPv6 address, return "IPv6".

Example 3: 
Input: "256.256.256.256"

Output: "Neither"

Explanation: This is neither a IPv4 address nor a IPv6 address.
'''


class Solution:

    #         IPv4: a.b.c.d
    #             a, b, c, d = decimal 0 ~ 255
    #             no leading zero
    #
    #         IPv6: a
    #             a:b:c:d:e:f:g:h
    #             a, b, c, d, e, f, g, h = hour hexadecimal digits, 16 bits

    # Time O(N) Space O(1), runtime = 28 ms
    def validIPAddress(self, IP: str) -> str:

        def validIPv4(ips):
            for ip in ips:
                if not ip: return False
                if len(ip) > 3: return False
                for i in range(len(ip)):
                    if ip[i] not in '0123456789': return False

                for i in range(len(ip) - 1):
                    if ip[i] == '0':
                        return False
                    else:
                        break

                ip_int = int(ip)
                if ip_int not in range(0, 256): return False

            return True

        def validIPv6(ips):
            largest = int('ffff', 16)
            for ip in ips:
                if not ip: return False
                if len(ip) > 4: return False
                for char in ip:
                    if char not in '0123456789abcdefABCDEF': return False

                ip_int = int(ip, 16)
                if ip_int not in range(0, largest + 1): return False

            return True

        v4, v6, invalid = 'IPv4', 'IPv6', 'Neither'

        splits = IP.split('.')
        if len(splits) == 4 and validIPv4(splits):
            return v4

        splits = IP.split(':')
        if len(splits) == 8 and validIPv6(splits):
            return v6

        else:
            return invalid

