"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Nested brackets, such as [(){}], are valid.
"""


class Solution:
    @staticmethod
    def isValid(s: str) -> bool:  # NOQA

        stack = []
        valid_set = {')': '(', '}': '{', ']': '['}

        for character in s:
            if character in valid_set:  # in closing brackets
                if stack and stack[-1] == valid_set[character]:  # == opening brackets
                    stack.pop()  # popping closing brackets
                else:
                    return False
            else:
                stack.append(character)  # appending closing brackets
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isValid('({[]})()'))

# Time Complexity: O(n)
# Memory Complexity: O(n)
