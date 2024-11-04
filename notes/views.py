from audioop import reverse
from lib2to3.fixes.fix_input import context
from pyexpat.errors import messages
from unicodedata import category

from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Category, Note


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    # note_list =[
    #      Note(title='lesson 32', text='pending', reminder='done by today'),
    #      Note(title='lesson 33', text='pending', reminder='done by today'),
    #      Note(title='lesson 34', text='pending', reminder='done by today'),
    #      Note(title='lesson 35', text='pending', reminder='done by today'),
    # ]
    # Note.objects.bulk_create(note_list)
    notes_data = Note.objects.all()
    return render(request, 'notes/index.html', {'notes_data': notes_data})


def add(request: HttpRequest) -> HttpResponse:
    return render(request, 'notes/add.html')

# def list_notes(request: HttpRequest) -> HttpResponse:
#    notes = Note.objects.all()
#    return render(request, 'notes/list.html', {'notes': notes})
def list_notes(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        note_title = request.POST['title']
        note_text = request.POST['text']
        note_reminder = request.POST['reminder']
        category_title = request.POST['category']
        #create category first
        category_title = Category.objects.create(title=category_title)
        # create a new note using Note model
        note = Note(title=note_title, text=note_text, reminder=note_reminder, category=category_title)

        note.save()
        ##collect note from db and list them on list.html
        notes = Note.objects.all()
        return render(request, 'notes/list.html', {'notes': notes})

    else:
        context = 'something went wrong ! please add again!'
        return render(request, 'notes/add.html', context)

def edit_note(request: HttpRequest, id: int) -> HttpResponse:
    note = Note.objects.get(pk=id)

    if request.method == 'POST':
        note_title = request.POST['title']
        note_text = request.POST['text']
        note_reminder = request.POST['reminder']
        category_title = request.POST['category']

        category_title = Category.objects.create(title=category_title)

        # update  a new note using Note model
        note.title = note_title
        note.text = note_text
        note.reminder = note_reminder
        note.category = category_title
        note.save()
        notes = Note.objects.all()
        return render(request, 'notes/list.html', {'notes': notes})
    else:
        context = {'note': note}
        return render(request, 'notes/edit.html', context)

def delete_note(request: HttpRequest, id:int) -> HttpResponse:
    note = Note.objects.get(pk=id)
    if request.method == 'POST':
        note.delete()
        return redirect('note:add')
    return HttpResponse('Deleted successfully')



