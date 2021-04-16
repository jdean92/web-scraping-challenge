from flask import Flask, render_template, redirect
from pymongo import MongoClient
import mission_to_mars

app = Flask(__name__)

mongo - MongoClient("mongodb://localhost:27017/scraped")


@app.route("/")
def home():
    scraped_knees = mongo.db.scraped_knees.find_one()
    return render_template("index.html", scraped=scraped_knees)

@app.route("/scrape")
def scrape():
    mission_scraped = mission_to_mars.mission_scraped()
    mongo.db.mission_scraped.update({}, mission_scraped, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)




