# Generated by Django 4.0.3 on 2022-04-12 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0014_delete_games'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_acc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField()),
                ('discord_id', models.CharField(max_length=100)),
                ('zoom_id', models.CharField(max_length=100)),
            ],
        ),
    ]
