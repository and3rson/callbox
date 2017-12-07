# Generated by Django 2.0 on 2017-12-07 15:58

from django.db import migrations


USERS = [
    ('alice', 'alice@example.org', '12345'),
    ('bob', 'bob@example.org', '12345'),
    ('cat', 'cat@example.org', '12345'),
]


def create_users(apps, schema):
    from django.contrib.auth.models import User
    # user_model = apps.get_model('auth.User')
    for username, email, password in USERS:
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__')
    ]

    operations = [
        migrations.RunPython(create_users)
    ]

