# Generated by Django 4.1.5 on 2023-11-30 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_art_relation_tags_art_tags_arts_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='art_tags',
            name='arts_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.art'),
        ),
    ]
