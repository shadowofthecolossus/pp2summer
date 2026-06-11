#You can have if statements inside if statements. This is called nested if statements
username = "Emil"
password = "python123"
is_active = True
    
if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")