from cProfile import label
from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "encyclopedia/newpage.html",{
        'form': AddPage(),
    }) 