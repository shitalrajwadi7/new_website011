# Generated by Django 3.2.3 on 2021-05-19 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0003_auto_20210519_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('HOD', 'HOD'), ('Staff', 'Staff'), ('Student', 'Student')], default=1, max_length=10),
        ),
    ]