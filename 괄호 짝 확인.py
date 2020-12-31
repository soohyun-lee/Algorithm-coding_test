from stack import Stack

# def solution(str1):
#     s = Stack()
#     result = True
#     index = 0

#     while index < len(str1) and result:
#         symbol = str1[index]

#         if symbol == "(":
#             s.push(symbol)
#         else:
#             if s.isEmpty():
#                 result = False
#             else:
#                 s.pop()
#         index = index + 1
#     if result and s.isEmpty():
#         return True
#     else:
#         return False
    
# print(solution('(())'))
symbol  = '('
s = Stack()
print(s)
print(s.push(symbol))

