email = input("Enter your email: ").lower()
emaillist = []
passlist = []
caplist = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
small = [chr(i) for i in range(ord('a'), ord('z') + 1)]
symbols = ['@', "$", "#", "%", "^"]
flag = False

# Email validation
for x in email:
    emaillist.append(x)
while not flag:
    if len(emaillist) <= 30:
        if '@gmail.com' in email:
            flag = True
        else:
            print('@gmail.com is missing')
            break
    else:
        print("Email should contain at most 30 characters")
        break

# Password validation
if flag:
    password = input("Enter your password: ")
    has_upper = False
    has_lower = False
    has_symbol = False

    if len(password) >= 8:
        for z in password:
            if z in caplist:
                has_upper = True
            if z in small:
                has_lower = True
            if z in symbols:
                has_symbol = True

        if has_upper or has_lower:
            if has_symbol:
                print("Success")
            else:
                print("Password should contain at least one symbol")
        else:
            print("Password should contain at least one capital or small letter")
    else:
        print("Password should contain at least 8 characters")
