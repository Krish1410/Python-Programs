from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    djtext=request.POST.get('text','')
    char=0
    param={}
    if djtext=='':
        char=0
    else:
        for index,char in enumerate(djtext):
            char=index+1
            param={'char': char}
        
    return render(request,'index.html',param)

def analyze(request):
    djtext=request.POST.get('text','default')
    romovepunch=request.POST.get('removepunch','off')
    fullcaps=request.POST.get('fullcap','off')
    newlineromover=request.POST.get('newlineromover','off')
    extraspaceromover=request.POST.get('extraspaceromover','off')
    numberremove=request.POST.get('numberremove','off')

    removeText=request.POST.get('removeText','off')
    textForRemove=request.POST.get('textForRemove','off')
    char=0

    for index,char in enumerate(djtext):
        char=index+1
    
    params={}
    if romovepunch == 'on':
        Punctuation='''!()=[]{};:'"\,<>/?@#$%^-&*_?|~'''
        analyzed=""
        chars=0
        for index,char in enumerate(djtext):
                if char not in Punctuation:
                    analyzed+=char
                    chars=index+1
        djtext=analyzed
        params={'purpose' : 'Remove Punctuation' , 'analyzed_text' : analyzed,'char':chars}
    if fullcaps =='on':
        chars=0
        analyzed=""
        for index,char in enumerate(djtext):
            chars=index+1
            analyzed+=char.upper()
        djtext=analyzed
        params={'purpose' : 'Changed to Upper Case' , 'analyzed_text' : analyzed,'char':chars}
    if newlineromover=='on':
        chars=1
        analyzed=""
        for index,char in enumerate(djtext):
            if char != '\n' and char!='\r':
                analyzed+=char                
                chars=index+1
        djtext=analyzed

        params={'purpose' : 'Remove new Line' ,
                'analyzed_text' : analyzed,
                'char':chars}      
    if extraspaceromover=='on':
        chars=1
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed+=char
                chars=index+1
        djtext=analyzed
        params={'purpose' : 'Remove Extra Space' ,
                'analyzed_text' : analyzed,
                'char':chars} 
    if numberremove == 'on':
        numbers='''1234567890'''
        analyzed=""
        chars=0
        for index,char in enumerate(djtext):
                if char not in numbers:
                    analyzed+=char
                    chars=index+1
        djtext=analyzed
        params={'purpose' : 'Remove Punctuation' , 'analyzed_text' : analyzed,'char':chars}
    if removeText == 'on':
        text=f'''{textForRemove}'''
        # text=str(textForRemove)
        analyzed=""
        chars=0
        for index,char in enumerate(djtext):
                if char not in text:
                    analyzed+=char
                    chars=index+1
        djtext=analyzed
        print(text)
        params={'purpose' : 'Remove '+text , 'analyzed_text' : analyzed,'char':chars}
    if removeText != 'on' and romovepunch!='on' and fullcaps!='on' and newlineromover!='on' and extraspaceromover!='on' and numberremove!='on':
        return HttpResponse('<h1>ERROR</h1><h3>You Are not select a opshions</h3>')
    
    return render(request,'analyze.html',params)


def Notes(request):
    return render(request,'notes.html')
