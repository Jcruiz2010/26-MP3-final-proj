import requests

plan = []
 
def search_country():
    country = input("Enter the name of the country: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    request1 = requests.get(url)
    data = request1.json()[0]
    url2=f"https://api.open-meteo.com/v1/forecast?latitude={data["latlng"][0]}&longitude={data["latlng"][1]}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    request2= requests.get(url2)
    data2= request2.json()
   
  
    if request1.status_code == 200:
        
        
        currencies = ", ".join(data["currencies"].keys())
        languages = ", ".join(data["languages"].values())
        timezones = ", ".join(data["timezones"])
        
        print("\nInformation about contries")
        print("Official Name:", data["name"]["official"])
        print("Capital:", data["capital"][0])
        print("Region:", data["region"])
        print("Subregion:", data["subregion"])
        print("Population:", data["population"])
        print("Currency:", currencies)
        print("Languages:", languages)
        print("Timezones:", timezones)
        print("Country Code:", data["cca2"])
        print("Location:", data["latlng"])
        print("Weather:",data2["current"]["temperature_2m"])
        
 
    else:
        print("Country not found")
   
def add_country():
    try:
        country = input("Country: ")
        days = int(input("Days of stay: "))
        start_dia = int(input("Start day: "))
        if 1<= start_dia <=31:
            start_mes= int(input("Start month"))
            if  1<= start_mes <=12:
                
                start_year= int(input("Start year"))
                notes = input("Notes: ")
                start_date= f"{start_dia}/{start_mes}/{start_year}"
                trip_thingsidk = {
                    "country": country,
                    "days": days,
                    "start_date": start_date,
                    "notes": notes
                }
                plan.append(trip_thingsidk)
            
                print("\nTrip added!")
                print(f"{country} - {days} days - Start: {start_date} - Notes: {notes}\n")
            else:
                print("thats not a valid month")
        else:
            print("Thats not a valid day")
    except:
        print("An error has ocurred")
 
def show_trips():
    if not plan:
        print("No trips added yet.\n")
        return
 
    print("\nCurrent Trips")
    for p in plan:
        country = p["country"]
        days = p["days"]
        start = p["start_date"]
        notes = p["notes"]
 
        print(country + " - " + str(days) + " days - Start: " + start + " : Notes: " + notes)
 
 
def calculate_cost():
    total_dias = 0
 
    for guacamole in plan:
        total_dias = total_dias + guacamole["days"]
 
    total = (total_dias * 165) + (len(plan) * 75) + 30
 
    print("\nTotal Cost: $" + str(total) + "\n")
 
 
def save_trip():
    client = input("Client name: ")
 
    with open("trip.txt", "a") as file:
        file.append("Client: " + client + "\n")
        file.append("Trips:\n")
 
        for tripstuff in plan:
            country = tripstuff["country"]
            days = tripstuff["days"]
            start = tripstuff["start_dia"]
            notes = tripstuff["notes"]
 
            line = country + f" -  {str(days)}  days - Start:  {start}  - Notes:  {notes} \n"
            file.append(line)
 
    print("Trip saved\n")
 

def ui():
    while True:
        print("\n1. Search Country")
        print("2. Add Country to Trip")
        print("3. Show Trips")
        print("4. Calculate Cost")
        print("5. Save Trip")
        print("6. Exit")
 
        decision = input("Choose an option: ")
 
        if decision == "1":
            search_country()
        elif decision == "2":
            add_country()
        elif decision == "3":
            show_trips()
        elif decision == "4":
            calculate_cost()
        elif decision == "5":
            save_trip()
        elif decision == "6":
            print ("ya done ok? im sorry")
            break
        else:
            print("U can't do that yo\n")
 
ui()