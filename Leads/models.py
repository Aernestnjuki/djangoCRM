from django.db import models
from django.contrib.auth.models import AbstractUser

TYPE_OF_COMMUNICATION = (
    ('Phone Call', 'Phone Call'),
    ('Text Message', 'Text Message'),
    ('Email', 'Email'),
    ('WhatsApp', 'WhatsApp')
)

LEAD_SOURCE = (
    ('Activation', 'Activation'),
    ('Facebook', 'Facebook'),
    ('Instagram', 'Instagram'),
    ('Website', 'Website'),
    ('Referral', 'Referral'),
)

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=200)

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
    
class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100)

    def __str__(self):
        return self.agent_name


class Lead(models.Model):
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    lead_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    comment = models.TextField()
    mode_of_communication = models.CharField(max_length=100, choices=TYPE_OF_COMMUNICATION)
    source_of_lead = models.CharField(max_length=100, choices=LEAD_SOURCE)
    profile_picture = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='CRM_FILES')

    def __str__(self):
        return self.lead_name
