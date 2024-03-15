from django.shortcuts import render,redirect,get_object_or_404
from .models import Themes

def themes_list(request):
    themes = Themes.objects.all()
    return render(request,'themes/themes.html',{'themes':themes})

def theme_detail(request,pk):
    theme = Themes.objects.get(id=pk)
    return render(request,'themes/themes_details.html',{'theme':theme})

def create_theme(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        image = request.FILES.get('image')
        if image:
            new_theme = new_theme = Themes(title=title,description1=description)
        else:
            new_theme = Themes(title=title, description=description, image=image)
        new_theme.save()
        return redirect('theme_detail',pk=new_theme.pk)
    else:
        return render(request,'themes/add_theme.html')

def edit_theme(request,pk):
    this_theme = get_object_or_404(Themes,pk=pk)
    if request.method == 'POST':
        this_theme.title = request.POST['title']
        this_theme.description = request.POST['description']
        image = request.FILES.get('image')
        if image:
            this_theme.image = image
        this_theme.save()
        return redirect('themes_list',pk=this_theme.pk)
    else:
        return render(request,'themes/edit_theme.html',{'theme':this_theme})

def delete_theme(request,pk):
    this_theme = get_object_or_404(Themes,pk=pk)
    if request.method == 'POST':
        this_theme.delete()
        return redirect('themes_list')
    return render(request,'themes/delete_theme.html',{'theme':this_theme})