# Generated by Django 4.1.5 on 2023-04-15 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0016_alter_course_course_certficate_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_certficate_upload',
            field=models.ImageField(default='Certificat not avilibale', upload_to='static/pdfs/'),
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('starthijridate', models.CharField(max_length=512, null=True)),
                ('endhijridate', models.CharField(max_length=512, null=True)),
                ('employee_assigend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.employee')),
                ('writen_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
