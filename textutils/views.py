# This file was created by Sani. REMEMBER THIS!!!!!!!!!!!!!!!!

"""
To return a html file, do:
    i) go to settings.py, find the TEMPLATES and add 'templates' to the DIR list.
   ii) create a directory 'templates' in the base directory(the one containing manage.py).
  iii) add the html file to the 'templates' directory.
   iv) in the views.py, add the import(from django.shortcuts import render).
    v) in views.py, in the endpoint function, add code in the following syntax:
           return render(request, '<html file>')

The third argument for render can be a dictionary which can be accessed by the html file by {{ <key> }} syntax.
This is optional
   """
from django.shortcuts import render

def index(request):    # functions acc. to the endpoints in urls.py; don't forget the request parameter.
    dict = {'name':'Sani', 'place':'Surul'}
    return render(request, 'index.html', dict)    # do this for returning a html file


def analyze(request):
    #getting the text
    djtext = request.POST.get('text', 'default')    # get the text and the default value if text is unavailable.
    removepunc = request.POST.get('removepunc', 'default')    # get the text and the default value if text is unavailable.
    removespace = request.POST.get('removespace', 'default')
    ucase = request.POST.get('ucase', 'default')
    newlineremove = request.POST.get('newlineremove', 'default')
    exsprem = request.POST.get('exsprem', 'default')
    charcount = request.POST.get('charcount', 'default')
    linecount = request.POST.get('linecount', 'default')

    if removespace != "on" and removepunc != "on" and ucase != "on" and newlineremove != "on" and exsprem != "on" and \
            charcount != "on" and linecount != "on":

        return render(request, 'error.html')

    else:

        if removepunc == "on":
            punctuations = '''!:()-[]{};'"\,<>./?@#$%^&*_~'''
            analyzed = ""
            for char in djtext:
                if char not in punctuations:
                    analyzed = analyzed + char
            params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}

            djtext = analyzed

        if removespace == "on":
            Spaces = ''' '''
            analyzed = ""
            for chara in djtext:
                if chara not in Spaces:
                    analyzed = analyzed + str(chara)
            params = {'purpose':'Removed Spaces', 'analyzed_text':analyzed}
            djtext = analyzed

        if ucase == "on":
            analyzed = ""
            for charac in djtext:
                analyzed = analyzed + str(charac.upper())
            params = {'purpose':'Converted to UPPER CASE', 'analyzed_text':analyzed}
            djtext = analyzed

        if newlineremove == "on":
            analyzed = ""
            for chara in djtext:
                if chara != "\n" and chara != "\r":
                    analyzed = analyzed + str(chara)
            params = {'purpose':'Removed New Lines', 'analyzed_text':analyzed}
            djtext = analyzed

        if exsprem == "on":
            analyzed = ""
            for index, chara in enumerate(djtext):
                if not(djtext[index] == " " and djtext[index + 1] == " "):
                    analyzed = analyzed + str(chara)
            params = {'purpose':'Removed Extra Spaces', 'analyzed_text':analyzed}
            djtext = analyzed

        if charcount == "on":
            analyzed = str(len(djtext))
            params = {'purpose': 'Counted the Number of Characters', 'analyzed_text': analyzed}
            djtext = analyzed

        if linecount == "on":
            analyzed = 1
            for item in djtext:
                if item == "\n":
                    analyzed += 1
                elif djtext == "":
                    analyzed = 0
            params = {'purpose': 'Counted the Number of Lines', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')