# Generated by Django 4.0.2 on 2022-02-28 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_home_delete_choice_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('picture', models.ImageField(blank=True, null=True, upload_to='img')),
            ],
        ),
    ]