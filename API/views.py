from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.http import FileResponse
import base64
from . import face_spec

# Create your views here.
def pageNotFound(request):
    return render(request, "404.html")

def dataUploadingForm(request):
    return render(request, "dataUploadingPage.html")

def processImages(request):
    try:
        face = request.FILES["face"]
        frame = request.FILES["frame"]
        fs = FileSystemStorage()
        face_url = fs.save(face.name, face)
        frame_url = fs.save(frame.name, frame)

        uploaded_face_url = fs.url(face_url)
        uploaded_frame_url = fs.url(frame_url)
        
        face_spec.process_image("."+uploaded_face_url, "."+uploaded_frame_url)
        
        # Clear storage
        fs.delete(face.name)
        fs.delete(frame.name)
    except:
        return render(request, "404.html")
    else:
        return HttpResponse(base64.b64encode(open("media/output.jpg", "rb").read()), content_type="image/png")

