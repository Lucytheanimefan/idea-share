import server

db = server.get_db()

categories = []


def init():
    global categories
    if (db.ideas.find({"_id": 0}).count() == 0):
        db.ideas.insert({"_id": 0, "title": "", "content": "", "category": "", "categories": []})
    categories = db.ideas.find({"_id": 0})[0]["categories"]


def add(category):
    global categories
    init()
    if category not in categories:
        print("hi")
        categories.append(category)
        db.ideas.update(
            {"_id": 0},
            {"$set": {"categories": categories}}
        )


def remove(category):
    global categories
    init()
    if category in categories:
        categories.remove(category)
        db.ideas.update(
            {"_id": 0},
            {"$set": {"categories": categories}}
        )


def get_all():
    if (db.ideas.find({"_id": 0}).count() == 0):
        return "None"
    else:
        return db.ideas.find({"_id": 0})[0]["categories"]