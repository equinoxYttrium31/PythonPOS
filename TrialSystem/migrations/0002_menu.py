# Generated by Django 5.1.2 on 2024-11-09 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TrialSystem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FoodName', models.CharField(max_length=100)),
                ('foodPrice', models.IntegerField()),
                ('foodDescription', models.CharField(max_length=100)),
                ('foodType', models.CharField(max_length=100)),
            ],
        ),
    ]