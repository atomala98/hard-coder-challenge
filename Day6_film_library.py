import requests

url = "https://imdb8.p.rapidapi.com/title/auto-complete"

querystring = {"q":input("Choose film name:")}

headers = {
    'x-rapidapi-key': "458c8852f8msh4da7f7cf71021bdp177d3fjsn1f3d90436f6c",
    'x-rapidapi-host': "imdb8.p.rapidapi.com"}

response = requests.request("GET", url, headers=headers, params=querystring)

json_resp = response.json()

films = {}
for i in range(min(5, len(json_resp['d']))):
    films[json_resp['d'][i]['l']] = {}


url = "http://www.omdbapi.com/?apikey={}&".format("e402b14c")

for key in films:
    params = {"t": key}

    response = requests.request("GET", url, params=params)
    json_resp = response.json()
    try:
        print(json_resp['Title'])
        print("Year of production: " + json_resp['Year'])
        print("Genre: " + json_resp['Genre'])
        print("Plot: " + json_resp['Plot'])
        print("IMDB Rating: " + json_resp['imdbRating'])
        print("Length: " + json_resp['Runtime'])
        print("Starring:")
        for i in json_resp['Actors'].split(", "):
            print(i)
        print('\n')
    except:
        pass