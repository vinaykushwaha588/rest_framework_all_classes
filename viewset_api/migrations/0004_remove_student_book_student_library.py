# Generated by Django 4.1 on 2022-08-24 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewset_api', '0003_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='book',
        ),
        migrations.AddField(
            model_name='student',
            name='library',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, related_name='student', to='viewset_api.library'),
            preserve_default=False,
        ),
    ]
