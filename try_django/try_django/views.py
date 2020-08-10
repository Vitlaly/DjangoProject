from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

# Dont Repeat Yourself = DRY

def home_page(request):
   my_title = "Hello there ..."
   contex =  {'title': my_title}
   return render(request, 'home.html', contex)


def contact_page(request):
    print(request.POST)
    return render(request, 'form.html', {'title': 'Contact us'})

def about_page(request):
    return render(request, 'about.html', {'title': 'About us'})

def example_page(request):
    context = {"title": "example"}
    something_here = "hello.html"
    template_obj=get_template(template_name=something_here)

    return HttpResponse(template_obj.render(context))