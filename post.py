import server
import datetime
import pymongo
from JSONEncoder import JSONEncoder

db = server.get_db()


def add(title, content, category):
    if db.ideas.find({"title": title, "content": content}).count() > 0:
        return "Duplicate post!"
    else:
        date = get_date(datetime.datetime.now())
        db.ideas.insert({"title": title, "content": content, "category": category, "date": date})
        add(category)
        return "Success!"


def get_all(category=None):
    """
    Gets all posts within a specified category
    :param category: the specified category (if empty, gets all posts)
    :return: array of posts
    """
    if category is None:
        doc = db.ideas.find()
    else:
        doc = db.ideas.find({"category": category})

    num_posts = doc.count()

    if num_posts > 0:
        doc = doc.sort("date", pymongo.DESCENDING)

        return return_posts(0, num_posts, doc)
    return "None"


def get_num(num_posts, category=None):
    """
    Gets a specific number of posts within a specified category
    :param num_posts: the specific number of posts
    :param category: the specified category (if empty, gets all posts)
    :return: array of posts
    """
    if category is None:
        doc = db.ideas.find()
    else:
        doc = db.ideas.find({"category": category})

    if num_posts > doc.count():
        num_posts = doc.count()

    if num_posts > 0:
        doc = doc.sort("date", pymongo.DESCENDING)

        return return_posts(0, num_posts, doc)
    return "None"


def get_range(start, end, category=None):
    """
    Gets a range of posts within a specified category
    :param start: the start of the range
    :param end: the end of the range
    :param category: the specified category (if empty, gets all posts)
    :return: array of posts
    """
    if category is None:
        doc = db.ideas.find()
    else:
        doc = db.ideas.find({"category": category})

    num_posts = doc.count()

    if end > num_posts:
        return "None"

    if num_posts > 0:
        doc = doc.sort("date", pymongo.DESCENDING)

        return return_posts(start, end, doc)
    return "None"


def return_posts(start, end, doc):
    posts = []
    for p in range(start, end):
        post = {"title": doc[p]["title"], "content": doc[p]["content"], "category": doc[p]["category"]}
        posts.append(post)
    posts = [JSONEncoder().encode(post) for post in posts]
    return posts


def get_date(entry):
    return entry.strftime("%c")


if __name__ == '__main__':
    add("new post1", "content", "category")
    array = get_all()
    for i in range(len(array)):
        print(array[i])
