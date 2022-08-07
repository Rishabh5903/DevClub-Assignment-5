from django.shortcuts import render,HttpResponse
from .forms import Docs
from .models import file_upload
# Create your views here.
# def Documents(request):
#     if request.method == 'POST':
#         c_form = Docs(request.POST,request.FILES)
#         if c_form.is_valid():
#             name= c_form.cleaned_data['file_name']
#             files=c_form.cleaned_data['files']
#             file_upload(file_name=name,my_file=files).save()
#             return HttpResponse("file uploaded")
#         else:
#             return HttpResponse('error')
#     else:
#         context={
#             'form': Docs()
#         }
#         return render(request, 'Documents.html' ,context)
def show_file(request):
    all_data=file_upload.objects.all()
    context={
        'data':all_data
    }
    return render(request,'view.html',context)
