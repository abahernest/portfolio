# Generated by Django 3.1.1 on 2020-09-05 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0006_auto_20200903_1414'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='')),
            ],
        ),
    ]
