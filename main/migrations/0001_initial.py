# Generated by Django 4.2.7 on 2023-11-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=40)),
                ('team_level', models.CharField(choices=[('U09', 'Under 09s'), ('U10', 'Under 10s'), ('U11', 'Under 11s')], default='U11', max_length=3)),
            ],
        ),
    ]
