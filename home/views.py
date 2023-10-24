from django.shortcuts import render

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
    for i in raw_data:
        print(i.file.name)
    data=[[x.name,x.file.name,x.file.name[6:],x.added_by,x.date,x.file_size] for x in raw_data]
    return render(request,"index.html",{"data":data})

def file_list(request):
    files = Fyles.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        file=Fyles()
        file.name=request.POST["name"]
        file.added_by=request.POST["added_by"]
        file.file=request.FILES["myfile"].read()
        # myfile=FileSystemStorage()
        # myfile.save(file.file.name,file.file)
        # file_size=get_human_readable_file_size(str("media/")+str(file.file.name))
        file.file_size=""
        file.save()
        raw_data=Fyles.objects.all()
        data=[[x.name,x.file.name,x.file.name[6:],x.added_by,x.date,x.file_size] for x in raw_data]
        return render(request,"index.html",{"data":data})
    else:
        return render(request,"/")


