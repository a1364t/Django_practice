# Generated by Django 4.0.5 on 2022-07-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='teacher',
            field=models.CharField(blank=True, choices=[('ahmadi', 'Ahmadi'), ('abdi', 'Abdi'), ('bahrami', 'Bahrami')], max_length=7, null=True),
        ),
    ]
