password = input("Enter Password: ")
password_length = str(8)
message = ("is too short")
message_2 = (" is Good✅ ")
if password < password_length:
     print(f"{password} {message}")
     if password >= password_length:
          print(f"{password} {message_2}")

else:
     print(f"{password} {message_2}")