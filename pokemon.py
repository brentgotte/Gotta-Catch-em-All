import json
import requests
import mysql.connector
Score = 1
mydb = mysql.connector.connect(
  host="localhost",
  user="bit_academy",
  password="bit_academy",
  database="python_novice"
)
sql = 'INSERT INTO `python_novice`.`pokemon` (`ID`, `name`, `weight`, `height`) VALUES (%s, %s, %s, %s)'


for x in range(1,151):
    link = requests.get("https://pokeapi.co/api/v2/pokemon/" + str(Score))
    linkjson = json.loads(link.text)
    Score+=1
    name = linkjson['name']
    weight = linkjson['weight']
    height = linkjson['height']
    mycursor = mydb.cursor()
    mycursor.execute(sql,  (x, name, weight, height))
    mydb.commit()
print(mycursor.rowcount, "geslaagd!")
