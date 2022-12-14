# collect the email from user 
# split the email using  the @, the first part as the user name , the second part is gonna be saved as domain 
# split domain using .,

def main():
    print ("Welcome to the email slicer")
    print("")

    email_input = input("Input your address: ")
    
     # use particular format 
    (username,domain) = email_input.split("@")
    (domain,extension)=domain.split(".")


    print("Username:",username)
    print ("Domain :",domain)
    print("extension: ", extension)
main()    


