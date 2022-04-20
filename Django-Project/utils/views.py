from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #return HttpResponse("Helow World!")
    return render(request,'index.html')

def analyze(request):
    restext=request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','false')
    textupper = request.POST.get('textupper','false')
    removeline = request.POST.get('removeline','false')
    spaceremover = request.POST.get('spaceremover','false')
    charcount = request.POST.get('charcount','false')
    #analyzed= restext
    if removepunc == "on":
        punctuation = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in restext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)
    
    elif textupper == "on":
        analyzed=""
        for char in restext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'To UpperCase','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)

    elif removeline == "on":
        analyzed=""
        for char in restext:
            if char !='\n' and char !='\r':
                analyzed = analyzed + char
        params = {'purpose':'Remove Line Char','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)

    elif spaceremover == "on":
        analyzed=""
        for index,char in enumerate(restext):
            if not(restext[index]==" " and restext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose':'SpaceRemover','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)

    elif charcount == "on":
        count = 0
        for char in restext:
            if char:
                count +=1 
            analyzed = count
        params = {'purpose':'Char Count','analyzed_text':analyzed}
        return render(request,'analyzed.html',params)
    
    else:
        return HttpResponse('Error')

'''def captilizedsent(request):
    return HttpResponse("captilizedsent")

def newlineremover(request):
    return HttpResponse("newlineremover")

def spaceremover(request):
    return HttpResponse("spaceremover")

def charcount(request):
    return HttpResponse("charcount")'''