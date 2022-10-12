
from random import choices
from tabnanny import verbose
from django.db import models
from multiselectfield import MultiSelectField


SITUATION = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected')
)

PERSONALITY = (
    ('','Select personality'),
    ('I am outgoing',' I am outgoing'),
    ('I am social','I am social'),
    ('I am antisocial','I am antisocial'),
    ('I am discreet','I am discreet'),
    ('I am serious','I am serious'),
)

SMOKER = (
    ('1','Yes'),
    ('2', 'No'),
)

#Multiple Checboxex
FRAMEWORKS = (
    ('Laravel', 'Laravel'),
    ('Angular', 'Angular'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('Vue', 'Vue'),
    ('Others', 'Others'))


LANGUAGES = (
    ('Python', 'Python'),
    ('Javascript', 'Javascript'),
    ('Java', 'Java'),
    ('C++', 'C++'),
    ('Ruby', 'Ruby'),
    ('Others', 'Others'),
)


DATABASES = (
    ('MySql', 'MySql'),
    ('postgres', 'Postgres'),
    ('MongoDB', 'MongoDB'),
    ('SqLite3', 'SqLite3'),
    ('Oracle', 'Oracle'),
    ('Others', 'Others'),
)


LIBRARIES = (
    ('Ajax', 'Ajax'),
    ('JQuery', 'JQuery'),
    ('React.js', 'React.js'),
    ('Chart.js', 'Chart.js'),
    ('Gsap', 'Gsap'),
    ('Others', 'Others'),
)


MOBILE = (
    ('React native', 'React native'),
    ('Kivy', 'Kivy'),
    ('Flutter', 'Flutter'),
    ('Ionic', 'Ionic'),
    ('Xamarim', 'Xamarim'),
    ('Others', 'Others'),
)

OTHERS = (
    ('UML', 'UML'),
    ('SQL', 'SQL'),
    ('Docker', 'Docker'),
    ('GIT', 'GIT'),
    ('GraphQL', 'GraphQL'),
    ('Others', 'Others'),
)

STATUS_COURSE = (
    ('', 'Select your status'),
    ("I'm studying", "I'm studying"),
    ('I took a break', 'I took a break'),
    ('Completed', 'Completed'),
)

class candidate(models.Model):    
    # Personal (CARD 1)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=5, verbose_name='Job code')
    birth =models.DateField(auto_now=False, auto_now_add=False, verbose_name='Birthday')
    phone = models.CharField(max_length=18)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50, verbose_name='Salary expectation')
    gender = models.CharField(max_length=7)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField(verbose_name='Presentation')
    file = models.FileField(upload_to='resume', blank=True, verbose_name='Resume')
    image = models.ImageField(upload_to='photo', blank=True, verbose_name='Photo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    company_note = models.TextField(blank=True)
    
    # SkillS (CARD 2)
    # Multiple Checkbox
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="", max_length=50)
    languages = MultiSelectField(choices=LANGUAGES, default="", max_length=50)
    databases = MultiSelectField(choices=DATABASES, default="", max_length=50)
    libraries = MultiSelectField(choices=LIBRARIES, default="", max_length=50)
    mobile = MultiSelectField(choices=MOBILE, default="", max_length=50)
    others = MultiSelectField(choices=OTHERS, default="", max_length=50)

    # Educational (CARD 3)
    institution = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    started_course = models.DateField(auto_now=False, auto_now_add=False)
    finished_course = models.DateField(auto_now=False, auto_now_add=False)
    about_course = models.TextField()
    status_course = models.CharField(max_length=50, null=True, choices=STATUS_COURSE)

    # Professional (CARD 4)
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    started_job = models.DateField(auto_now=False, auto_now_add=False)
    finished_job = models.DateField(auto_now=False, auto_now_add=False)
    about_job = models.TextField()
    employed = models.BooleanField(null=True, verbose_name='I am employed')
    remote = models.BooleanField(null=True, verbose_name='I agree to work remotely')
    travel = models.BooleanField(null=True, verbose_name="I'm available for travel")


    def __str__(self):
        return self.first_name


        # Capitalize Firstname and Lastname
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()

    # Concatenate Firstname and Lastname (Admin Table)
    def name(obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    # Concatenate (when you click over the Candidate)
    def __str__(self):
        return self.first_name + ' ' + self.last_name


    
