# Generated by Django 4.1.5 on 2023-12-02 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_user_social_whatsapp_deal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='Message',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='buyer',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='payment_id',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='seller',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='status',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='timestamp',
        ),
    ]
