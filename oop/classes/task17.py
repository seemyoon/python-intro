class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email


class Post:
    def __init__(self, title: str, content: str, author: User):
        self.title = title
        self.content = content
        self.author = author


class Forum:
    def __init__(self):
        self.users = []
        self.posts = []

    def register_user(self, username: str, email: str):
        user = User(username, email)
        self.users.append(user)
        return user

    def create_post(self, title: str, content: str, author: User):
        post = Post(title, content, author)
        self.posts.append(post)
        return post

    def find_user_by_username(self, username: str):
        for user in self.users:
            if user.username == username:
                return user

    def find_user_by_email(self, email: str):
        for user in self.users:
            if user.email == email:
                return user

    def find_post_by_user(self, user: User):
        found_posts = []
        for post in self.posts:
            if post.author == user:
                found_posts.append(post)
        return list(map(lambda found_post: found_post.title, found_posts))


forum = Forum()
oleksandr = forum.register_user("oleksandr001", "alexandrsemenec01@gmail.com")
ivan = forum.register_user("ivan132", "ivanivanov@gmail.com")

post_of_ivan = forum.create_post("my first post", "i love my car", ivan)
post_of_ivan2 = forum.create_post("my second post", "i love my milk", ivan)
post_of_oleksandr = forum.create_post("my first post", "i love my jib", oleksandr)

print(forum.posts[0].author.username)
print(forum.users[0].username)


print(forum.find_user_by_username("oleksandr001").email)

print(forum.find_post_by_user(ivan))

user_email = "alexandrsemenec01@gmail.com"
found_user = forum.find_user_by_email(user_email)

if found_user:
    print(forum.find_post_by_user(found_user))
else:
    print(f"User with email {user_email} doesn't exist")
