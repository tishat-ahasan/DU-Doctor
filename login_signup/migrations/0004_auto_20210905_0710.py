# Generated by Django 3.0.3 on 2021-09-05 07:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0003_auto_20190430_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
