def game():
    
    print()
    print("Rolling two 6-sided dice five times and totalling the count of top surfaces")
    print("The throw is controlled by the selection of the seed (any key on the keyboard)")
    print("Results of individual throws are not shown; only the total after 5 throws")
    print("Highest total count WINS")
    print()

    from random import seed                      # initiate random function (needed at the final stages)
    from random import randint

    cycle=1
    #player=1
    D1=0
    D2=0

    while cycle<6:
        s1=input("P1 Roll the dice: ") # or "Enter the seed: "
        seed=(s1)
        d11=randint(1,6)
        d12=randint(1,6)
        D1=D1+d11+d12
        cycle=cycle+1

    cycle=1
    while cycle<6:
     
        s2=input("                         P2 Roll the dice: ") # or "Enter the seed: "
        seed=(s2)
        d21=randint(1,6)
        d22=randint(1,6)
        D2=D2+d21+d22
        cycle=cycle+1
        
    if D1>D2:
        result=u1+" won "+str(D1)+"/"+str(D2)
        print(u1+" won "+str(D1)+"/"+str(D2))
    if D1==D2:
        result="Draw "+str(D1)+"/"+str(D2)
        print("Draw "+str(D1)+"/"+str(D2))
    if D1<D2:
        result=u2+" won "+str(D1)+"/"+str(D2)
        print(u2+" won "+str(D1)+"/"+str(D2))

    fr="usersresults.txt"

    ffr = open(fr, "a")
    ffr.write(result+chr(13))
    ffr.close()

                        # Log-in to the game program #

# Uploading user names and passwords into a directory data structure
# define a dictionary data structure to be used in the program (up to 10 users)
x = dict(u1="x", u2="x", u3="x", u4="x", u5="x", u6="x", u7="x", u8="x", u9="x", u10="x",
         u11="x", u12="x", u13="x", u14="x", u15="x", u16="x", u17="x", u18="x", u19="x", u20="x",
         u21="x", u22="x", u23="x", u24="x", u25="x", u26="x", u27="x", u28="x", u29="x", u30="x")

# text file created by the administrator with fixed record length
# (10 characters - user name, 10 characters - password, 1 character separator and a new line)
# fo = input("Enter the name of the file: ")  
fo="realUsers.txt"

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
    u=input("Player 1 enter username: ")
    u1=u
    if len(u)>10:                           # limit the name to 10 characters
        u=u[0:10]

    p=input("Enter password: ")
    if len(p)>10:                           # limit the password to 10 characters
        p=p[0:10]

    u=u+blank[len(u):]                      # entry padded to 10 characters
    p=p+blank[len(p):]                      # entry padded to 10 characters

#


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

if attempt==0:                               # unsuccessful entry of user names
    print("Three unsuccessful attempts")
    print("No permission to play. Exiting...")
    exit
else:

    ask=input("""Do you want to play with a registered user? [1]
Or Guest? [2]
""")
    if ask == "1":
        blank="          "                          # 10-spaces string for padding entries
        attempt=3                                   # limit the number of user name trials to 3
        exists=0                                    # flag to indicate that entered user name exists

        while attempt>0 and exists==0:              # repeat user name entries 
            u=input("Player 2 enter username: ")
            u2=u
            if len(u)>10:                           # limit the name to 10 characters
                u=u[0:10]

            p=input("Enter password: ")
            if len(p)>10:                           # limit the password to 10 characters
                p=p[0:10]

            u=u+blank[len(u):]                      # entry padded to 10 characters
            p=p+blank[len(p):]                      # entry padded to 10 characters

        #


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

        if attempt==0:                               # unsuccessful entry of user names
            print("Three unsuccessful attempts")
            print("No permission to play. Exiting...")
            exit
        
    if ask == "2":
        u2="guest"

    clear=input("Do you want to clear the scoresheet? Y or N: ").upper()
    if clear == "Y":
        frr=open("usersresults.txt", "w")
        frr.close()
        
    print("Play the game")             # SUCCESS, verification completed
    game()

    view=input("Do you want to see the scoresheet? Y or N: ").upper()
    if view=="Y":
        print("")
        frr=open("usersresults.txt", "r")
        print(frr.read())
        frr.close()
