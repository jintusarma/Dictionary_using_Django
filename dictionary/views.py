from django.shortcuts import render
import requests
from .models import DictionaryEntry
from datetime import date, datetime
now = datetime.now()

cal = date.today()

# Create your views here.
def home(request):
    return render(request,"index.html",{'cal':cal})

def submit(request):
    if request.method == 'POST':
        text = str(request.POST['input'])
        print(text)
        url = "https://api.dictionaryapi.dev/api/v2/entries/en/"+text

        meaning = requests.get(url).json()
        textMeaning = str(meaning[0]['meanings'][0]['definitions'][0]['definition'])

        # textMeaning = "SUCCESS"
        output = {"word":text,"meaning":textMeaning,"cal":cal}
        DictionaryEntry.objects.create(input_word=text, output_word=textMeaning)

    else:
        print("no")
        entries = DictionaryEntry.objects.all()


    
    return render(request,"result.html",output)
