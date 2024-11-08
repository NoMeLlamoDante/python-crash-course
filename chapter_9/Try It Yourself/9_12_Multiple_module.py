#Admin:
# - admin class
# - privileges

#User:
# - users
from admin import Admin

privileges = ['can add post', 'can delete post', 
            'can ban user', 'can edit post']
evil = Admin("frank", 'sinatra',privileges)
evil.describe_user()
evil.privileges.show_privileges()