from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
import random
import markdown2

from . import util

class new_entry_form(forms.Form):
    title = forms.CharField(min_length=1, label="")
    content = forms.CharField(min_length=1, label="", widget = forms.Textarea)

def index(request):
    if request.method == "POST":
        
        if form.is_valid():
            entries = util.list_entries()
            s_entry = form.cleaned_data["search_string"]
            found_entries = []
            for entry in entries:
                if s_entry in entry:
                    if s_entry == entry:
                        return HttpResponseRedirect(f"/wiki/{entry}")
                    found_entries.append(entry)
            return render(request, "encyclopedia/search_result.html", {
                "entries" : found_entries,
                "entry" : s_entry
            })
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def new(request):
    if request.method == "POST" :
        form = new_entry_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title) == None:
                util.save_entry(title, content)
                return HttpResponseRedirect(f"/wiki/{title}")
            return render(request, "encyclopedia/new.html", {
                "form" : new_entry_form(request.POST),
                "err_found" : "Sorry, there's an existing page with this title"
            })
    return render(request, "encyclopedia/new.html", {
        "form" : new_entry_form(),
        "err_found" : ""
    })

def random_entry(request):
    return HttpResponseRedirect(f"/wiki/{random.choice(util.list_entries()) }")

def show_entry(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/err_not_found.html", {
            "entry" : entry
        })
    return render(request, "encyclopedia/entry.html", {
        "html_content" : markdown2.markdown(util.get_entry(entry))
    })