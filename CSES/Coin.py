# Read the number of test cases
t = int(input())

for i in range(t):
    line = input().split()
    a = int(line[0])
    b = int(line[1])
    
    if (a + b) % 3 == 0 and a <= 2 * b and b <= 2 * a:
        print("YES")
    else:
        print("NO")
