from dataclasses import fields
from urllib import request
from django.contrib import admin
from app.models import candidate
from django.utils.html import format_html
from .forms import CandidateForm

class CandidateAdmin(admin.ModelAdmin):
    radio_fields = {"smoker": admin.HORIZONTAL}
    form = CandidateForm
    readonly_fields = ['experience', 'first_name', 'last_name', 'job', 'email', 'age', 'phone', 'salary', 'personality', 'gender', 'smoker', 'file', 'frameworks', 'languages', 'databases', 'libraries', 'mobile', 'others','message',  'created_at']
    exclude = ['status']
    list_filter= ['Situation']
    list_display= ['name', 'job', 'email', 'age', 'created_at', 'status', '_']
    search_fields = ['first_name', 'last_name', 'email', 'age', 'Situation']
    list_per_page = 10
    
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
