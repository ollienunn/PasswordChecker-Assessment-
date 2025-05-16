import gooeypie as gp

WIDTH = 400
HEIGHT = 300
ROWS = 4
COLUMNS = 3

######  EVENTS  ######

def toggle_mask(event): # Toggles the password
    password_inp.toggle() # Makes the input visible or not

######################

######################
# Need a score system for the password,
#                                       speacial characters = + points
#                                       numbers = + points
#                                       length 10 + = + points  
#                                       mix of uppercase and lowercase = + points                                      
#                                       whether or not it is a common password = +- points      
#                                       if it has been pwnaed = - points
#                                       common letters = - points
######################

app = gp.GooeyPieApp("Password Checker") # Defines the stuff in app
app.set_size(WIDTH, HEIGHT) # Makes the app a certain size depending on the width and height
app.set_grid(ROWS, COLUMNS) # Makes a grid

########## Event Stuff ##########

check = gp.Checkbox(app, 'See password') # A checkbox to toggle the password
check.add_event_listener('change', toggle_mask) # Changes the password to a visible input

#################################


############  WIDGETS  ###############

intro_lbl = gp.StyleLabel(app, "Password Checker 9000") # Label
intro_lbl.font_size = 20 # Font size
password_lbl = gp.Label(app, "Enter your password: ") # Label
password_inp = gp.Secret(app) # Makes the input dots
password_inp.width = 50 # Sets the size of the input

#######################################

app.add(intro_lbl, 1, 2, align="center") # Needed to show stuff on the app
app.add(password_lbl, 2, 1, align="center") # Aligns the input to the center
app.add(password_inp, 2, 2) 
app.add(check, 2, 3, align="center")
app.add()

app.run() # Makes the app run