from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_db"
mongo = PyMongo(app)

# Route to render index.html template using data from Mongo
@app.route("/")
def home():
    try:
    # Find one record of data from the mongo database
        marsData = mongo.db.mars_data.find_one()
    except:
        print("database timeout")
        return redirect("/", code=302)
        
    # Return template and data
    return render_template("index.html", marsData=marsData)
    


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():

    # Run the scrape function
    mars_data = scrape_mars.scrape_info()

    # Insert the record
    mongo.db.mars_data.update_one({}, {"$set": mars_data}, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)


if __name__ == "__main__":
    app.run(debug=True)
