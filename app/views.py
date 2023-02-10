from django.shortcuts import render, redirect, HttpResponse
from .forms import CandidateForm, EmailForm, ChatCandidateForm
from django.contrib import messages
from .models import Email, candidate, ChartCandidate
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q

# Get users
from django.contrib.auth.models import User

# Send email
from django.core.mail import EmailMessage

# COncatenate (F-Name and L-name)
from django.db.models.functions import Concat  
from django.db.models import Value as P

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


def Logout(request):
    logout(request)
    messages.success(request, "Logout successfully !")
    return redirect('/')


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
     
     # COUNTERS
    total = candidate.objects.all().count()
    frontend = candidate.objects.filter(job='FR-22')
    backend = candidate.objects.filter(job='BA-10').count()
    fullstack = candidate.objects.filter(job='FU-15').count()

    # FILTER
    if request.method == 'POST':
        job = request.POST.get('job')
        gender = request.POST.get('gender')
        filter =  candidate.objects.filter(Q(job=job) | Q(gender=gender))
        context = {
            'candidates': filter,
            'total': total,
            'frontend': frontend,
            'backend': backend,
            'fullstack': fullstack,
            }
        return render(request, 'app/candidates.html', context)

    # GLOBAL SEARCH
    elif 'q' in request.GET:
        q = request.GET['q']
        all_candidates_list = candidate.objects.annotate(
            name =Concat('first_name', P(' '), 'last_name')).filter(Q(name__icontains=q) | Q(first_name__icontains=q) 
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
        'total': total,
        'frontend': frontend,
        'backend': backend,
        'fullstack': fullstack,
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


@login_required(login_url="loginpage")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Delete(request, pk):
    candidateObj = candidate.objects.get(id=pk)

    # DELETE CHAT ONCE CANDIDATE DELETED
    candidate_emails = candidate.objects.values_list('email', flat=True)
    y = ChartCandidate.objects.filter(candidate_email__in = candidate_emails)
    for data in y:
        if data.candidate_email in candidateObj.email:
            candidateObj.delete()
            ChartCandidate.objects.exclude(candidate_email__in = candidate_emails).delete()
            messages.success(request, 'Candidate deleted successfully')
            return redirect('candidates')
        else:
            candidateObj.delete()
            messages.success(request, 'Candidate deleted successfully')
            return redirect('candidates')



@login_required(login_url="loginpage")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def exportToPdf(request, pk):
    c = candidate.objects.get(id=pk)
    cookies = request.COOKIES # GET (access) privates pages
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'cookie' : [
            ('csrftoken', cookies ['csrftoken']),
            ('sessionid', cookies ['sessionid'])
        ]
    }

    # Method 2 (Customized, but requires an external html file)
    pdf_name = c.first_name + '_' + c.last_name + '.pdf'
    pdf = pdfkit.from_url('http://127.0.0.1:8000/pdf/'+str(c.id), False, options = options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-disposition'] = 'attachment; filename="{}"'.format(pdf_name)
    return response


# PDF TEMPLATE
@login_required(login_url="loginpage")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def pdf(request, pk):
    candidateobj = candidate.objects.get(id=pk)
    return render(request, "app/pdf.html", {'candidate':candidateobj})



def email(request):
    if request.method == 'POST':
        # save message to DB
        to_db = Email(
            status = request.POST.get('status'),
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            message = request.POST.get('message'),
            subject = request.POST.get('subject'),
        )
        to_db.save()

        #Send email 
        form = EmailForm(request.POST)
        company = "TT Software Solutions"
        if form.is_valid():
            email = form.cleaned_data["email"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]

            mail = EmailMessage(subject, message, company, [email])
            mail.send()
            messages.success(request, 'Email sent successfully')
            return redirect('candidates')
    else:
        form = EmailForm()
        return render(request, {'form':form})




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


@login_required(login_url="loginpage")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def chat_candidate(request, id):
    candidateObj = candidate.objects.get(pk=id)
    chat_candidate = ChartCandidate.objects.all().order_by('-dt')
    list_users = User.objects.all()

    if request.method == 'POST':
        form = ChatCandidateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('chat-candidate', id=candidateObj.id)
    else:
        form = ChatCandidateForm()
    context = {
        'form': form,
        'chat_candidate': chat_candidate,
        'list_users': list_users,
        'candidateObj': candidateObj
    }
    
    return render(request, 'app/chat_candidate.html', context)