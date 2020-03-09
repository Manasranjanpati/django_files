from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy

from .forms import PdfForm
from .models import Pdf


class Home(TemplateView):
    template_name = 'home.html'

def pdf_list(request):
    pdf = Pdf.objects.all()
    return render(request, 'pdf_list.html', {
        'pdf': pdf
    })


def upload_pdf(request):
    if request.method == 'POST':
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pdf_list')
    else:
        form = PdfForm()
    return render(request, 'upload_pdf.html', {
        'form': form
    })


def delete_pdf(request, pk):
    if request.method == 'POST':
        pdf = Pdf.objects.get(pk=pk)
        pdf.delete()
    return redirect('pdf_list')
