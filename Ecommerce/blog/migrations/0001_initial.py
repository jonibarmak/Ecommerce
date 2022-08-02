# Generated by Django 4.0.6 on 2022-08-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=1000)),
                ('creation_date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=50)),
            ],
        ),
    ]
