str1 = "-52.6759008050801,52.3893563178108,-1.41394598074385E-06"  # point in targetPoints:
new_point = str1.replace(",", " ")
print(new_point)
x = (('"_Copy ') + new_point + (' _Enter"'))
print(type(x))
print(x)
"""
x = list()
for copy in list_point:
    x.append('"')
    x.append('_Copy')
    x.append(' ')
"""

# #x = ("_Copy 0,0,0 0,10,0 _Enter")