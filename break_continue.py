# code asking for name and password using break and continue statements

while True:
    print ('What is your name?')
    name = input()
    if name != 'Belinda':
        continue
    print ('Please enter your password, hint: it is an animal')
    password = input()
    if password == "elephant":
        break
print('Access granted')