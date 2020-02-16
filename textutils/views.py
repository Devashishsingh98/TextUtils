from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def analyze(request):
    dj_text = request.POST.get("dj_text")
    count = 0
    temp_text = ""

    remove_punc = request.POST.get("remove_punc", "off")
    fullcaps = request.POST.get("fullcaps")
    newlineremover = request.POST.get("newlineremover")
    charcounter = request.POST.get("charcounter")

    if remove_punc == "on":
        for char in dj_text:
            if char not in """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~""":
                temp_text += char
        dj_text = temp_text
        
    
    if fullcaps == "on":
        dj_text = dj_text.upper()
        

    if newlineremover == "on":
        dj_text = dj_text.replace("\n", "")
        dj_text = dj_text.replace("\r", "")
    
    if charcounter == "on":
        count = len(dj_text) - dj_text.count("\n") + dj_text.count("\r")
        dj_text += "  {}".format(count)

    return render(request, "result.html", {"result_text":dj_text})