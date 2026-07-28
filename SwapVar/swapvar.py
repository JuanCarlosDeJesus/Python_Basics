# Swapping Variables

a = 10
b = 20

# old way of swapping
temp = a
a = b 
b = temp

print(a)  # Output: 20
print(b)  # Output: 10

# new way of swapping
a, b = b, a
print(a)  # Output: 10
print(b)  # Output: 20

# Swapping Variables using XOR
a = 24
b = 41

a = a ^ b # 110001
'''
24=011000 = a
41=101001 = b
   110001 = a new value
'''
b = a ^ b
'''
110001 = a
101001 = b
011000 = b new value
'''
a = a ^ b
'''
110001 = a
011000 = b
101001 = a
'''
print(a)  # Output: 20
print(b)  # Output: 10