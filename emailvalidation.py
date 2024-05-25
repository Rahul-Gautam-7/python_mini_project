email = input("Enter your email ")
valid=0
error=0
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@')==1):
            if (email[-4]=='.') ^ (email[-3]=='.'):
                if (' ' not in email):
                    for i in email:
                        if i.isalpha():
                            if i==i.upper():
                                error=-1
                                break
                            else:
                               valid=1

                else:
                    print("email must not contain space ")
            else:
                print("must contain . ")
        else:
            print("It must contain one @ ")
    else:
        print("The first number must be an alphabet")

else:
    print("Enter a valid email")


if error==-1:
    print("Enter email in lower case")
if valid == 1:
    print("Your email is valid ",email)