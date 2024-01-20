

Authorized_Users = {
    'ali': 12345,
    'Mohammad': 23455,
    'Mahdi': 214
}


def Authorised(func):
    def wrapper(username, password):

        if username in Authorized_Users.keys():
            if password == Authorized_Users[username]:
                return func(username, password)

        return 'not authorized'

    return wrapper


@Authorised
def get_blog(username, password):
    return f'this is your blog {username}'


@Authorised
def get_comment(username, password):
    return f'this is your comments {username}'


print(get_blog('Mohammad', 23455))

print(get_comment('ali', 12345))
