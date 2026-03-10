import requests
 
plan = []
 
def search_country():
    country = input("Enter the name of the country: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    request1 = requests.get(url)
 
    if request1.status_code == 200:
        data = request1.json()[0]
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
 
    else:
        print("Country not found")
   
def add_country():
    country = input("Country: ")
    days = int(input("Days of stay: "))
    start_dia = input("Start date: ")
    notes = input("Notes: ")
 
    trip_thingsidk = {
        "country": country,
        "days": days,
        "start_dia": start_dia,
        "notes": notes
    }
    plan.append(trip_thingsidk)
 
    print("\nTrip added!")
    print(f"{country} - {days} days - Start: {start_dia} - Notes: {notes}\n")
 
 
def show_trips():
    if not plan:
        print("No trips added yet.\n")
        return
 
    print("\nCurrent Trips")
    for p in plan:
        country = p["country"]
        days = p["days"]
        start = p["start_dia"]
        notes = p["notes"]
 
        print(country + " - " + str(days) + " days - Start: " + start + " : Notes: " + notes)
 
 
def calculate_cost():
    total_dias = 0
 
    for guacamole in plan:
        total_dias = total_dias + guacamole["days"]
 
    total = (total_dias * 165) + (len(plan) * 75) + 30
 
    print("\nTotal Cost: $" + str(total) + "\n")
 
 
def save_trip():
    pass
 

def ui():
    while True:
        print("1. Search Country")
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