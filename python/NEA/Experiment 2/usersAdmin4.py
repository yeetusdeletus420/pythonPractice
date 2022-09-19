# Program to administer user accounts 

# text file created by the administrator with fixed record length
# (10 characters - user name, 10 characters - password, 1 character separator and a new line)
# fo = input("Enter the name of the file: ")  
#fo="users.txt"
fo="users.txt"                                          # fixed user permission file
ft="utemp.txt"                                          # temporary file
fa="userA.txt"

ffa=open(fa, "r")                                       # read administrator password from a file
a = ffa.readline()
ffa.close()

p=input("Enter admin account password: ")

if len(p)>10:                                   # limit the password to 10 characters
    p=p[0:10]
blank="          "
p=p+blank[len(p):]                              # entry padded to 10 characters

if p==a:                                                # hard-wired admin password

    print(" ")
    print("Current authorised users:")
    ffo=open(fo, "r")                                   # full file print-out before change
    print(ffo.read())
    ffo.close()

    option="-"                                              # default option setting
    while option.upper()!="A" and option.upper()!="R" and option.upper()!="X":
        option=input("Add users (A); Remove users (R); Exit (X): ")
    
        if option.upper()=="A":                             # Add user section
            u=input("Enter user name: ")
            if len(u)>10:                                   # limit the name to 10 characters
                u=u[0:10]
            p=input("Enter password: ")
            if len(p)>10:                                   # limit the password to 10 characters
                p=p[0:10]
            blank="          "
            u=u+blank[len(u):]                              # entry padded to 10 characters
            p=p+blank[len(p):]                              # entry padded to 10 characters

            ffo = open(fo, "a")
            ffo.write(u+p+";"+chr(10))                      # new user added
            ffo.close()

            print(" ")
            print("Updated set of authorised users:")
            ffo=open(fo, "r")                               # full file print-out after change
            print(ffo.read())
            ffo.close()
            option='-'                                      # default option setting

        if option.upper()=="R":                             # Remove sected user
            u=input("Enter user name: ")
            if len(u)>10:                                   # limit the name to 10 characters
                u=u[0:10]
            blank="          "
            u=u+blank[len(u):]
        
            ffo=open(fo, "r")                               # open the original file for reading
            fft=open(ft,"a")                                # open temporary file for appending
            while True:
                line = ffo.readline()
                if line=='':                                # if empty line then stop
                    break                                   # exit while loop after finding an empty line
                if u != line[0:10]:                         # copy the line that is not to be removed
                    fft.write(line)                         # write lines into temporary file
    
            ffo.close()                                     # close original file
            fft.close()                                     # close temporary file
        
            print(line)        
            print("Updated temporary list of users:")
            fft=open(ft, "r")                               # full file print-out after update
            print(fft.read())
            fft.close()

            ffo=open(fo, "w")                               # open original file for writing (wipe out content)
            ffo.close()                                     # close original file 
        
            ffo=open(fo, "a")                               # open original file for appending entries
            fft=open(ft, "r")                               # open temporary file for reading

            while True:
                line = fft.readline()                       # read lines from the temporary file
                if line=='':                                # if empty line then stop
                    break                                   # exit while loop after finding an empty line
                ffo.write(line)                             # write lines into the original file

            ffo.close()                                     # close original file
            fft.close()                                     # close temporary file

            fft=open(ft, "w")                               # open temporary file for writing (wipe out content)
            fft.close()                                     # close temporary file
            option='-'                                      # default option setting
                
        
        if option.upper()=="X":                             # Exit admin program
            break

