from django.db import models

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

class Lead(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    comment = models.TextField()
    mode_of_communication = models.CharField(max_length=100, choices=TYPE_OF_COMMUNICATION)
    source_of_lead = models.CharField(max_length=100, choices=LEAD_SOURCE)
    profile_picture = models.ImageField(blank=True, null=True, default='default.jpg', upload_to='CRM_FILES')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
