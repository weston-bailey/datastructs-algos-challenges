# def reverse_string(s):
#   s_len = len(s)
#   for i in range(s_len // 2):
#     s[i], s[s_len - 1 - i ] = s[s_len - 1 - i], s[i]


#   return s
def reverse_string(s):
  if len(s) == 0: return []

  return reverse_string(s[1:]) + [s[0]]
  # code golf 
  # return [] if len(s) == 0 else reverse_string(s[1:]) + [s[0]]




s = ["h","e","l","l","o"]

print(reverse_string(s))

s = ["H","a","n","n","a","h"]

print(reverse_string(s))
