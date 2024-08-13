from django.db import models

class Ticket(models.Model):
    
    
    #vahed = models. 
    subject = models.CharField(max_length=70)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{ self.subject} - {self.description[:30]}"
