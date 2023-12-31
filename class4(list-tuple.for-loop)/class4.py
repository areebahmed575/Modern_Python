database : list[tuple[str,str]] = [("qasim","123"),("areeb","456"),("ali","890")]

user :str =input("Enter your name:")
passw :str =input("Enter your passwrd:")

for i in database:
    username,password = i
    #print(username,password)
    if username == user and password == passw:
        print(f"Valid {user}")
        break
else:
    print(f"Invalid {user}")    


print([2 * i for i in range(1,11)])    