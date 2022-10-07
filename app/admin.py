from dataclasses import fields
from urllib import request
from django.contrib import admin
from app.models import candidate
from django.utils.html import format_html
from .forms import CandidateForm

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    form = CandidateForm
    exclude = ['status']
    list_filter= ['Situation']
    list_display= ['name', 'job', 'email',  'created_at', 'status', '_']
    search_fields = ['first_name', 'last_name', 'email','Situation']
    list_per_page = 10

    # READONLY (ADMIN DASHBOARD)
    readonly_fields = ['experience', 'gender', 'first_name', 'last_name', 'job', 'email', 
    'phone', 'salary', 'birth', 'personality', 'smoker', 'file', 'image', 'frameworks', 
    'languages', 'databases', 'libraries', 'mobile', 'others','message' ,'status_course',
    'started_course','finished_course','course','institution','about_course','started_job',
    'finished_job','company','position','about_job','employed','remote','travel']
    

    #FIELDSET
    fieldsets =[
        #HR Operations
        ('HR OPERATIONS', {'fields': ['Situation', 'company_note']}),
        
        # PERSONAL
        ('PERSONAL', {'fields': ['experience', 'gender', 'job', 'email', 'phone', 
        'salary','birth', 'personality', 'smoker', 'file', 'image', 'message']}),

        # SKILLS
        ('SKILLS', {'fields': ['frameworks', 'languages', 'databases', 'libraries', 
        'mobile', 'others']}),
        
        # EDUCATIONAL
        ('EDUCATIONAL', {'fields': ['status_course', 'started_course', 'finished_course', 'institution', 
        'course', 'about_course']}),

        # PROFESSIONAL
        ('PROFESSIONAL', {'fields': ['started_job', 'finished_job', 'company', 'position', 
        'about_job']}),

        #NOTE
        ('NOTE', {'fields': ['employed', 'remote', 'travel']}),
    ]


    #Function to hide F-name and L-name in the Admin Dashboard
    def get_fields(self, request, obj=None):
        fields = super().get_fields(request, obj)
        if obj:
            fields.remove('first_name')
            fields.remove('last_name')
        return fields
    

    # Function to change the ICONS
    def _(self, obj):
        if obj.Situation == 'Approved':
            return True
        elif obj.Situation == 'Pending':
            return None
        else:
            return False
    _.boolean = True


    # Function to Color the TEXT
    def status(self, obj):
        if obj.Situation == 'Approved':
            color = '#28a745'
        elif obj.Situation == 'Pending':
            color = '#fea95e'
        else:
            color ='red'
        return format_html('<strong><p style="color: {}">{}</p></strong>'.format(color, obj.Situation))
    status.allow_tags = True

        

admin.site.register(candidate, CandidateAdmin)
