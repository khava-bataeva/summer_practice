num = (int(input("Введите число: ")))
nums = str(num)
sum = 0
n = len(nums)
for digit in nums:
    sum += int(digit) ** n
if num == sum:
    print(num, "является числом Армстронга")
else:
    print(num, "не является числом Армстронга")
