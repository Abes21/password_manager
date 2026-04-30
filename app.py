import hashlib
from getpass import getpass

main_password = getpass("Podaj hasło: ")

mainPass = hashlib.sha256(main_password.encode()).hexdigest()
# with open("main_password.txt", "a") as f:
#   f.write(mainPass+"\n")

if(mainPass == mainPass):
  print("test")
else:
  print("Brak dostępu")




# password = hashlib.sha256(input("podaj haslo: ").encode()).hexdigest()
# with open("passwords.txt", "a") as f:
#   f.write(password+"\n")
# print(password)