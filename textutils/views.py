from django.http import HttpResponse
from django.shortcuts import render

#funcions used inside function
def first_char_cap(x):
    if len(x) !=0:
        x = ' ' + x
        a,b = 0,[]
        for i in x:
            if i ==' ':
                b.append(a)
            a+=1
        x = list(x)
        for j in b:
            x[j+1] = x[j+1].upper()
        s = ''
        for i in x:
            s += i
        return s
    else:
        return x
    
#main functions
def index(request):
    return render(request,"index1.html")

def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.POST.get('removepunc','off')
    capitalizefirst = request.POST.get('capitalizefirst','off')
    newlineremove = request.POST.get('newlineremove','off')
    spaceremover = request.POST.get('spaceremover','off')
    upper = request.POST.get('upper','off')
    lower = request.POST.get('lower','off')

    if removepunc == 'on':
        punc = '''!@#$%^&*(){}[]:;""''<>?,./|\~`+-*/'''
        anz = djtext.strip(punc)
        params = {'purpose': 'Removed Punctuations','analyzed_text': anz,'input':djtext}
        djtext = anz

    if capitalizefirst == 'on':
        a = djtext
        anz = first_char_cap(a)
        params = {'purpose': 'capitalizefirst','analyzed_text': anz,'input':djtext}
        djtext = anz
        
    if newlineremove == 'on':
        anz = djtext.replace('\n','')
        params = {'purpose': 'newlineremove','analyzed_text': anz,'input':djtext}
        djtext = anz
        
    if spaceremover == 'on':
        anz = djtext.replace(" ","")
        params = {'purpose': 'spaceremover','analyzed_text': anz,'input':djtext}
        djtext = anz
        
    if upper == 'on':
        anz = djtext.upper()
        params = {'purpose': 'upper','analyzed_text': anz,'input':djtext}
        djtext = anz
    if lower == 'on':
        anz = djtext.lower()
        params = {'purpose': 'lower','analyzed_text': anz,'input':djtext}
        djtext = anz

    if (removepunc == 'off' and capitalizefirst == 'off' and newlineremove == 'off' and spaceremover == 'off' and upper == 'off' and lower == 'off'):
        anz = "(*-*)"
        params = {'purpose': 'Please select CheckBox operations!','analyzed_text': anz,'input':djtext}
    return render(request,"analyze.html",params)