import server
import datetime
import pymongo
from JSONEncoder import JSONEncoder

db = server.get_db()


def add(title, content, category):
    if (db.ideas.find({"title": title, "content": content}).count() > 0):
        return "Duplicate post!"
    else:
        date = get_date(datetime.datetime.now())
        db.ideas.insert({"title": title, "content": content, "category": category, "date": date})
        return "Success!"

def get(num_posts, category):
    print "in get"
    if (db.ideas.find({"category": category}).count() > 0):
        doc = db.ideas.find({"category": category}).sort("date", pymongo.DESCENDING)

        if num_posts > db.ideas.find({"category": category}).count():
            num_posts = db.ideas.find({"category": category}).count()

        posts = []
        for p in range(num_posts):
            post = {"title": doc[p]["title"], "content": doc[p]["content"], "category": doc[p]["category"]}
            posts.append(post)

            
        posts = [JSONEncoder().encode(post) for post in posts]
        return posts
    else:
        return "None"

def get_date(entry):
    return entry.strftime("%c")


if __name__ == '__main__':
    add("new post1", "content", "category")
    array = get(2, "category")
    for i in range(len(array)):
        print(array[i])