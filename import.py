from xml.dom import minidom
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
        print ("%s %s %s" % (business, date, rating))
