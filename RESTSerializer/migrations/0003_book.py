# Generated by Django 3.0.7 on 2020-07-15 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RESTSerializer', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=32)),
                ('b_price', models.IntegerField(default=1)),
            ],
        ),
    ]