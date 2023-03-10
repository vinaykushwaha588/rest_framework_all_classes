# Generated by Django 4.1 on 2022-08-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=100, null=True)),
                ('book_title', models.CharField(blank=True, max_length=150, null=True)),
                ('book_author', models.CharField(max_length=100)),
                ('publish_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
