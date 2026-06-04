class Chatbook:
    def __init__(self):
        self.username= ''
        self.email= ''
        self.password= ''
        self.loggedin= False 

    def menu(self): 
        user_input= input("""Welcome to Chatbook!!! How would you like to proceed ?
                          1. Press 1 to signup.
                          2. Press 2 to signin.
                          3. Press 3 to write a post.
                          4. Press 4 to message a friend.
                          5. Press 5 to logout.
                          6. Press any other key to exit.
                          \n Please Enter: """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input == "4":
            self.message_friend()
        elif user_input == "5":
            self.logout()
        else: 
            exit()

        
    def signup(self):
        
        name= input("\nEnter your first and last name: ")
        email= input("\nEnter your mail:  ")
        pwd= input("\nEnter password: ")
        self.username= name 
        self.email= email 
        self.password= pwd 
        print("\n✅You have signup sucessfully")
        self.signin()


    def signin(self):
        print("\n Continue to signin to login\n")
        if self.email== '' and self.password == '':
            print("\n😊Please signup first to continue")
        else: 
            umail= input("\nEnter email: ")
            upwd= input("\nEnter password: ")
            if self.email == umail and self.password == upwd:
                self.loggedin = True
                print("\n✅You have signed in successfully")
            else:
                print("\n❌Given email and password donot exist")
        print("\n")
        self.menu()


    def my_post(self):
        if self.loggedin == True:
            txt= input("\nEnter your message here: ")
            print(f"🔥You post: {txt}")
        else:
            print("You need to signin first to post something")
        print("\n")
        self.menu()

    def message_friend(self):
        if self.loggedin == True:
            txt= input("\nEnter your message: ")
            frnd= input("\nWhom to send the msg?")
            print("Your message has been sent to ", frnd)
        else:
            print("\n You need to signin first")
        self.menu()
            
    def logout(self):
        self.loggedin = False
        print("➡️ You have logged out sucessfully")
        self.signin()
obj= Chatbook()
obj.menu()