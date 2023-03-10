import rhinoscriptsyntax as rs
#x = ("_Copy 0,0,0 0,10,0 _Enter")
x = list()
x.append('"')
x.append('_Copy')
x.append(' ')
x.append('0,0,0')
x.append(' ')
x.append('0,10,0')
x.append(' ')
x.append('0,10,0')
x.append(' ')
x.append('_Enter')
x.append('"')

print(x)
y = ''.join(x)
print(y)
#rs.Command(x)
            #print(xyz) #xyz ini sudah ok
            #translation = point-start
            #rs.CopyObjects( objectIds, translation )
            
"""
listnya = ['10.000 34.000 50.000', '3.000 5.000 9.000']
print(listnya)
co = ('_Copy 0 0 0 ')
jadi = ' '.join(listnya)
print(jadi)
jadi2 = ('"' + co + jadi + '"')
print(jadi2)
"""
