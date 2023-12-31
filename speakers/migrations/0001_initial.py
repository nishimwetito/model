# Generated by Django 4.2.2 on 2023-06-24 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('contact_info', models.CharField(max_length=255)),
                ('profile_picture', models.ImageField(upload_to='speaker_images')),
                ('expertise_areas', models.CharField(max_length=255)),
            ],
        ),
    ]
