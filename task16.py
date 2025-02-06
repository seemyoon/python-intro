# Create another instance of the Post class and call 'like' method for it
# Check 'likes_qty' for both instances


class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author
        self.likes_qty = 0

    def like(self):
        self.likes_qty += 1


my_post = Post("My work", "Some post content", "Oleksandr")
my_post2 = Post("My roles", "Some post content", "Oleksandr")

my_post.like()
my_post.like()
my_post2.like()

print(my_post.likes_qty)
print(my_post2.likes_qty)
