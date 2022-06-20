
from django.http import HttpResponse
from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    return render(request,"index.html")

def submit(request):
    text = str(request.GET['input'])
    url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text

    meaning = requests.get(url).json()
    textMeaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition'])

    # textMeaning = "SUCCESS"
    return render(request,"result.html",{'meaning':textMeaning})
