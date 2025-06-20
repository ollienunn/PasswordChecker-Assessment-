import gooeypie as gp
import hashlib
import requests

WIDTH = 800
HEIGHT = 600
ROWS = 4
COLUMNS = 3

############ Classes (def) ############

def check_exit(): # Checks if the user wants to exit the app
    ok_to_exit = app.confirm_yesno('Really?', 'Are you sure you want to close?', 'question')
    return ok_to_exit

def toggle_mask(event): # Toggles the password
    password_inp.toggle() # Makes the input visible or not

def open_about_me_window(event): # Opens the about me window
    about_me_window.show()

def open_requirements_window(event): # Opens the about me window
    requirments_window.show()

def check_password(event): # Checks the password

    password = password_inp.text # Gets the password
    feedback.text = "" # Clears the feedback
    strength_password.value = 100 # Sets the progress bar to 0

    if not any(char for char in password): # Checks if there are numbers in the password
        feedback.text += "You must input a password\n" # Adds to the feedback
        strength_password.value -= 100
        app.set_icon("Cross.png") # Sets the icon of the app
    else:
        f = open("passwords_10k.txt") #Pass word checker
        common_passwords = f.readlines()
        r = open("10000-passwords.txt") #Pass word checker
        more_common_passwords = r.readlines()
        clean_passwords = []

        if len(password) <= 6: # Checks the length of the password
            feedback.text += "Your password is very short must be 10 characters or more\n" # Adds to the feedback
            strength_password.value -= 90
            app.set_icon("Cross.png") # Sets the icon of the app
        elif len(password) <= 9:
            strength_password.value -= 50
            app.set_icon("Cross.png") # Sets the icon of the app
            if not any(char.isdigit() for char in password): # Checks if there are numbers in the password
                feedback.text += "Your password must contain a number\n" # Adds to the feedback
                strength_password.value -= 10 
            if not any(char.isupper() for char in password): # Checks if there are uppercase letters in the password
                feedback.text += "Your password must contain at least 1 uppercase letter\n" # Adds to the feedback
                strength_password.value -= 10 
            if not any(char.islower() for char in password): # Checks if there are lowercase letters in the password
                feedback.text += "Your password must contain at least 1 lowercase letter\n" # Adds to the feedback
                strength_password.value -= 10
            if not any(not char.isalnum() for char in password):  # Checks if there are special characters
                feedback.text += "Your password must contain at least 1 special character eg. !@#$%&*()\n"
                strength_password.value -= 10
            feedback.text += "Your password is getting closer but must 10 characters or more\n" # Adds to the feedback
            for passwords in common_passwords:
                passwords = passwords.replace("\n", "")
                clean_passwords.append(passwords)
            
            for passwords in more_common_passwords:
                passwords = passwords.replace("\n", "")
                clean_passwords.append(passwords)
 
            for common in clean_passwords:
                if common and common in password and len(common) > 3:  # Avoid empty lines and very short substrings
                    strength_password.value -= 15
                    feedback.text += "Your password contains a very common password ('{}'), make it more unique!\n".format(common)
                    break
            
            sequential_stuff(password)
            #check_password_pwned(password)  # Checks if the password has been pwned
            check_password_pwned(password) # It works but gives a warning in the console
            if strength_password.value <= 0:   
                strength_password.value = 0                                                                                                  

        elif len(password) >= 10: # Checks the length of the password
            if not any(char.isdigit() for char in password): # Checks if there are numbers in the password
                feedback.text += "Your password must contain a number\n" # Adds to the feedback
                strength_password.value -= 20 
            if not any(char.isupper() for char in password): # Checks if there are uppercase letters in the password
                feedback.text += "Your password must contain at least 1 uppercase letter\n" # Adds to the feedback
                strength_password.value -= 20 
            if not any(char.islower() for char in password): # Checks if there are lowercase letters in the password
                feedback.text += "Your password must contain at least 1 lowercase letter\n" # Adds to the feedback
                strength_password.value -= 20 
            if not any(not char.isalnum() for char in password):  # Checks if there are special characters
                feedback.text += "Your password must contain at least 1 special character eg. !@#$%&*()\n"
                strength_password.value -= 20
 
            for passwords in common_passwords:
                passwords = passwords.replace("\n", "")
                clean_passwords.append(passwords)
            
            for passwords in more_common_passwords:
                passwords = passwords.replace("\n", "")
                clean_passwords.append(passwords)
            
            for common in clean_passwords:
                if common and common in password and len(common) > 3:  # Avoid empty lines and very short substrings
                    strength_password.value -= 30
                    feedback.text += "Your password contains a very common password ('{}'), make it more unique!\n".format(common)
                    break
            
            sequential_stuff(password)
            #check_password_pwned(password)  # Checks if the password has been pwned
            check_password_pwned(password) # It works but gives a warning in the console
            if strength_password.value <= 0:   
                strength_password.value = 0       

            if strength_password.value >= 85:
                feedback.text += "Your password stronger than most good job\n"
    
        f.close()
        r.close()

def check_password_pwned(password):
    try:
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        headers = {"User-Agent": "PasswordChecker9000"}
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code != 200:
            app.alert("Error", "Error checking if password has been pwned please wait than try again")
            return 0

        hashes = (line.split(':') for line in res.text.splitlines())
        for h, count in hashes:
            if h == suffix:
                feedback.text += f"⚠️ This password has been found in {count} breaches! do not use this password\n"
                strength_password.value = 0
                app.set_icon("Cross.png")
                return int(count)

        return 0
    except Exception as e:
        app.alert("Error", "Error checking the pwned passwords please wait than try again", "error")
        return 0

