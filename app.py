from flask import Flask, render_template, request, jsonify
import category
import os
import post
from JSONEncoder import JSONEncoder
import sys

app = Flask(__name__)

reload(sys)
sys.setdefaultencoding('utf-8')

@app.route("/")
def main():
	return render_template("index.html")


@app.route("/addNote", methods = ["POST"])
def add_note():
	print "Adding note"
	data = request.get_json()
	print data
	to_ret = post.add(data['title'], data['content'], data['category'])
	return to_ret



@app.route("/getNotes", methods = ["GET"])
def get_note():
	print "getting note"
	data = post.get_all()
	print data
	return jsonify(result=data)
	

@app.route("/getCategories", methods = ["GET"])
def get_categories():
	data = category.get_all()
	return jsonify(result=data)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
