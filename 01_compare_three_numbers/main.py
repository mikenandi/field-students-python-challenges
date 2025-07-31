def find_greatest(a, b, c):
    if a < b:
        a, b = b, a
    if a < c:
        a, c = c, a
    return a

#user input
num1 = float(input("first number: "))
num2 = float(input("second number: "))
num3 = float(input("third number: "))

# we use function to get the answers
ans = find_greatest(num1, num2, num3)

# we display the answers
print("GREATEST number is:", ans)
