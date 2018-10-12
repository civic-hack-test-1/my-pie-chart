from flask import Flask
from xml.dom import minidom

app = Flask(__name__)
@app.route("/")

def hello():
    html = "<h1>Restaurants in Durham</h1>"

    xmldoc = minidom.parse("open-data.xml")
    list = xmldoc.getElementsByTagName("EstablishmentDetail")
    for n in list:
        business = n.getElementsByTagName("BusinessName")[0].firstChild.data
        rating = n.getElementsByTagName("RatingValue")[0].firstChild.data
        type = n.getElementsByTagName("BusinessType")[0].firstChild.data

        if rating == "AwaitingInspection":
            rating = "pending"

        if n.getElementsByTagName("RatingDate")[0].firstChild:
            date = n.getElementsByTagName("RatingDate")[0].firstChild.data
        else:
            date = "none"

        if type == "Restaurant/Cafe/Canteen":
            html += "<br/>"
            html += "<strong>" + business + "</strong> rated " + rating + " on " + date

    return html
