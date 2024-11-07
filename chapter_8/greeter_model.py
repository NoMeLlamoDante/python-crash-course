import greeter_functions
from greeter_functions import greet_users
from greeter_functions import greet_users as gs
import greeter_functions as gf
from greeter_functions import *

usernames = ['hannah', 'ty', 'margot']


greeter_functions.greet_users(usernames)
greet_users(usernames)
gs(usernames)
gf.greet_users(usernames)