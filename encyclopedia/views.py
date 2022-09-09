from ast import Add
from cProfile import label
#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from .forms import AddPage


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    entry = util.get_entry(name)
    if entry:
        return render(request, "encyclopedia/article.html",{
            "title":name.capitalize(),
            "article": markdown(entry)
        })
    else:
        return render(request, "encyclopedia/article.html",{
            "article": "None"
        })

def newpage(request):
    if request.method == 'POST':
        form = AddPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            text = form.cleaned_data["text"]
            print(title,text)
            messages.success(request, 'Page added successfully')
            return redirect('encyclopedia:newpage')

    return render(request, "encyclopedia/newpage.html",{
        'form': AddPage(),
    }) 