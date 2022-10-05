from random import choices
from django.db import models


SITUATION = {
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved')
}

class candidate(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    job = models.CharField(max_length=5)
    age = models.CharField(max_length=3)
    phone = models.CharField(max_length=18)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50, null=True, choices=SITUATION, default='Pending')

    # Capitalize Firstname and Lastname
    def clean(self):
        self.first_name = self.first_name.capitalize()
        self.last_name = self.last_name.capitalize()


    def __str__(self):
        return self.first_name
