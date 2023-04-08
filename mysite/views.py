# I have created this file - Meet
from django.http import HttpResponse 
from django.shortcuts import render

def index(request):
   
    return render(request, 'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    fullcap = request.POST.get('fullcaps','off')
    spaceremove = request.POST.get('spaceremover','off')
    newlineremove = request.POST.get('newlineremover','off')
    
    #analyze the text
    if (spaceremove == 'on'):
        analyzed= "";
        for index, char in enumerate(djtext):
            if djtext[index] ==" " and djtext[index+1] ==" ":
                pass
            else:
                analyzed = analyzed + char
        params={'purpose':'Upper Case', 'analyzed_text':analyzed}
        djtext = analyzed 
    if removepunc == 'on':

        punctuation = '''!"#$%&'()*+,-./:;<=>? @[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char;
        params={'purpose':'Removed Punctuation', 'analyzed_text':analyzed}
        djtext = analyzed

    if (fullcap == 'on'):
        analyzed= "";
        for char in djtext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Upper Case', 'analyzed_text':analyzed}
        djtext = analyzed    
    
    if (newlineremove == 'on'):
        analyzed= "";
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params={'purpose':'Upper Case', 'analyzed_text':analyzed}
        djtext = analyzed        

    return render(request, 'analyze.html', params)

