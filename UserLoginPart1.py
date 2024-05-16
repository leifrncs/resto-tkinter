# TOMALON: Assignment User Login
# Please maximize for better view of windows

from tkinter import *
from tkinter import messagebox


# Main window, login
def login_window():
    
    
  # Create a dictionary for user data with predefined users for each role
  user_data = {
      "admin": {
          "name": "Admin",
          "password": "admin123",
          "role": "Admin"
      },
      "staff": {
          "name": "Staff",
          "password": "staff123",
          "role": "Staff"
      },
      "customer": {
          "name": "Customer",
          "password": "customer123",
          "role": "Customer"
      }
  }

  # Login fnucntion
  def login():
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()
    print("Username: ", username)
    print("Password: ", password)

    # Check if any of the fields are empty
    if not username or not password:
      messagebox.showerror(
          "User Login",
          "Invalid input: Please enter both username and password.")
    # Check if the username and password match
    elif username not in user_data or user_data[username].get(
        "password") != password:
      messagebox.showerror(
          "User Login",
          "Invalid username or password. \nOr Account does not exist!")
    else:
      role = user_data[username]["role"]
      messagebox.showinfo("User Login", "Login successful!")
      root.destroy()
      # Open the appropriate page or window based on the user's role
      if role == "Admin":
        open_admin_page(user_data[username]["name"])
      elif role == "Staff":
        open_staff_page(user_data[username]["name"])
      else:
        open_customer_page(user_data[username]["name"])

  def signup():

    def register():
      # Get the entered name, username, password, and role
      name = name_reg_entry.get()
      username = username_reg_entry.get()
      password = password_reg_entry.get()
      print("Username: ", username)
      print("Password: ", password)
      role = role_var.get()

      # Check if any of the fields are empty
      if not username or not password or not role:
        messagebox.showerror(
            "Registration",
            "Invalid input: Please enter username, password, and select a role"
        )
      # Check if the username is already taken
      elif username in user_data:
        messagebox.showerror("Registration", "Username already exists")
      else:
        # Add the new user to the user_data dictionary
        user_data[username] = {
            "name": name,
            "password": password,
            "role": role
        }
        messagebox.showinfo("Registration", "Successful registration")
        signup_window.destroy()

    # Create a new window for registration
    signup_window = Toplevel(root)
    signup_window.title("Registration")
    signup_window.resizable(False, False)
    signup_window.configure(bg="#E4CFBB")

    # Create a label for the registration window
    registration_label = Label(signup_window,
                               text="Sign Up to Lei's Kitchen",
                               font=("Georgia", 12, "bold"),
                               fg="white",
                               bg="#D4AD79",
                               padx=65,
                               pady=20)
    registration_label.pack(pady=20)

    #Create a frame for login content with background color
    signup_frame = Frame(signup_window, bg="#D4AD79", padx=30, pady=30)
    signup_frame.pack(padx=10, pady=10)

    # Create labels and entry fields for name, username, and password
    name_reg_label = Label(signup_frame,
                           text="Name:",
                           font=("Georgia", 10, "bold"),
                           fg="white",
                           bg="#D4AD79")
    name_reg_label.grid(row=0, column=0, sticky="w")
    name_reg_entry = Entry(signup_frame, font=("Georgia", 10))
    name_reg_entry.grid(row=0, column=1, pady=10)

    username_reg_label = Label(signup_frame,
                               text="Username:",
                               font=("Georgia", 10, "bold"),
                               fg="white",
                               bg="#D4AD79")
    username_reg_label.grid(row=1, column=0, sticky="w")
    username_reg_entry = Entry(signup_frame, font=("Georgia", 10))
    username_reg_entry.grid(row=1, column=1, pady=10)

    password_reg_label = Label(signup_frame,
                               text="Password:",
                               font=("Georgia", 10, "bold"),
                               fg="white",
                               bg="#D4AD79")
    password_reg_label.grid(row=2, column=0, sticky="w")
    password_reg_entry = Entry(signup_frame, show="*", font=("Georgia", 10))
    password_reg_entry.grid(row=2, column=1, pady=10)

    # Create a dropdown menu for selecting the role
    role_reg_label = Label(signup_frame,
                           text="Role:",
                           font=("Georgia", 10, "bold"),
                           fg="white",
                           bg="#D4AD79")
    role_reg_label.grid(row=3, column=0, sticky="w")
    role_var = StringVar(signup_frame)
    role_var.set("Customer")  # Default role is Customer
    role_reg_dropdown = OptionMenu(signup_frame, role_var, "Admin", "Staff",
                                   "Customer")
    role_reg_dropdown.grid(row=3, columnspan=2, pady=10)

    # Create a button to register the user
    register_button = Button(signup_frame,
                             text="Register",
                             command=register,
                             font=("Georgia", 10))
    register_button.grid(row=4, columnspan=2, pady=10)

    signup_window.mainloop()

  #Create a new window for the admin page
  def open_admin_page(name):
    admin_page = Tk()
    admin_page.title("Welcome to Lei's Kitchen")
    admin_page.geometry("950x595")
    admin_page.resizable(False, False)
    admin_page.configure(bg="#E4CFBB")

    # Create a frame on the left side of the admin page
    left_frame = Frame(admin_page,
                       highlightbackground="#FAEFCF",
                       highlightthickness=4,
                       bg="#D4AD79",
                       pady=25)
    left_frame.pack(side=LEFT, fill="y")

    # Create a frame for the image on the admin page
    image_frame = Frame(admin_page)
    image_frame.pack()
    image_frame.place(anchor='center', relx=0.68, rely=0.47)

    # Load and display the image on the admin page
    try:
      image = PhotoImage(file="OpenSoon.png").subsample(1, 1)
    except TclError as e:
      print("Error loading image", e)
    else:
      image_label = Label(image_frame,
                          text="Lei'sKitchen",
                          font=("Arial", 12, "bold"),
                          image=image)
      image_label.pack(padx=0, pady=0)
      root.image = image

    # Create the title label on the left frame
    title_label = Label(left_frame,
                        text="Welcome, " + name.capitalize() + "!",
                        font=("Georgia", 18, "bold"),
                        fg="#3D2F21",
                        bg="#D4AD79",
                        padx=20,
                        pady=5)
    title_label.grid(row=0, column=0, sticky="n")

    # Create labels for different sections on the left frame
    dashboard_button = Button(left_frame,
                            text="Dashboard",
                            font=("Georgia", 12, "bold"),
                            fg="#3D2F21",
                            bg="#D1AD88",
                            padx=67,
                            pady=10,
                            borderwidth=2,
                            relief='ridge')
    dashboard_button.grid(row=1, column=0, pady=15)

    order_button = Button(left_frame,
                        text="Orders",
                        font=("Georgia", 12, "bold"),
                        fg="#3D2F21",
                        bg="#D1AD88",
                        padx=83,
                        pady=10,
                        borderwidth=2,
                        relief='ridge')
    order_button.grid(row=2, column=0, pady=15)

    menu_button = Button(left_frame,
                       text="Menus",
                       font=("Georgia", 12, "bold"),
                       fg="#3D2F21",
                       bg="#D1AD88",
                       padx=85,
                       pady=10,
                       borderwidth=2,
                       relief='ridge')
    menu_button.grid(row=3, column=0, pady=15)

    members_button = Button(left_frame,
                          text="Members",
                          font=("Georgia", 12, "bold"),
                          fg="#3D2F21",
                          bg="#D1AD88",
                          padx=74,
                          pady=10,
                          borderwidth=2,
                          relief='ridge')
    members_button.grid(row=4, column=0, pady=15)

    aboutus_button = Button(left_frame,
                          text="About Us",
                          font=("Georgia", 12, "bold"),
                          fg="#3D2F21",
                          bg="#D1AD88",
                          padx=74,
                          pady=10,
                          borderwidth=2,
                          relief='ridge')
    aboutus_button.grid(row=5, column=0, pady=15)

    # Create a button to logout and destroy the admin page window
    logout_button = Button(
        left_frame,
        text="Logout",
        font=("Georgia", 12, "bold"),
        pady=10,
        padx=83,
        command=lambda: [admin_page.destroy(),
                         login_window()])
    logout_button.grid(row=6, column=0, padx=20, pady=10)

    copyright_label = Label(admin_page,
                            text="© 2024 Lei's Kitchen",
                            font=("Georgia", 8, "bold", "italic"),
                            fg="Black",
                            bg="#E4CFBB")
    copyright_label.place(anchor='center', relx=0.68, rely=0.95)

    # Start the admin page window's main loop
    admin_page.mainloop()

  #Create a new window for the staff page
  def open_staff_page(name):
    staff_page = Tk()
    staff_page.title("Welcome to Lei's Kitchen")
    staff_page.geometry("950x595")
    staff_page.resizable(False, False)
    staff_page.configure(bg="#E4CFBB")

    # Create a frame on the left side of the staff page
    left_frame = Frame(staff_page,
                       highlightbackground="#FAEFCF",
                       highlightthickness=4,
                       bg="#D4AD79",
                       pady=25)
    left_frame.pack(side=LEFT, fill="y")

    # Create a frame for the image on the staff page
    image_frame = Frame(staff_page)
    image_frame.pack()
    image_frame.place(anchor='center', relx=0.68, rely=0.47)

    # Load and display the image
    try:
      image = PhotoImage(file="OpenSoon.png").subsample(1, 1)
    except TclError as e:
      print("Error loading image", e)
    else:
      image_label = Label(image_frame,
                          text="Lei'sKitchen",
                          font=("Arial", 12, "bold"),
                          image=image)
      image_label.pack(padx=0, pady=0)
      root.image = image

    # Create the title label on the left frame
    title_label = Label(left_frame,
                        text="Welcome, " + name.capitalize() + "!",
                        font=("Georgia", 18, "bold"),
                        fg="#3D2F21",
                        bg="#D4AD79",
                        padx=20,
                        pady=10)
    title_label.grid(row=0, column=0, sticky="n")

    # Create labels for different sections on the left frame
    dashboard_button = Button(left_frame,
                            text="Dashboard",
                            font=("Georgia", 12, "bold"),
                            fg="#3D2F21",
                            bg="#D1AD88",
                            padx=65,
                            pady=10,
                            borderwidth=2,
                            relief='ridge')
    dashboard_button.grid(row=1, column=0, pady=15)

    order_button = Button(left_frame,
                        text="Orders",
                        font=("Georgia", 12, "bold"),
                        fg="#3D2F21",
                        bg="#D1AD88",
                        padx=80,
                        pady=10,
                        borderwidth=2,
                        relief='ridge')
    order_button.grid(row=2, column=0, pady=15)

    menu_button = Button(left_frame,
                       text="Menus",
                       font=("Georgia", 12, "bold"),
                       fg="#3D2F21",
                       bg="#D1AD88",
                       padx=82,
                       pady=10,
                       borderwidth=2,
                       relief='ridge')
    menu_button.grid(row=3, column=0, pady=15)

    shift_button = Button(left_frame,
                        text="Shift",
                        font=("Georgia", 12, "bold"),
                        fg="#3D2F21",
                        bg="#D1AD88",
                        padx=89,
                        pady=10,
                        borderwidth=2,
                        relief='ridge')
    shift_button.grid(row=4, column=0, pady=15)

    aboutus_button = Button(left_frame,
                          text="About Us",
                          font=("Georgia", 12, "bold"),
                          fg="#3D2F21",
                          bg="#D1AD88",
                          padx=71,
                          pady=10,
                          borderwidth=2,
                          relief='ridge')
    aboutus_button.grid(row=5, column=0, pady=15)

    # Create a button to logout and destroy the staff page window
    logout_button = Button(
        left_frame,
        text="Logout",
        font=("Georgia", 12, "bold"),
        pady=10,
        padx=80,
        command=lambda: [staff_page.destroy(),
                         login_window()])
    logout_button.grid(row=6, column=0, padx=20, pady=20)

    copyright_label = Label(staff_page,
                            text="© 2024 Lei's Kitchen",
                            font=("Georgia", 8, "bold", "italic"),
                            fg="Black",
                            bg="#E4CFBB")
    copyright_label.place(anchor='center', relx=0.68, rely=0.95)

    # Start the staff page window's main loop
    staff_page.mainloop()

  #Create a new window for the customer page
  def open_customer_page(name):
    customer_page = Tk()
    customer_page.title("Welcome to Lei's Kitchen")
    customer_page.geometry("950x595")
    customer_page.resizable(False, False)
    customer_page.configure(bg="#E4CFBB")

    # Create a frame on the left side of the staff page
    left_frame = Frame(customer_page,
                       highlightbackground="#FAEFCF",
                       highlightthickness=4,
                       bg="#D4AD79",
                       pady=20)
    left_frame.pack(side=LEFT, fill="y")

    # Create a frame for the image on the staff page
    image_frame = Frame(customer_page)
    image_frame.pack()
    image_frame.place(anchor='center', relx=0.68, rely=0.47)

    # Load adn display the image
    try:
      image = PhotoImage(file="OpenSoon.png").subsample(1, 1)
    except TclError as e:
      print("Error loading image", e)
    else:
      image_label = Label(image_frame,
                          text="Lei'sKitchen",
                          font=("Arial", 12, "bold"),
                          image=image)
      image_label.pack(padx=0, pady=0)
      root.image = image

    # Create the title label on the left frame
    title_label = Label(left_frame,
                        text="Welcome, " + name.capitalize() + "!",
                        font=("Georgia", 18, "bold"),
                        fg="#3D2F21",
                        bg="#D4AD79",
                        padx=20,
                        pady=10)
    title_label.grid(row=0, column=0, sticky="n")

    # Create labels for different sections on the left frame
    menu_button = Button(left_frame,
                       text="Menus",
                       font=("Georgia", 12, "bold"),
                       fg="#3D2F21",
                       bg="#D1AD88",
                       padx=83,
                       pady=10,
                       borderwidth=2,
                       relief='ridge')
    menu_button.grid(row=1, column=0, pady=15)

    cart_button = Button(left_frame,
                       text="Cart",
                       font=("Georgia", 12, "bold"),
                       fg="#3D2F21",
                       bg="#D1AD88",
                       padx=92,
                       pady=10,
                       borderwidth=2,
                       relief='ridge')
    cart_button.grid(row=2, column=0, pady=15)

    receipt_button = Button(left_frame,
                          text="Receipt",
                          font=("Georgia", 12, "bold"),
                          fg="#3D2F21",
                          bg="#D1AD88",
                          padx=78,
                          pady=10,
                          borderwidth=2,
                          relief='ridge')
    receipt_button.grid(row=3, column=0, pady=15)

    aboutus_button = Button(left_frame,
                          text="About Us",
                          font=("Georgia", 12, "bold"),
                          fg="#3D2F21",
                          bg="#D1AD88",
                          padx=71,
                          pady=10,
                          borderwidth=2,
                          relief='ridge')
    aboutus_button.grid(row=4, column=0, pady=15)

    contactus_button = Button(left_frame,
                            text="Contact Us",
                            font=("Georgia", 12, "bold"),
                            fg="#3D2F21",
                            bg="#D1AD88",
                            padx=63,
                            pady=10,
                            borderwidth=2,
                            relief='ridge')
    contactus_button.grid(row=5, column=0, pady=15)

    # Create a button to logout and destroy the customer page window
    logout_button = Button(
        left_frame,
        text="Logout",
        font=("Georgia", 12, "bold"),
        pady=10,
        padx=80,
        command=lambda: [customer_page.destroy(),
                         login_window()])
    logout_button.grid(row=6, column=0, padx=20, pady=20)

    copyright_label = Label(customer_page,
                            text="© 2024 Lei's Kitchen",
                            font=("Georgia", 8, "bold", "italic"),
                            fg="Black",
                            bg="#E4CFBB")
    copyright_label.place(anchor='center', relx=0.68, rely=0.95)

    # Start the customer page window's main loop
    customer_page.mainloop()
    
  # Create the main window
  root = Tk()
  root.title("Welcome to Lei's Kitchen!")
  root.geometry("950x595")
  root.resizable(False, False)

  # Create a frame for login content with background color
  login_frame = Frame(root, bg="#E4CFBB", padx=50, pady=50)
  login_frame.pack(side=TOP, fill="x")

  # Create the title label for the login section
  title_label = Label(login_frame,
                      text="USER LOGIN",
                      font=("Georgia", 12, "bold"),
                      fg="white",
                      bg="#D4AD79",
                      padx=58,
                      pady=12)
  title_label.place(relx=.81, rely=.18, anchor="n")

  # Load and display the image on the left side
  image_frame = Frame(login_frame)
  image_frame.grid(row=0, column=0)

  # Load the image
  try:
    image = PhotoImage(file="Logo.png").subsample(1, 1)
  except TclError as e:
    print("Error loading image", e)
  else:
    image_label = Label(image_frame,
                        text="Lei'sKitchen",
                        font=("Arial", 12, "bold"),
                        image=image)
    image_label.pack(padx=0, pady=0)
    root.image = image

  # Create a frame for the right grid with background color
  right_frame = Frame(login_frame, bg="#D4AD79")
  right_frame.grid(row=0, column=1, padx=73, pady=20)

  # Usernmae entry label
  username_label = Label(right_frame,
                         text="Username: ",
                         font=("Georgia", 10, "bold"),
                         fg="white",
                         bg="#D4AD79")
  username_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
  username_entry = Entry(right_frame, font=("Times New Roman", 12))
  username_entry.grid(row=1, columnspan=2, padx=30, pady=5)

  # Password entry label
  password_label = Label(right_frame,
                         text="Password: ",
                         font=("Georgia", 10, "bold"),
                         fg="white",
                         bg="#D4AD79")
  password_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
  password_entry = Entry(right_frame, show="*", font=("Times New Roman", 12))
  password_entry.grid(row=3, columnspan=2, padx=30, pady=0)

  # Login button
  login_button = Button(right_frame,
                        text="Login",
                        command=login,
                        font=("Georgia", 10))
  login_button.grid(row=4, column=0, padx=20, pady=10, sticky="w")

  or_label = Label(login_frame,
                   text="or",
                   font=("Georgia", 9, "bold"),
                   fg="white",
                   bg="#D4AD79",
                   padx=0,
                   pady=0)
  or_label.place(relx=.82, rely=0.61, anchor="n")

  # SignUp button
  signup_button = Button(right_frame,
                         text="Signup",
                         command=signup,
                         font=("Georgia", 10))
  signup_button.grid(row=4, column=1, pady=10)

  copyright_label = Label(login_frame,
                          text="© 2024 Lei's Kitchen",
                          font=("Georgia", 8, "bold", "italic"),
                          fg="Black",
                          bg="#E4CFBB")
  copyright_label.place(relx=0.81, rely=1, anchor="n")

  # Main window loop
  root.mainloop()


# Call the login_window to start the application
login_window()
