def mod(number):
    y = number//2   # By using // we get the quotient part of the division
    z = number % 2    # By using % we get the remainder part of the division
    print(z)
    return y


nums = int(input("Please enter any number: "))
m = mod(nums)
print(m)
