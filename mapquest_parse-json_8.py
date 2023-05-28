import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Santiago"
dest = "Ovalle"
key = "g84iu9qsJDEldynZWxI6o4NXucjVuiXW"

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print("URL: " + url)
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("=============================================")
        print("Direccion desde  " + orig + " hacia " + dest)
        print("Duracion del viaje : " + json_data["route"]["formattedTime"])
        print("Kilometros: {:.2f}".format((json_data["route"]["distance"]) * 1.61))
        
        fuel_used = json_data["route"].get("fuelUsed")
        if fuel_used:
            print("Combustible usado (Ltr): {:.2f}".format(fuel_used * 3.78))
        else:
            print("Combustible usado: No disponible")
        
        print("=============================================")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " ({:.2f}km)".format((each["distance"]) * 1.61))
        
        print("=============================================\n")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print(each["narrative"] + " ({:.2f}km)".format((each["distance"]) * 1.61))
        
        print("=====================================================\n")
        
    elif json_status == 402:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n")
        
    elif json_status == 611:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
        
    else:
        print("************************************************************************")
        print("For Staus Code: " + str(json_status) + "; Consulte:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
