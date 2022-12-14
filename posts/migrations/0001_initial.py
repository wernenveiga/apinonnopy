# Generated by Django 4.1.4 on 2022-12-13 01:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id_post', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('link_post', models.CharField(max_length=500)),
                ('image', models.CharField(max_length=500)),
            ],
        ),
    ]
