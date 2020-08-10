from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm
#
# def blog_post_detail_page(request, slug):
#     # queryset = BlogPost.objects.filter(slug=slug)  # query->data base->data->django render it
#     # if queryset.count() ==0:
#     #     raise Http404
#     # obj = queryset.first()
#     obj = get_object_or_404(BlogPost, slug=slug)
#     template_name = "blog_post_detail.html"
#     context = {"object": obj}
#     return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()  #queryset-> list of python objects
    context = {"object_list": qs}
    template_name = "blog/list.html"
    return render(request, template_name, context)

def blog_post_create_view(request):
    # for creating objects we need using a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        # obj = BlogPostModelForm.objects.create(**form.cleaned_data)
        obj = form.save(commit=False)
        obj.save()
        form= BlogPostModelForm()
    context = {"form": form}
    template_name = "form.html"
    return render(request, template_name, context)


def blog_post_detail_view(request, slug):
    # this is 1 object->detail view
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    template_name = "blog/detail.html"
    return render(request, template_name, context)

def blog_post_update_view(request,slug):
    # this is 1 object
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj, "form": None}
    template_name = "blog/update.html"
    return render(request, template_name, context)


def blog_post_delete_view(request, slug):
    # this is 1 object
    obj = get_object_or_404(BlogPost, slug=slug)
    context = {"object": obj}
    template_name = "blog/delete.html"
    return render(request, template_name, context)