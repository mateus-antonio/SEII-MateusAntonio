nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 4:
        print('Found 4')
        break
    if num == 2:
        print('Found 2')
        continue
    print(num)

for num in range(7, 10):
    for letter in 'abc':
        print(num, letter) 

x = 0
while True:
    if x==5:
        break
    print(x)
    x+=1