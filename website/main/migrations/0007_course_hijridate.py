# Generated by Django 4.1.5 on 2023-03-26 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_employee_number_of_courses_days_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='hijridate',
            field=models.CharField(max_length=512, null=True),
        ),
    ]