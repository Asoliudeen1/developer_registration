from django.contrib import admin
from app.models import candidate
from django.utils.html import format_html

class CandidateAdmin(admin.ModelAdmin):
    list_filter= ['Situation']
    list_display= ['first_name', 'last_name', 'job', 'email', 'age', 'created_at', 'status', '_']
    search_fields = ['first_name', 'last_name', 'email', 'age', 'Situation']
    list_per_page = 10
    
    
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
