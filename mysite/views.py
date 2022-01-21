# I have created this File -- Manually
from django.http import HttpResponse
from django.shortcuts import render


# ------  font editor section below


def index(request):
    return render(request, "index.html")


def removepunc(request):

    djtext = request.POST.get('text', 'default')
    righttick = request.POST.get('righttick', 'off')
    upper = request.POST.get('upper', 'off')
    extraspace = request.POST.get('extraspace', 'off')

    if righttick == 'on':
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~+“'''
        analyzed = ''
        for char in djtext:
            if char not in punc:
                analyzed += char
        params = {'purpose': "Removed Punctuations Text", 'analyzed_text': analyzed}
        return render(request, 'result.html', params)

    elif upper == 'on':
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': "Make it text upper case ", 'analyzed_text': analyzed}
        return render(request, 'result.html', params)

    elif extraspace == "on":
        analyzed = ''
        for i in range(len(djtext)):
            if djtext[i] == ' ' and djtext[i + 1] == ' ':
                pass
            else:
                analyzed += djtext[i]
        params = {'purpose': "Text after Extra spaces Removed", 'analyzed_text': analyzed}
        return render(request, 'result.html', params)

    else:
        return HttpResponse("<h3>ERROR ! you have not selected any option</h3>")


#  ----     font changer section below

def about(request):
    return render(request, "about.html")


def fontfunc(request):
    fontText = request.POST.get('fonttext', 'default')
    boldb = request.POST.get('bold', 'off')
    italicb = request.POST.get('italics', 'off')
    sofiab = request.POST.get('sofia', 'off')

    if boldb == 'on':
        vari = {'style': 'Bold', 'fontchange': fontText}
        return render(request, 'font.html', vari)

    elif italicb == 'on':
        vari = {'style': 'Italics', 'fontchange': fontText}
        return render(request, 'italic.html', vari)

    elif sofiab == 'on':
        vari = {'style': 'Sofia-Cursive', 'fontchange': fontText}
        return render(request, 'sofia.html', vari)
    else:
        return HttpResponse("<h3>ERROR ! you have not selected any option</h3>")
