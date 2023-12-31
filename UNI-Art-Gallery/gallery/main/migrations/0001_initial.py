# Generated by Django 4.1.5 on 2023-11-30 17:08

import cloudinary.models
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Creation_Date', models.DateTimeField(auto_now_add=True)),
                ('title', models.TextField(default='Untitled', max_length=100)),
                ('Description', models.TextField(max_length=500)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Owner_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag_List',
            fields=[
                ('Tag_ID', models.AutoField(primary_key=True, serialize=False)),
                ('Tag_Name', models.TextField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.TextField(max_length=20)),
                ('Last_Name', models.TextField(max_length=20)),
                ('About_Me', models.TextField(max_length=500)),
                ('User_ID', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Art_Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tag1', models.ForeignKey(default='No Tag', on_delete=django.db.models.deletion.CASCADE, related_name='Tag1', to='main.tag_list')),
                ('Tag2', models.ForeignKey(default='No Tag', on_delete=django.db.models.deletion.CASCADE, related_name='Tag2', to='main.tag_list')),
                ('Tag3', models.ForeignKey(default='No Tag', on_delete=django.db.models.deletion.CASCADE, related_name='Tag3', to='main.tag_list')),
            ],
        ),
        migrations.CreateModel(
            name='Art_Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rating', models.PositiveBigIntegerField(verbose_name=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('Art_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_id', to='main.art')),
                ('Reviewer_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='art',
            name='Relation_Tags',
            field=models.ManyToManyField(to='main.art_tags'),
        ),
    ]
