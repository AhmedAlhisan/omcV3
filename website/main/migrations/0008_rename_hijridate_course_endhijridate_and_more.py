# Generated by Django 4.1.5 on 2023-03-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_course_hijridate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='hijridate',
            new_name='endhijridate',
        ),
        migrations.AddField(
            model_name='course',
            name='starthijridate',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
