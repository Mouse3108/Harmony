# Generated by Django 5.1.1 on 2025-01-30 09:32

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/users', verbose_name='Аватар')),
                ('date_birth', models.DateField(blank=True, default=None, null=True, verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='Телефон')),
                ('job_title', models.CharField(blank=True, max_length=50, null=True, verbose_name='Должность')),
                ('job_speciality', tinymce.models.HTMLField(blank=True, null=True, verbose_name='Направления работы')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('educational_institution', models.CharField(max_length=200, verbose_name='Учебное заведение')),
                ('status', models.IntegerField(choices=[(1, 'Высшее образование'), (2, 'Повышение квалификации'), (3, 'Семинар'), (4, 'Обучающий курс'), (0, 'Другое')], default=0, verbose_name='Статус')),
                ('speciality', models.TextField(verbose_name='Специальность')),
                ('year', models.CharField(max_length=4, verbose_name='Год окончания')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='diplomes/', verbose_name='')),
                ('psychologist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='psychologist', to=settings.AUTH_USER_MODEL, verbose_name='Психолог')),
            ],
            options={
                'verbose_name': 'Образование',
                'verbose_name_plural': 'Образование',
            },
        ),
    ]
