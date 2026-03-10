import requests
 
plan = []
 
def search_country():
    country = input("Enter the name of the country: ")
    url = f"https://restcountries.com/v3.1/name/{country}"
    request1 = requests.get(url)
 
    if request1.status_code == 200:
        pass

    else:
        pass
   
def add_country():
    pass
 
 
def show_trips():
    pass
 
 
def calculate_cost():
    pass
 
 
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