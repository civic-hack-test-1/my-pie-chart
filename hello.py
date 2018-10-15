from flask import Flask, request, render_template
from xml.dom import minidom
import pygal                                                       # First import pygal

app = Flask(__name__)

@app.route('/')
def charts():
    pie_chart = pygal.Pie()
    xmldoc = minidom.parse("open-data.xml")
    list = xmldoc.getElementsByTagName("EstablishmentDetail")
    rating_1 = 0
    rating_2 = 0
    rating_3 = 0
    rating_4 = 0
    rating_5 = 0
    no_rating = 0

    for n in list:
        type = n.getElementsByTagName("BusinessType")[0].firstChild.data
        if type == "Restaurant/Cafe/Canteen":
            rating = n.getElementsByTagName("RatingValue")[0].firstChild.data
            if rating == "1":
                rating_1 += 1
            if rating == "2":
                rating_2 += 1
            if rating == "3":
                rating_3 += 1
            if rating == "4":
                rating_4 += 1
            if rating == "5":
                rating_5 += 1
            if rating == "AwaitingInspection":
                no_rating += 1

    pie_chart.title = 'Restaurants and cafes in Durham'
    pie_chart.add('Rating 1', rating_1)
    pie_chart.add('Rating 2', rating_2)
    pie_chart.add('Rating 3', rating_1)
    pie_chart.add('Rating 4', rating_2)
    pie_chart.add('Rating 5', rating_1)
    pie_chart.add('Awaiting inspection', no_rating)

    chart = pie_chart.render_data_uri()
    return render_template( 'chart.html', chart = chart)

    @app.route("/data")
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
