
from django.db import models
from multiselectfield import MultiSelectField


SITUATION = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected')
)

PERSONALITY = (
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

class candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=18)
    personality = models.CharField(max_length=50, null=True, choices=PERSONALITY)
    salary = models.CharField(max_length=50)
    gender = models.CharField(max_length=7)
    experience = models.BooleanField(null=True)
    smoker = models.CharField(max_length=10, null=True, choices=SMOKER, default="")
    email = models.EmailField(max_length=50)
    message = models.TextField()
    file = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')
    
    # Multiple Checkbox
    frameworks = MultiSelectField(choices=FRAMEWORKS, default="", max_length=50)
    languages = MultiSelectField(choices=LANGUAGES, default="", max_length=50)
    databases = MultiSelectField(choices=DATABASES, default="", max_length=50)
    libraries = MultiSelectField(choices=LIBRARIES, default="", max_length=50)
    mobile = MultiSelectField(choices=MOBILE, default="", max_length=50)
    others = MultiSelectField(choices=OTHERS, default="", max_length=50)

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
