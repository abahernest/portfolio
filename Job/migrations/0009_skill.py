# Generated by Django 3.1.1 on 2020-09-12 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job', '0008_auto_20200909_2247'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
        ),
    ]