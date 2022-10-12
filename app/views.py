
from django.shortcuts import render, redirect, HttpResponse
from .forms import CandidateForm
from django.contrib import messages
from .models import candidate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
# COncatenate (F-Name and L-name)
from django.db.models.functions import Concat  
from django.db.models import Value as p

#Export to PDF
import pdfkit



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
    # FILTER
    if request.method == 'POST':
        job = request.POST.get('job')
        gender = request.POST.get('gender')
        filter = candidate.objects.filter(Q(job=job) | Q(gender=gender))
        context = {
            'candidates': filter,
            }
        return render(request, 'app/candidates.html', context)

    # GLOBAL SEARCH
    elif 'q' in request.GET:
        q = request.GET['q']
        all_candidates_list = candidate.objects.annotate(
            name =Concat('first_name', p(' '), 'last_name')).filter(Q(name__icontains=q) | Q(first_name__icontains=q) 
            | Q(last_name__icontains=q) | Q(email__icontains=q) | Q(phone__icontains=q) 
            | Q(created_at__icontains=q)).order_by('-created_at')
    else:
        all_candidates_list = candidate.objects.all().order_by('-created_at')
   
    # PAGINATION
    paginator = Paginator(all_candidates_list, 10) #10 is number of records to display on a Page 
    page = request.GET.get('page')
    all_candidates = paginator.get_page(page)
    
    
    context={
        'candidates': all_candidates,
        }
    return render(request, 'app/candidates.html', context)


@login_required(login_url='loginpage')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Candidate(request, candidate_id):
    candidateObj = get_object_or_404(candidate, id=candidate_id)
    context= {
        'candidate': candidateObj
    }
    return render(request, 'app/candidate.html', context)


def Logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='loginpage')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def exportToPdf(request, pk):
    c = get_object_or_404(candidate, id=pk)
    cookies = request.COOKIES
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'cookie' : [
            ('csrftoken', cookies ['csrftoken']),
            ('sessionid', cookies ['sessionid'])
        ]
    }

    # pdf = pdfkit.from_url('http://127.0.0.1:8000/'+str(c.id), False, options = options)
    # response = HttpResponse(pdf, content_type='application/pdf')
    # response['Content-Disposition'] = 'attachment; filename=candidate.pdf'
    # return response

    pdf_name = c.first_name + '' + c.last_name + '.pdf'
    pdf = pdfkit.from_url('http://127.0.0.1:8000/pdf/'+str(c.id), False, options = options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(pdf_name)
    return response

@login_required(login_url='loginpage')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Pdf (request, pk):
    candidate = get_object_or_404(candidate, id=pk)
    context = {
        'candidate':candidate,
        }
    return render(request, 'pdf.html',context)




    # # DISABLE ALL THE FORM FIELDS
    # fields_list = ['experience', 'gender', 'first_name', 'last_name', 'job', 'email',
    #             'phone', 'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'frameworks', 
    #             'languages', 'databases', 'libraries', 'mobile', 'others','message' ,'status_course',
    #             'started_course','finished_course','course','institution','about_course','started_job',
    #             'finished_job','company','position','about_job','employed','remote','travel']
    
    # for field in fields_list:
    #     form.fields[field].disabled=True
    #     form.fields['file'].widget.attrs.update({'style':'display: none'})
    #     form.fields['image'].widget.attrs.update({'style':'display: none'})
