from django.shortcuts import render, redirect
from django import forms
from django.core.files import File

from . import util
import random

class NewArticle(forms.Form):
    title = forms.CharField(label="Title")
    content = forms.CharField(label="Content", widget=forms.Textarea(attrs={'rows': 1, 'cols': 1}))

class EditArticle(forms.Form):
    content = forms.CharField(label="content", widget=forms.Textarea())

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def article(request, name):
    if name.lower() in (name.lower() for name in util.list_entries()):
        content = util.markdown_to_html(util.get_entry(name))
        return render(request, "encyclopedia/article.html", {
            "name": name,
            "entry": content
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "error": 'Article Not Found!'
        })

def new(request):
    if request.method == "POST":
        form = NewArticle(request.POST)
        
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            
            if title.lower() in (name.lower() for name in util.list_entries()):
                return render(request, "encyclopedia/error.html", {
                    "error": 'File with similar name already exists!'
                })
            else:
                with open(f'entries/{title}.md', 'w') as f:
                    myfile = File(f)
                    myfile.write(content)
                return redirect("article", name=title)
            # return redirect("index")
        else:
            form = NewArticle()    
            
    return render(request, "encyclopedia/new.html", {
        "form": NewArticle()
    })
    
def randp(request):
    name = random.choice(util.list_entries())
    return redirect("article", name=name)

def search(request):
    searched = request.GET['q']
    if searched.lower() in (name.lower() for name in util.list_entries()):
        return redirect("article", name=searched)
    else:
        results = [i for i in util.list_entries() if searched.upper() in i.upper()]
        return render(request, "encyclopedia/search.html", {
            "results": results
        })
        
def edit(request, name):
    if request.method == "POST":
        form = EditArticle(request.POST)
        
        if form.is_valid():
            new_content = form.cleaned_data["content"]
            
        with open(f'entries/{name}.md', 'w') as f:
                    myfile = File(f)
                    myfile.write(new_content)
        return redirect("article", name=name)    
    else:
        existing_content = util.get_entry(name)
        form = EditArticle({
            'content': existing_content,
        })
            
    return render(request, "encyclopedia/edit.html", {
        "form": form,
        "name": name
    })