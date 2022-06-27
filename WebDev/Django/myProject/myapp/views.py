from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Quick service'
    feature1.istrue = True

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Elisa'
    feature2.details = 'It is just good'
    feature2.istrue = False

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Safe'
    feature3.details = 'No one can hack you'
    feature3.istrue = False

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Scalable'
    feature4.details = 'Scale to large enterprises'    
    feature4.istrue = True

    features = [feature1, feature2, feature3, feature4]
    return render(request, 'index.html', {'features' : features}) 

def counter(request):
    words = request.POST['text']
    word_count = len(words.split())
    return render(request, 'index.html')