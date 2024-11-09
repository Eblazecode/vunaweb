from django.shortcuts import render


# Create your views here.

# index page
def index(request):
    return render(request, 'index.html')


def book_category_landing(request):
    departments = [
        {
            "name": "Theology",
            "image_url": "images/cross.jpg",
            "link": "https://drive.google.com/drive/folders/1zD4bZnZ-sAsfkURm4Pa-VsGKr-Yfa4XT?usp=sharing",
            "type": "department"
        },
        {
            "name": "Software Engineering",
            "image_url": "images/software_dev.jpg",
            "link": "https://drive.google.com/drive/folders/1IXoVn1wC5rjkyUK_qjL99vjUZPo05CeA?usp=sharing",
            "type": "department"
        },
        {
            "name": "Computer Engineering",
            "image_url": "images/electel.jpg",
            "link": "https://drive.google.com/drive/folders/1oE6oAuAVkY6qiFb25dcV1dby9hjpCjpP?usp=sharing",
            "type": "department"
        },
        {
            "name": "Electronics Engineering",
            "image_url": "images/electbub.webp",
            "link": "https://drive.google.com/drive/folders/1e6VDc7wihvAOCzuAsvX9SWbHEwdD5b-I?usp=sharing",
            "type": "department"
        },
        {
            "name": "Chemistry Education",
            "image_url": "images/chemistry_edu.jpg",
            "link": "https://drive.google.com/drive/folders/1KK3Duw7iI1rSt6vQFFdA_tQ4gveLLDKj?usp=sharing",
            "type": "department"
        },
        {
            "name": "Physics Education",
            "image_url": "images/physics.jpg",
            "link": "https://drive.google.com/drive/folders/1KK3Duw7iI1rSt6vQFFdA_tQ4gveLLDKj?usp=sharing",
            "type": "department"
        },
        {
            "name": "Nursing Science",
            "image_url": "images/nursing.png",
            "link": "https://drive.google.com/drive/folders/1ir-kNxM5_3-NwzesEL-UxXG7m53J5b6n?usp=sharing",
            "type": "department"
        },
        {
            "name": "Medical Laboratory Science",
            "image_url": "images/medlab.jpg",
            "link": "https://drive.google.com/drive/folders/1ir-kNxM5_3-NwzesEL-UxXG7m53J5b6n?usp=sharing",
            "type": "department"
        }
    ]
    return render(request, 'departments.html', {"departments": departments})


# book category page
def book_category(request):
    return render(request, 'categories.html')


def journals(request):
    return render(request, 'journals.html')
