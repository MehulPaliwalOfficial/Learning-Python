# num = 30
# secret = 34
# encrypted_num = num ^ secret
# print("Sending:", encrypted_num)
# print("Receiving:", encrypted_num ^ secret)  # Decrypting the number using XOR with the same secret

# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")
    
# num = int(input("Enter a number: "))
# if num & 1 == 0:
#     print("The number is even.")
# else:
#     print("The number is odd.")

READ    = 0b100 #4
WRITE   = 0b010 #2
EXECUTE = 0b001 #1

perms = READ | WRITE
print(bin(perms))   #user can read and write, but not execute

print(bool(perms & READ))       # can the user read?
print(bool(perms & EXECUTE))    #can the user execute?