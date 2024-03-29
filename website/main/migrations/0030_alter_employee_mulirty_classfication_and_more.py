# Generated by Django 4.1.5 on 2023-09-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_alter_employee_mulirty_classfication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='mulirty_classfication',
            field=models.CharField(blank=True, choices=[('جندي', 'جندي'), ('جندي اول', 'جندي أول'), ('عريف', 'عريف'), ('وكيل رقيب', 'وكيل رقيب'), ('رقيب', 'رقيب'), ('رقيب أول', 'رقيب أول'), ('رئيس رقيباء', 'رئيس رقباء'), ('ملازم', 'ملازم'), ('ملازم أول', 'ملازم أول'), ('نقيب', 'نقيب'), ('رائد', 'رائد'), ('مقدم', 'مقدم'), ('عقيد', 'عقيد'), ('عميد', 'عميد'), ('لواء', 'لواء')], max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='non_mulirty_classfication',
            field=models.CharField(blank=True, choices=[('الخامسة', 'الخامسة  '), ('السادسة', 'السادسة  '), ('السابعة', 'السابعة  '), ('الثامنة', 'الثامنة  '), ('التاسعة', 'التاسعة  '), ('العاشرة', 'العاشرة  '), ('الحادية عشر', ' الحادية عشر'), ('الثانية عشر', ' الثانية عشر'), ('الرابعة عشر', ' الثالثة عشر')], max_length=512, null=True),
        ),
    ]
