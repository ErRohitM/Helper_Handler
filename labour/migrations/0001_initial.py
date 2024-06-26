# Generated by Django 3.2.25 on 2024-05-26 07:57

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helpers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('helper', models.CharField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('NOT_SPECIFIED', 'NOT_SPECIFIED')], max_length=15)),
                ('skill', models.CharField(blank=True, max_length=100)),
                ('age', models.IntegerField(default=18)),
                ('location', models.CharField(blank=True, max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True)),
                ('is_assigned', models.BooleanField(default=False)),
                ('assigned_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
