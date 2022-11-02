import requests
import json
import Location
from flask import Flask, jsonify



# class Location:
#     def __init__(self, name, rating, vicinity):
#         self.name = name
#         self.rating = rating
#         self.vicinity = vicinity

type = ["restaurant","tourist_attraction","shopping_mall"]


app = Flask(__name__)
@app.route("/")
def createTravelPackage():
    travelPackage = [] #list of dictonaries
    for i in range(3):
        response = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?&location=35.308651%2C-80.733818&radius=1500&type={type}&key=AIzaSyBidFEd-ENRWOQbxLyECss8RkxI2seu8kc".format(type=type[i]))
        data = response.json()
        travelPackage.append({"name": data['results'][i]['name'], "rating":  data['results'][i]['rating'], "vicinity:": data['results'][i]['vicinity']})
    return jsonify(travelPackage)

if __name__ == '__main__':
    app.run(debug=True) 
# print(travelPackage[2])























#create api that takes in the json response and spits out an arraylist with good choices
#api should confirm that the restraunt is open and fits distance critera(distance critera can be filled within the api request) along with highly rated
    #also considers price_level


#for rn choose the first object in json
    #later we will convert the api response to a binary tree and use a search algorhitm to make an informed decision about the best location



#get iterniary as a dict (then we can use flask to return that dict as json)

