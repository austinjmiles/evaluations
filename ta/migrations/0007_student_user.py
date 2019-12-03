# Generated by Django 2.2.7 on 2019-12-01 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ta', '0006_auto_20191119_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
