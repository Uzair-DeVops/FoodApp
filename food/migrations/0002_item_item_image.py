# Generated by Django 5.1.3 on 2024-11-18 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://nanilovestocook.com/wp-content/uploads/2022/08/placeholder.png', max_length=500),
        ),
    ]
