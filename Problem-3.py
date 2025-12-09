a = int(input("Enter a number: "))

limit = a
if a % 2 == 0:
    limit = a - 1   

result = []
for i in range(1, limit * 2, 2):
    result.append(i)

print(*result, sep=", ")
