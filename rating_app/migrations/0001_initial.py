# Generated by Django 4.1.3 on 2022-12-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('producer', models.CharField(max_length=50, verbose_name='Producer')),
                ('year', models.CharField(max_length=4, verbose_name='Year')),
                ('link', models.CharField(max_length=150, verbose_name='Link')),
                ('rating', models.IntegerField(verbose_name='Rating')),
            ],
        ),
    ]
