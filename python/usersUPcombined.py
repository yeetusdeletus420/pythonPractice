# Log-in to the game program
#
# Uploading user names and passwords into a directory data structure
# define a dictionary data structure to be used in the program (up to 10 users)
x = dict(u1="x", u2="x", u3="x", u4="x", u5="x", u6="x", u7="x", u8="x", u9="x", u10="x",
         u11="x", u12="x", u13="x", u14="x", u15="x", u16="x", u17="x", u18="x", u19="x", u20="x",
         u21="x", u22="x", u23="x", u24="x", u25="x", u26="x", u27="x", u28="x", u29="x", u30="x")

# text file created by the administrator with fixed record length
# (10 characters - user name, 10 characters - password, 1 character separator and a new line)
# fo = input("Enter the name of the file: ")  
fo="users.txt"

ffo = open(fo, "r")                         # read user names and passwords from a file

i=0
while True:
    line = ffo.readline()                   # read line
    if line=='':                            # if empty line then stop
        break                               # exit while loop after finding an empty line    
    i=i+1                                   # number of users with passwords
    user="u"+str(i)                         # generate a key for user i
    x[user]=line[0:20]                      # update dictionary entry for user i
    
ffo.close()                                 # close the file

# Check if the user is listed in the dictionary and submits correct password
# 

blank="          "                          # 10-spaces string for padding entries
attempt=3                                   # limit the number of user name trials to 3
exists=0                                    # flag to indicate that entered user name exists

while attempt>0 and exists==0:              # repeat user name entries 
    u=input("Enter user name: ")
    if len(u)>10:                           # limit the name to 10 characters
        u=u[0:10]
    p=input("Enter password: ")
    if len(p)>10:                           # limit the password to 10 characters
        p=p[0:10]

    u=u+blank[len(u):]                      # entry padded to 10 characters
    p=p+blank[len(p):]                      # entry padded to 10 characters
#
# encode password
    from random import seed                      # initiate random function (needed at the final stages)
    from random import randint
    seed(1)
    encode = ''
    for i in range(0,10):
        ofset=randint(32,94)
        encode = encode+chr((ord(p[i])-32+ofset)%95+32)
    p=encode

#
    up=u+p                                  # combined user name and password

# search for the specified user in the directory
    for j in range(1,i+1):                  # iterate a search for a specified user name
        userj="u"+str(j)                    # generate a user name key for the dictionary
        if up==x[userj]:                    # user name exists in the dictionary
            exists=1                        # set the exists flag
            break                           # terminate the search for the user name in the dictionary
    
    attempt=attempt-1                       # decrement trial count for the user name
    if exists==0:
        print("Incorrect user name or password")

if exists==0:                               # unsuccessful entry of user names
    print("Three unsuccessful attempts")
    print("Please register with the administrator of the game")
else:
    print("Play the game")              # SUCCESS, verification completed

#   Code for the selected game
#
    





