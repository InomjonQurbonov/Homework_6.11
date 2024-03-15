from django.shortcuts import render,get_object_or_404,redirect

from .models import Pupil



# Create your views here.
def pupils_list(request):
    if 'pupil' not in request.GET:
        pupils = Pupil.objects.all() # SELECT * FROM pupils;
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})
    else:
        pupils = Pupil.objects.filter(name__icontains=request.GET['pupil'])
        # SELECT * FROM pupils WHERE name LIKE '%str%';
        return render(request, 'pupils/pupils_list.html', {'pupils': pupils})


def pupils_detail(request, pk):
    pupil = Pupil.objects.get(id=pk)
    return render(request, 'pupils/pupil_info.html', {'pupil': pupil})

def create_pupil(request):
    if request.method == 'POST':
        name = request.POST['name']
        month_1 = request.POST['month_1']
        month_2 = request.POST['month_2']
        month_3 = request.POST['month_3']
        all_points = request.POST['all_points']
        image = request.FILES.get('image')
        if image:
            new_pupil = Pupil(name=name, month_1=month_1, month_2=month_2, month_3=month_3, all_points=all_points, image=image)
        else:
            new_pupil = Pupil(name=name, month_1=month_1, month_2=month_2, month_3=month_3, all_points=all_points)
        new_pupil.save()
        return redirect('pupil_info',pk=new_pupil.pk)
    else:
        return render(request,'pupils/add_pupil.html')

def edit_pupil(request, pk):
    this_pupil = get_object_or_404(Pupil, pk=pk)
    if request.method == 'POST':
        this_pupil.name = request.POST['name']
        this_pupil.month_1 = request.POST['month_1']
        this_pupil.month_2 = request.POST['month_2']
        this_pupil.month_3 = request.POST['month_3']
        this_pupil.all_points = request.POST['all_points']
        image = request.FILES.get('image')
        if image:
            this_pupil.image = image
        this_pupil.save()
        return redirect('pupil_info',pk=this_pupil.pk)
    else:
        return render(request,'pupils/edit_pupil.html',{'pupil':this_pupil})

def delete_pupil(request, pk):
    this_pupil = get_object_or_404(Pupil, pk=pk)
    if request.method == 'POST':
        this_pupil.delete()
        return redirect('pupils_list')
    return render(request, 'pupils/delete_pupil.html', {'pupil': this_pupil})