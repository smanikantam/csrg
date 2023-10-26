from django.shortcuts import render
from django.forms import FileField
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,FileResponse
from .models import Fyles
from django.core.files.storage import FileSystemStorage
import os

# Create your views here.
def convert_bytes(size):
    # Define the units and their respective scales
    units = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    for unit in units:
        if size < 1024.0:
            break
        size /= 1024.0
    return f"{size:.2f} {unit}"

def get_human_readable_file_size(file_path):
    if os.path.isfile(file_path):
        file_size = os.path.getsize(file_path)
        return convert_bytes(file_size)
    else:
        return "File does not exist."

def index(request):
    raw_data=Fyles.objects.all()
    data=[[x.name,x.added_by,x.date] for x in raw_data]
    return render(request,"index.html",{"data":data})

def file_list(request):
    files = Fyles.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        # form = FileUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     # Save the form data, which includes name, added_by, and the file
        #     form.save()

            # Create a new Fyles instance with all data
        file_model = Fyles(
            # file=request.FILES['myfile'],
            name=request.POST['name'],
            added_by=request.POST['added_by'],
        )

            # Save the Fyles instance with updated data
        file_model.save()

            # Retrieve and prepare data for rendering
        raw_data = Fyles.objects.all()
        data=[[x.name,x.added_by,x.date] for x in raw_data]
        return render(request,"index.html",{"data":data})
    else:
        return render(request, "/")
    return HttpResponse("Unexpected error")

def delete_entry(request):
    if request.method == 'POST':
        name=request.POST["deletion_name"]
        addedby=request.POST["deletion_addedby"]
        try:
            entries_to_delete = Fyles.objects.filter(name=name, added_by=addedby)
            for entry in entries_to_delete:
                entry.delete()
        except Fyles.DoesNotExist:
            pass 
        print("deletion success")
        raw_data = Fyles.objects.all()
        data=[[x.name,x.added_by,x.date] for x in raw_data]
        return render(request,"index.html",{"data":data})
    else:
        return render(request,"/")














