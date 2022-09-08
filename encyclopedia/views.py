from django.http import HttpResponse
from django.shortcuts import render
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    entry = util.get_entry(name)
    
    if entry:
        print(markdown(entry))
        return render(request, "encyclopedia/article.html",{
            "article": markdown(entry)
        })