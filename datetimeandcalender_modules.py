"""from datetime import date,time,datetime
june = date.today()
print(june)
schedule = datetime.now()
print(schedule)"""

#activity 2
"""import time
import random
def randomd(startdate,enddate):
    print("printing random date between",startdate,"and",enddate)
    random_generator = random.random()
    date_format = "%m/%d/%Y"
    starttime = time.mktime(time.strptime(startdate,date_format))
    endtime = time.mktime(time.strptime(enddate,date_format))
    randomtime = starttime+random_generator*(endtime-starttime)
    randomdate = time.strftime(date_format,time.localtime(randomtime))
    return randomdate
print("Random date = ",randomd("6/1/2025","7/1/2025"))"""

#activity 3
def planeridecost(city):
    if city=="New York":
        return 180
    elif city=="Texas":
        return 220
    elif city=="Los Angeles":
        return 350
    else:
        raise ValueError("UNKOWN CITY")
def hotelcost(nights):
    return 500*nights
def carcost(days):
    cost = 40 * days
    if days >= 7:
        cost -= 50
    elif days >= 3:
        cost -= 20
    return cost
def tripcost(city,days,spendingmoney):
    return carcost(days)+hotelcost(days)+planeridecost(city)+spendingmoney
print("Cost for car rent ",carcost(20))
print("Cost of plane ride ",planeridecost("Texas"))
print("Cost of hotel room ",hotelcost(7))
print("Total cost of the trip ",tripcost("New York",10,5000))