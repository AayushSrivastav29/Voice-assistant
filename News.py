import requests 
from ss import *

api_address="https://newsapi.org/v2/top-headlines?country=in&apiKey=f90668b3283c4521aa0be2247ec49e59"
json_data= requests.get(api_address).json()

def news():
    for i in range(3):
       ar.append("Number "+str(i+1)+" "+ json_data["articles"][i]["title"]+".")
    
    return ar

