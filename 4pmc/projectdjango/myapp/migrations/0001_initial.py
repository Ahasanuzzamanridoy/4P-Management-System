# Generated by Django 4.0 on 2022-01-30 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Receivebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BOOKID', models.CharField(max_length=6)),
                ('FICODE', models.CharField(max_length=5)),
                ('DATE', models.CharField(max_length=10)),
            ],
        ),
    ]