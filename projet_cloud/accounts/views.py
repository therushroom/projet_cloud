from django.shortcuts import render
from django.views.generic.base import TemplateView
import base64
import requests


class app(TemplateView):

    template_name = "app.html" # templates/home.html

def result(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        #base64.b64encode(stream.getvalue())
        x = request.FILES['image'].file
        img = base64.b64encode(x.getvalue())
        print(img)

        # tell him to give url of image in server 

        r = requests.post('http://127.0.0.1:5000', data={'image' : img})
        image = r.json()['path']

        return render(request, 'result.html', {'image': 'http://127.0.0.1:5000'+image})
    return render(request, 'result.html')
