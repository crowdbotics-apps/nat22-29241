# Generated by Django 2.2.24 on 2021-07-28 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('users', '0002_auto_20210728_0524'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='group',
            field=models.ManyToManyField(blank=True, related_name='user_group', to='course.Group'),
        ),
    ]
