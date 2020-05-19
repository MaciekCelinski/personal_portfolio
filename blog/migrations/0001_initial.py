# Generated by Django 3.0.6 on 2020-05-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blog/images')),
                ('url', models.URLField(blank=True)),
            ],
        ),
    ]
