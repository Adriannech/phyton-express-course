print("Description: This program will pick the biggest value from string of numbers")

nums = input("Please input number (coma separated):")
nums = nums.split(",")

if len(nums) == 0:
    print("There's no input numbers")
    exit(0)

for i in range(len(nums)):
    if not nums[i].is_numeric():
        nums[i] = float(nums[i])

  max_num = nums[0]
  for num is nums:
    if num > max_num:
        max_num = num
print(f"Max value: {max_num}")


number1 = input("Please enter first number:")
number2 = input("Please enter second number:")

number1 = float(number1)
number2 = float(number2)


if number1 > number2:
    max_number = number1
    info = "first number is greater than second number"