def sequential_stuff(password):
    password = password.lower()  # Case-insensitive

    # Check for repeating characters (e.g., aaa, 111)
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            feedback.text += f"Repeating pattern found: '{password[i]*3}'\n"
            strength_password.value -= 20

    # Check for sequential characters (e.g., abc, 123)
    for i in range(len(password) - 2): # Used gpt for this
        a, b, c = password[i], password[i+1], password[i+2]
        if ord(b) == ord(a) + 1 and ord(c) == ord(b) + 1:
            feedback.text += f"Sequential pattern found: '{a + b + c}'\n"
            strength_password.value -= 15

    return False, ""

app = gp.GooeyPieApp("Password Checker") # Defines the stuff in app
app.set_size(WIDTH, HEIGHT) # Makes the app a certain size depending on the width and height
app.set_grid(ROWS, COLUMNS) # Makes a grid
app.set_icon("Green_tick.svg.png") # Sets the icon of the app


######################    Windows   ##################################

about_me_window = gp.Window(app, "About") # Creates a new window
about_me_window.height = 400 # Sets the height of the window
about_me_window.width = 200 # Sets the width of the window

#######################    Containers   ##########################

about_me_container = gp.Container(about_me_window) # Creates a new container
about_me_container.set_grid(3, 2) # Sets the grid of the container

info_lbl = gp.Label(about_me_container, "This is version 1 of Password Checker 9000,")
info_lbl2 = gp.Label(about_me_container, "It's meant to be a guide to help people understand how they can improve their passwords,") # Label
info_lbl3 = gp.Label(about_me_container, "Or create a strong password to see what else i have made check out my git hub page") # Label
git_hub_lbl = gp.Hyperlink(about_me_container, "Here!", "https://github.com/ollienunn")

about_me_container.add(info_lbl, 1, 1)
about_me_container.add(info_lbl2, 2, 1) # Adds the about me info to the container
about_me_container.add(info_lbl3, 3, 1) # Adds the about me info to the container
about_me_container.add(git_hub_lbl, 3, 2, align="left") # Adds the about me info to the container

#####################################################################
#######################    About Me Window   ########################

about_me_window.set_grid(2, 2) # Sets the grid of the window
int_lbl = gp.StyleLabel(about_me_window, "About the App") # Label
int_lbl.font_size = 20 # Font size
about_me_window.add(int_lbl, 1, 1, column_span = 2, align="center") # Adds the label to the window
about_me_window.add(about_me_container, 2, 1) # Adds the about me info to the window

########################    Requirments Window   ##########################

requirments_window = gp.Window(app, "Requirements") # Creates a new window
requirments_window.height = 400 # Sets the height of the window
requirments_window.width = 400 # Sets the width of the window
requirments_window.set_grid(2, 1) # Sets the grid of the window
requirments_lbl = gp.StyleLabel(requirments_window, "Requirments") # Label
requirments_lbl.font_size = 20 # Font size
requirments_info = gp.Label(requirments_window, "The requirements for a good password are,\n The length being above 10 characters, \n Having at least one uppercase letter,\n A special charactcer eg (#:!£$*),\n Numbers (123456789),\n NOT HAVING A PASSWORD USED IN A DATA BREACH.") # Label

requirments_window.add(requirments_lbl, 1, 1, align="center") # Adds the label to the window
requirments_window.add(requirments_info, 2, 1, align="center") # Adds the about me info to the window

######################################################################
############  WIDGETS  ###############

intro_lbl = gp.StyleLabel(app, "Password Checker 9000") # Label
intro_lbl.font_size = 20 # Font size
bout_me = gp.Label(app, "About") # Label
require_wind = gp.Label(app, "Requirments for the password") # Label
password_lbl = gp.Label(app, "Enter your password: ") # Label
password_inp = gp.Secret(app) # Makes the input dots
password_inp.width = 50 # Sets the size of the input
check_btn = gp.Button(app, "Check your password", check_password) # Button
feedback_lbl = gp.Label(app, "Feedback: ") # Label
feedback = gp.Label(app, "") # Text box for feedback
strength_password = gp.Progressbar(app) # Progress bar for the password strength

#######################################
########## Event Stuff ##########

check = gp.Checkbox(app, 'See password') # A checkbox to toggle the password
check.add_event_listener('change', toggle_mask) # Changes the password to a visible input
bout_me.add_event_listener('mouse_over', open_about_me_window) # Opens the about me window
require_wind.add_event_listener('mouse_over', open_requirements_window) # Opens the about me window

#################################
######## Adding Widgets to the app ########

app.add(require_wind, 1, 1, align="left") # Adds the requirments button to the app
app.add(intro_lbl, 1, 2, align="center") # Needed to show stuff on the app
app.add(bout_me, 1, 3, align="right") # Aligns the input to the center
app.add(password_lbl, 2, 1, align="center") # Aligns the input to the center
app.add(password_inp, 2, 2, fill = True)
app.add(check, 2, 3, align="center")
app.add(check_btn, 3, 1, align="center") # Aligns the button to the center
app.add(strength_password, 3, 2, fill = True, column_span = 2) # Adds the progress bar to the app
app.add(feedback_lbl, 4, 1, align="center") # Aligns the input to the center
app.add(feedback, 4, 2) # Adds the feedback input to the app#

###########################################
app.on_close(check_exit)

app.run() # Makes the app run 
# Finished app 