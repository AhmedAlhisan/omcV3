# Generated by Django 4.1.5 on 2023-04-10 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_course_course_certficate_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_certficate_upload',
            field=models.FileField(default='Certificat not avilibale', upload_to='static/website/pdfs/'),
        ),
    ]
