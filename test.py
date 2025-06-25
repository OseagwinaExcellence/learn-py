password = input("Enter Password: ")
password_length = 8

message = ("is too short")
message_2 = (" is Good✅ ")
if password < password_length:
     print(f"{password} {message}")
     print(f"password must be 8 characters long")
else:
     print(f"{password} {message_2}")