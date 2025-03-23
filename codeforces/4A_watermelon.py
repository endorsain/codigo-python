def watermelon_weight(w):
  if w > 2 and w % 2 == 0:
    return 'Yes'
  else:
    return 'No'

w = int(input())
print(watermelon_weight(w))
