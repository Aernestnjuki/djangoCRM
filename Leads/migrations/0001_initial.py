# Generated by Django 5.1.6 on 2025-02-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('phone_number', models.IntegerField()),
                ('comment', models.TextField()),
                ('mode_of_communication', models.CharField(choices=[('Phone Call', 'Phone Call'), ('Text Message', 'Text Message'), ('Email', 'Email'), ('WhatsApp', 'WhatsApp')], max_length=100)),
                ('source_of_lead', models.CharField(choices=[('Activation', 'Activation'), ('Facebook', 'Facebook'), ('Instagram', 'Instagram'), ('Website', 'Website'), ('Referral', 'Referral')], max_length=100)),
                ('profile_picture', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='CRM_FILES')),
            ],
        ),
    ]
