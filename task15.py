# 1. Assignment: Implement a decorator to check authentication
# Write a check_user_auth decorator that will check if the user is authenticated before executing a protected function.
# 2. Code requirements:
# Create a function check_user_auth(fn) that will:
#
# Check if the user is authenticated via is_user_authenticated().
# If the user is authenticated, execute the original function.
# If not authenticated, throw an Exception("User is not authenticated") exception.
# Use a wrapper function inside check_user_auth.
# Create an is_user_authenticated() function that returns True or False, simulating an authentication check.
#
# Create 3 protected functions that accept login and password and then:
#
# Output a message that the task has been completed.
# Should be secured with @check_user_auth.
# Test the code by calling all three functions with different data.


def is_user_authenticated():
    return [
        {"login": "user1", "password": "password123"},
        {"login": "admin", "password": "admnpss"},
        {"login": "user1", "password": "securepass"},
    ]


def check_user_auth(fn):
    def wrapper(*args, **kwargs):
        try:
            data = [
                user
                for user in is_user_authenticated()
                if user["login"] == kwargs["login"]
                and user["password"] == kwargs["password"]
            ]
            if data:
                return fn(*args, **kwargs)
            else:
                raise Exception("User is not authenticated")
        except Exception as e:
            print(e)

    return wrapper


@check_user_auth
def access_manager(login, password):
    print(f"User {login} has accessed")


@check_user_auth
def access_admin_panel(login, password):
    print(f"User {login} has accessed")


@check_user_auth
def access_registered_user(login, password):
    print(f"User {login} has accessed")


access_manager(login="user1", password="password123")
access_admin_panel(login="admin", password="adminpass")
access_registered_user(login="user2", password="securepass")
