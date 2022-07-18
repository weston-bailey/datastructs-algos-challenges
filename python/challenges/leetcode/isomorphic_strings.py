'''
https://leetcode.com/problems/isomorphic-strings
205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.



Example 1:

Input: s = "egg", t = "add"
Output: true

Example 2:

Input: s = "foo", t = "bar"
Output: false

Example 3:

Input: s = "paper", t = "title"
Output: true



Constraints:

    1 <= s.length <= 5 * 104
    t.length == s.length
    s and t consist of any valid ascii character.

'''

# # egg
# t_table = {
#     e: [0],
#     g: [1, 2]
# }
# # add
# s_table = {
#     a: [0],
#     d: [1, 2]
# }

# # foo
# f_table = {
#     f: [0],
#     o: [1, 2]
# }
# # bar
# b_table = {
#     b: [0],
#     a: [1],
#     r: [2]
# }

def isIsomorphic(s, t):
    # add each char to table
    # chars in table will be lists of their position in the string
    # s and t table should be same 'shape', but have different keys
    # compare s and t table, if a match is found, remove from s table
    # s table should be empty, if they match
    s_table = __build_table(s)
    t_table = __build_table(t)
    for t_char in t_table:
        for s_char in s_table:
            if s_table[s_char] == t_table[t_char]:
                del s_table[s_char]
                break

    return not bool(s_table)

def __build_table(string):
    table = {}

    for i, char in enumerate(string):
        if char not in table:
            table[char] = [i]
        else:
            table[char].append(i)

    return table

