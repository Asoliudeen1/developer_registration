
from django.shortcuts import render, redirect
from .forms import CandidateForm
from django.contrib import messages
from .models import candidate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404


def Login(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in!")
        return redirect('candidates')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('candidates')
        else:
            messages.error(request, 'Username or Password does not exist')
            
    return render(request, 'registration/login.html')


def register(request):
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
    return render(request, 'app/register.html', context)


def home(request):
    
    form = CandidateForm()
    context={'form': form,}
    return render(request, 'app/home.html', context)



@login_required(login_url='loginpage')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Candidates(request):
    candidates = candidate.objects.all()
    context={'candidates': candidates,}
    return render(request, 'app/candidates.html', context)


@login_required(login_url='loginpage')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Candidate(request, candidate_id):
    candidateObj = get_object_or_404(candidate, id=candidate_id)

    form = CandidateForm(instance=candidateObj)
    context={'form': form,}
    
    # DISABLE ALL THE FORM FIELDS
    fields_list = ['experience', 'gender', 'first_name', 'last_name', 'job', 'email',
                'phone', 'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'frameworks', 
                'languages', 'databases', 'libraries', 'mobile', 'others','message' ,'status_course',
                'started_course','finished_course','course','institution','about_course','started_job',
                'finished_job','company','position','about_job','employed','remote','travel']
    
    for field in fields_list:
        form.fields[field].disabled=True
        form.fields['file'].widget.attrs.update({'style':'display: none'})
        form.fields['image'].widget.attrs.update({'style':'display: none'})
    return render(request, 'app/candidate.html', context)


def Logout(request):
    logout(request)
    return redirect('/')