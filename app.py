import gooeypie as gp
import pwnedpasswords

WIDTH = 600
HEIGHT = 600
ROWS = 4
COLUMNS = 3

############ Classes (def) ############

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

        if len(password) < 6: # Checks the length of the password
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
                    break  # Only penalize once
            
            # Check if password has been pwned
            pwned_count = pwnedpasswords.check(password)
            print(f"Pwned count: {pwned_count}")  # This will print to the terminal

            if pwned_count > 0:
                feedback.text += f"Warning: This password has appeared in {pwned_count} data breaches!\n"
                strength_password.value -= 40


            #if password in clean_passwords or password in more_common_passwords:
            #    strength_password.value -= 10
            #    feedback.text += "Your password is one of the most common passwords change it to be more abstract\n"
            #else:
            #    return
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
            
            if strength_password.value == 100:
                feedback.text += "Your password is strong, Good Job\n"
                app.set_icon("Green_tick.svg.png") # Sets the icon of the app
            if strength_password.value == 80:
                feedback.text += "Your password is alright but it could be improved\n"
            if strength_password.value == 70:
                feedback.text += "Your password is better but don't include a common password\n"
                app.set_icon("Green_tick.svg.png") # Sets the icon of the app
            if strength_password.value == 60:
                feedback.text += "Look at the feedback then fix your password\n"
                app.set_icon("Cross.png") # Changes the icon to a red cross if the password is bad
            if strength_password.value == 40:
                feedback.text += "Listen to the feedback and try again\n"
                app.set_icon("Cross.png") # Changes the icon to a red cross if the password is bad
            if strength_password.value == 20:
                feedback.text += "Wow your password really sucks use the feedback you need it\n"
                app.set_icon("Cross.png") # Changes the icon to a red cross if the password is bad
 
            #if password in clean_passwords or password in more_common_passwords:
            #    strength_password.value -= 20
            #    feedback.text += "Your password is one of the most common passwords change it to be more abstract\n"
            #else:
            #    return
        elif len(password) > 25:
            feedback.text += "Your password is super long but strong hope you can remember it :)\n" # Adds to the feedback
            strength_password.value = 90
    
            f.close()
            r.close()

######################
# Need a score system for the password,
#                                                       
#                                       if it has been pwnaed = - points
#                                       common letters = - points
#
######################

app = gp.GooeyPieApp("Password Checker") # Defines the stuff in app
app.set_size(WIDTH, HEIGHT) # Makes the app a certain size depending on the width and height
app.set_grid(ROWS, COLUMNS) # Makes a grid
app.set_icon("Green_tick.svg.png") # Sets the icon of the app

######################    Windows   ##################################

about_me_window = gp.Window(app, "About") # Creates a new window
about_me_window.height = 400 # Sets the height of the window
about_me_window.width = 200 # Sets the width of the window

about_me_window.set_grid(2, 2) # Sets the grid of the window
int_lbl = gp.StyleLabel(about_me_window, "About the App") # Label
int_lbl.font_size = 20 # Font size
info_lbl = gp.Label(about_me_window, "This is version 1 of Password Checker 9000, it's meant to be a guide to help people understand how they can improve their passwords or create a strong password to see what else i have made check out my git hub page") # Label
git_hub_lbl = gp.Hyperlink(about_me_window, "Here", "https://github.com/ollienunn")
about_me_info = gp.Label(about_me_window, "" + str(info_lbl) + str(git_hub_lbl)) # Text box for the about me info

about_me_window.add(int_lbl, 1, 1, column_span = 2, align="center") # Adds the label to the window
about_me_window.add(info_lbl, 2, 1, align="right") # Adds the about me info to the window
about_me_window.add(git_hub_lbl, 2, 2, align="left") # Adds the about me info to the window

requirments_window = gp.Window(app, "Requirements") # Creates a new window
requirments_window.height = 400 # Sets the height of the window
requirments_window.width = 400 # Sets the width of the window
requirments_window.set_grid(2, 1) # Sets the grid of the window
requirments_lbl = gp.StyleLabel(requirments_window, "Requirments") # Label
requirments_lbl.font_size = 20 # Font size
requirments_info = gp.Label(requirments_window, "The requirements for a good password are,\n The length being above 10 characters, \n Having at least one uppercase letter,\n A special charactcer eg (#:!£$*),\n Numbers (123456789).\n") # Label

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

app.run() # Makes the app run