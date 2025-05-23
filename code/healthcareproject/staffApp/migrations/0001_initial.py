# Generated by Django 4.1.10 on 2023-11-25 09:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=10)),
                ('specialization', models.CharField(max_length=25)),
                ('experience_years', models.PositiveIntegerField()),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('profile_photo', models.ImageField(upload_to='staff/profile/')),
            ],
        ),
    ]
