# Generated by Django 4.1.5 on 2023-04-10 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_course_certificate_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_certficate_upload',
            field=models.FileField(default='Certificat not avilibale', upload_to='pdf/'),
        ),
    ]
