users={"melih":"123456","mehmet":"password","fatma":"deneme"}
name=input("input username: ")
pw=input("input password: ")
if users[name]==pw:
    print("login succesfully")
else:
    print("wrong password or username")
