from django.shortcuts import render
from django.forms import FileField
from django.views.decorators.csrf import csrf_exempt

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
        # Use the form to handle file upload
        form = Fyles.FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data
            form.save()

            # Get the uploaded file and other relevant data
            uploaded_file = form.cleaned_data['file']
            name = form.cleaned_data['name']
            added_by = form.cleaned_data['added_by']

            # You can calculate file size or perform other operations here
            file_size = ""  # Calculate or set the file size as needed

            # Create a new Fyles instance with all data
            file_model = Fyles(
                name=name,
                date=None,  # Auto-generated date
                added_by=added_by,
                file=uploaded_file,
                file_size=file_size
            )

            # Save the Fyles instance with updated data
            file_model.save()

            # Retrieve and prepare data for rendering
            raw_data = Fyles.objects.all()
            data = [[x.name, x.file.name, x.file.name[6:], x.added_by, x.date, x.file_size] for x in raw_data]

            return render(request, "index.html", {"data": data})
    else:
        form = Fyles.FileUploadForm()
        return render(request, "upload_file.html", {"form": form})
# Please note that this code saves the uploaded file through the form and then creates a new Fyles instance with the additional data before saving it.








