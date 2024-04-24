# Generated by Django 4.2.3 on 2024-04-24 21:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course_registration', '0064_alter_internalcourse_discount_percentage'),
    ]

    operations = [
        migrations.AddField(
            model_name='internalcourse',
            name='bank_transfer_deadline',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='internalcourse',
            name='discount_percentage',
            field=models.IntegerField(default=50),
        ),
    ]
