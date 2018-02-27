from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import FileResponse
import base64
from . import face_spec
from .models import Image

# Create your views here.
def pageNotFound(request):
    return render(request, "404.html")

def dataUploadingForm(request):
    return render(request, "dataUploadingPage.html")

def processImages(request):
    face = request.FILES["face"]
    frame = request.FILES["frame"]

    Iface, created = Image.objects.get_or_create(image=face)
    Iframe, created = Image.objects.get_or_create(image=frame)
    

    # fs = FileSystemStorage()
    # face_url = fs.save(face.name, face)
    # frame_url = fs.save(frame.name, frame)
    # uploaded_face_url = settings.MEDIA_ROOT+"/"+face_url #fs.url(face_url)
    # uploaded_frame_url = settings.MEDIA_ROOT+"/"+frame_url  #fs.url(frame_url)
    
    # face_spec.process_image(face, frame)
    
    # # Clear storage
    # fs.delete(face.name)
    # fs.delete(frame.name)
    
    # img = open(settings.MEDIA_ROOT+"/"+outputname, "rb").read()
    absFace = settings.MEDIA_ROOT + "/" + str(Iface.image)
    absFrame = settings.MEDIA_ROOT + "/" + str(Iframe.image)

    output = face_spec.process_image(absFace, absFrame)
    # IOutput, created = Image.objects.get_or_create(image=output)

    # absOutput = settings.MEDIA_ROOT + "/" + str(IOutput.image)

    return HttpResponse(base64.b64encode(output), content_type="image/png")

