# Generated by Django 3.1.1 on 2020-09-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200919_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, to='main.Comments'),
        ),
    ]
