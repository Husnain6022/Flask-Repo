from flask import Flask, render_template
from post import Post
import requests


blog_posts = []
response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
blog_post = response.json()
for post in blog_post:
    post_object = Post(post['id'], post['title'], post['subtitle'], post['body'])
    blog_posts.append(post_object)



app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html", posts = blog_posts)


@app.route('/blog/<int:index>')
def show_post(index):
    blog = None
    for post in blog_posts:
        if post.id == index:
            blog = post
    return render_template("post.html", post=blog)

if __name__ == "__main__":
    app.run(debug=True)
