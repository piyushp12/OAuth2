# Generated by Django 4.0 on 2023-04-02 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='Profile/%Y/%m/%d/', verbose_name='Avatar')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(default='', max_length=100, verbose_name='Address')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super User')),
                ('is_staff', models.BooleanField(default=False)),
                ('otp', models.CharField(default='', max_length=10, verbose_name='Otp')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
