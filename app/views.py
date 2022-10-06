from django.shortcuts import render, redirect
from .forms import CandidateForm
from django.contrib import messages

def home(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Record saved successfully !")
            return redirect('/')
        else:
            messages.error(request, "Invalid form field")
    else:
        form = CandidateForm()
    context={'form': form,}
    return render(request, 'app/home.html', context)
