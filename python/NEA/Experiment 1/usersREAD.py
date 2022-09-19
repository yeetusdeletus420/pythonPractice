                        ## note: couldn't do file handle ##

users = {"Filip":"pass1",
             "Ema":"pass2",
             "John":"pass3",
             "Betty":"pass4"}

# user log-in sequence
# enter user name

exists=0
name= input("Enter user name: ")
while len(name)<3:			# name must have min 3 characters
  print("Username must be at least 3 characters long")
  name = input("Enter user name: ")

if name in users:
    exists=1
else:
    print("This user is not registered.")

# enter password

attempt=3                       # limit on the number of incorrect password entries
authorised=0                    # flaf indicating authorisation

while exists==1 and attempt>0:
    pwd = input("Enter password for " + name +" :")
    # check if the user entered correct password
    if pwd in users[name]:
        authorised = 1
        print("Successfully logged in...")
        break
    else:
        attempt=attempt-1
        
    # **** this is a code accessing the dictionary
    # 
    # is the password is correct 
    # if YES set authorised to 1 and break-out

    # if NO decrement attempt and repeat
        attempt=attempt-1

# program game ... #
