from django.shortcuts import render
import requests
import json
# Create your views here.

def display_wheather(request):   
    # print(data.text)
    # whather_data = data.text
    # json_data = json.loads(data.text)
    # print(json_data)
    return render(request,"index.html")


def get_wheather_data(request):
    '''GET input from user and display wheather data based on it '''

    if request.method == 'POST':
        print("in get wheather data api")
        order_stat = request.POST["stat"]
        # year_order_stat =request.POST["year_order_stat"]
        region = request.POST["region"]
        parameter =request.POST["parameter"]
        print(region)
        print(parameter)
        print(order_stat)
        BASE_URL = "https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/"
        CALL_URL = BASE_URL + parameter + "/" + order_stat +"/" + region +".txt"
        data = requests.get(CALL_URL) #GET API call with requests module
        whather_data = data.text
        return render(request, "display_wheather.html", {"whather_data": whather_data})
      

