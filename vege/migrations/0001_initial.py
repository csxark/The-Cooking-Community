# Generated by Django 5.1 on 2024-09-11 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipe_name', models.CharField(max_length=100)),
                ('receipe_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('receipe_ingredients', models.TextField(blank=True, null=True)),
                ('receipe_category', models.CharField(blank=True, max_length=100, null=True)),
                ('receipe_instructions', models.TextField(blank=True, null=True)),
                ('cooking_time', models.IntegerField(blank=True, null=True)),
                ('receipe_author', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('difficulty', models.CharField(blank=True, max_length=100, null=True)),
                ('receipe_image', models.ImageField(blank=True, null=True, upload_to='receipes')),
            ],
        ),
    ]
