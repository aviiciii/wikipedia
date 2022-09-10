from ast import Add
from cProfile import label
#from pyexpat.errors import messages
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from markdown2 import markdown
from . import util
from .forms import AddPage, EditPage


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def article(request, name):
    if request.method == 'POST':
        return redirect('encyclopedia:edit', name = name)

    entry = util.get_entry(name)
    if entry:
        return render(request, "encyclopedia/article.html",{
            "title":name,
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
            # get post data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["text"]

            # check if title already exists
            entries= util.list_entries()
            if title in entries:
                messages.error(request, f'Page named {title} already exists.')
                return redirect('encyclopedia:newpage')

            else:
                # added Heading(Title) to the content
                # content = f'# {title}\n\n' + content

                # save md in entries
                try:
                    util.save_entry(title, content)
                    messages.success(request, 'Page added successfully')
                    return redirect('encyclopedia:article', name = title)
                # some error while saving
                except:
                    messages.error(request, f'Some error occured while creating {title} page.')
                    return redirect('encyclopedia:newpage')
                
        return redirect('encyclopedia:newpage')

    return render(request, "encyclopedia/newpage.html",{
        'form': AddPage(),
    }) 


def edit(request, name):
    

    if request.method == 'POST':
        form = EditPage(request.POST)
        
        if form.is_valid():
            # get post data
            title = form.cleaned_data["title"]
            content = form.cleaned_data["text"]

            # verify title
            if title == name:
                # check if title already exists
                entries= util.list_entries()
                if title not in entries:
                    messages.error(request, f'Page named {title} doesn\'t exist.')
                    return redirect('encyclopedia:index')

                else:
                    # added Heading(Title) to the content
                    # content = f'# {title}\n\n' + content

                    # save md in entries
                    try:
                        util.save_entry(title, content)
                        messages.success(request, 'Page edited successfully')
                        return redirect('encyclopedia:article', name = title)
                    # some error while editing
                    except:
                        messages.error(request, f'Some error occured while editing {title} page.')
                        return redirect('encyclopedia:index')
        else:
            messages.error(request, f'Form invalid')
            return redirect('encyclopedia:index')

    else:
        entry = util.get_entry(name)
        form = EditPage()
        form.fields['title'].initial = name
        form.fields['text'].initial = entry
        
        if entry:
            return render(request, "encyclopedia/edit.html",{
                "title":name,
                "form": form,
            })
        else:
            messages.error(request, f'Page Not Found')
            return redirect('encyclopedia:index')