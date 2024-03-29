# Generated by Django 4.1.5 on 2023-09-11 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_course_course_certficate_upload'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='rank',
        ),
        migrations.AddField(
            model_name='employee',
            name='mulirty_classfication',
            field=models.CharField(choices=[('الرتبة العسكرية الاولى', 'الرتبة العسكرية الاولى'), ('الرتبة العسكرية الثانية', 'الرتبة العسكرية الثانية'), ('الرتبة العسكرية الثالثة', 'الرتبة العسكرية الثالثة'), ('الرتبة العسكرية الرابعة', 'الرتبة العسكرية الرابعة')], max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='non_mulirty_classfication',
            field=models.CharField(choices=[(' العاشره', 'العاشره  '), ('=  الحادية عشر', ' الحادية عشر'), ('  الثانية عشر', ' الثانية عشر'), ('  الثالثة عشر', ' الثالثة عشر')], max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='preRank',
            field=models.CharField(choices=[('عسكري', 'عسكري'), ('مدني', 'مدني')], default=1, max_length=512),
            preserve_default=False,
        ),
    ]
