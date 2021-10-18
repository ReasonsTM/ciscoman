import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "UMJQAM2ARczPugr5QxhuhrncpWlgG9CQ" 

while True:
    
    orig = input ("MAPQUEST\n= = = =\nInput the required fields below and press enter. To exit the program, type Q, q, QUIT, or quit.\n\nInput Source City :")
    if orig == "quit" or orig == "q" or orig == "QUIT" or orig == "Q":
        break
    dest = input("Input Destination City :")
    if dest == "quit" or dest == "q" or orig == "QUIT" or orig == "Q":
        break
  
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    print ("URL ", (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    if json_status == 0:
        print ("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration: " + (json_data["route"]["formattedTime"]))
        print("Kilometers: " + str("{:.2f}".format(json_data["route"]["distance"] * 1.6)))
        
        print("Fuel Used (Ltr): " + str("{:.3f}".format(json_data["route"]["fuelUsed"]*3.78)))
        print("=============================================")
        print("Current Seasonal Road Closures: " + str(json_data["route"]["hasSeasonalClosure"]))
        print("Country Cross: " + str(json_data["route"]["hasCountryCross"]))
        print("Route has Highways?: " + str(json_data["route"]["hasHighway"]))
        print("Any Nearby Tollgate Roads? : " + str(json_data["route"]["hasTollRoad"]))
        print("Any Nearby Ferry Stations? : " + str(json_data["route"]["hasFerry"]))
        #print("LINK ➪ " + each["mapUrl"])
        #print("wawa : " + str(json_data["route"]["transportMode"]))
        #print("Real Time: " + str(json_data["route"]["turnType"]))

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")
    elif json_status == 402:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("**********************************************\n")
    elif json_status == 611:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("**********************************************\n")
    else:
        print("**********************************************************************")
        print("For Staus Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")