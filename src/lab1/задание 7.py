ind1, ind2 = 0, 0

out = ''
a = input('in: ')

for i in range(len(a)):
    if a[i].isupper():
        out += a[i]
        ind1 = i
        break
    
for i in range(len(a)):
    if a[i] in '0123456789':
        out += a[i+1]
        ind2 = i+1
        break

raznitsa = abs(ind2-ind1)

for i in range(ind2 + raznitsa, len(a),raznitsa):
    out += a[i]
    
if out[-1] != '.':
    out += '.'
print('out:', out)
    
