from django.shortcuts import render
from .forms import FileForm
from .models import image
from PIL import Image
from PIL.ExifTags import TAGS
IMAGE_FILE_TYPES = ['jpg', 'jpeg']
def create_profile(request):
    form = FileForm()
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            user_pr = form.save(commit=False)
            user_pr.pic = request.FILES['pic']
            file_type = user_pr.pic.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                return render(request, 'errors.html')
            user_pr.save()
            # return render(request, 'details.html', {'user_pr': user_pr})
    images=image.objects.filter()
    context = {"form": form,"images":images}
    return render(request, 'create.html', context)

def storage(request, pk):
    images = image.objects.filter(id=pk)[0]
    # exif_data=get_exif(images.pic)
    return render(request,'storage.html',{"image":images})