palavra = input('Palavra: ')
i = 0
new = ''
while i < len(palavra):
  if palavra[i] in 'aeiou':
    new += '*'
  else:
    new += palavra[i]
  i += 1
print(new)