import requests
from random import randint, sample

training_plan = {"Monday": {'Activity': '', 'Time': ''}, "Tuesday": 'Day off', "Wednesday": {'Activity': '', 'Time': ''}, "Thursday": 'Day off', "Friday": {'Activity': '', 'Time': ''}, "Saturday": 'Day off', "Sunday": 'Day off'}
activities = {"running": "10", "swimming": "15", "gym" : "20", "yoga": "25", "cycling": "20"}

url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

try:
    weight = input("Your weight [kg]: ")
    height = input("Your height [m]: ")
except:
    print("Invalid data!")

querystring = {"weight":weight,"height":height}

headers = {
    'x-rapidapi-key': "458c8852f8msh4da7f7cf71021bdp177d3fjsn1f3d90436f6c",
    'x-rapidapi-host': "body-mass-index-bmi-calculator.p.rapidapi.com"}

response = requests.request("GET", url, headers=headers, params=querystring)

BMI = response.json()
print("BMI: {}".format(BMI["bmi"]))

url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/weight-category"

querystring = {"bmi": BMI["bmi"]}

response = requests.request("GET", url, headers=headers, params=querystring)

weightCategory = response.json()
print("Weight category: {}".format(weightCategory['weightCategory']))

while True:
    try:
        time = int(input("Your time for training every day [minutes]: "))
        if time < 10:
            raise Exception("You need more than 10 minutes!")
        break
    except Exception as ex:
        print(ex)
    
time_multiplier = float(BMI["bmi"])/10

activity_list = sample(range(5), 3)

i = 0
for key, value in training_plan.items():
    if isinstance(value, dict):
        value['Activity'] = list(activities.keys())[activity_list[i]]
        value['Time'] = min(int(list(activities.values())[activity_list[i]]), time)
        i += 1

with open('file.txt', 'w') as file:
    for key, value in training_plan.items():
        file.write(key + '\n')
        if isinstance(value, dict):
            for key2, value2 in value.items():
                file.write(key2 + ": ")
                file.write(str(value2) + "\n")
            file.write("\n")
        else:
            file.write(value + "\n\n")