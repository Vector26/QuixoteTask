from django.shortcuts import render
from .forms import FileForm
from task import settings
from .models import image
from PIL import Image
from PIL.ExifTags import TAGS
IMAGE_FILE_TYPES = ['jpg', 'jpeg','png']
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
            # exif_data=get_exif(f"MEDIA_ROOT/{user_pr.pic}")
            return render(request, 'details.html', {'user_pr': user_pr})
    images=image.objects.filter()
    context = {"form": form,"images":images}
    return render(request, 'create.html', context)

def get_exif(fn):
    ret = {}
    Img = Image.open(fn)
    # info_ = Img._getexif()
    # if(info_==None):
    #     info_=Img.info
    info=dict()
    info["EXIF"] = Img._getexif()
    info["Filename"]=Img.filename
    # Getting the format of image
    info["Format"]=Img.format
    # Getting the mode of image
    info["Mode"]=Img.mode
    # Getting the size of image
    info["Size"]=Img.size
    # Getting only the width of image
    info["Width"]=Img.width
    # Getting only the height of image
    info["Height"]=Img.height
    # Getting the color palette of image
    info["Image Palette"]=Img.palette
    return info

def storage(request, pk):
    images = image.objects.filter(id=pk)[0]
    exif_data = get_exif(f"{settings.MEDIA_ROOT}\\{images.pic}")
    print(f"{settings.MEDIA_ROOT}\\{images.pic}")
    exif_data=get_exif(images.pic)
    if(exif_data==None):
        exif_data="No Exif Data"
    return render(request,'storage.html',{"image":images,"exif":exif_data})