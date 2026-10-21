# n = int(input())
# i = 1
# while i<=n//2:
#     if n%i==0:
#         print(i)
#     i+=1
# print(n)

# n = int(input())
# i = 1
# while i<=n**(1/2):
#     if n%i==0:
#         print(i)
#         if i != n//i:
#             print(n//i)
#     i +=1

# Count Method
# n = int(input())
# i = 1
# factor_count = 0
# while i<=n:
#     if n%i==0:
#         factor_count += 1
#     i +=1
# if factor_count == 2:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")

# Flag Method
# n = int(input())
# is_prime = True
# if n <= 1:
#     is_prime = False
# else:
#     i = 2
#     while i < n:
#         if n % i == 0:
#             is_prime = False
#         i += 1
# if is_prime == True:
#     print(n, "is a prime number")
# else:
#     print(n, "is not a prime number")


# n = int(input())
# p = 0
# digits = n
# while digits>0:
#     p +=1
#     digits = digits//10
# digits = n
# total_sum = 0
# while digits > 0:
#     last_digit = digits % 10
#     total_sum = total_sum + (last_digit ** p)
#     digits = digits // 10
# if total_sum == n:
#     print("It is an Armstrong number!")
# else:
#     print("It is NOT an Armstrong number.")



