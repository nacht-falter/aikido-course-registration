# Generated by Django 4.2.3 on 2024-04-24 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_registration', '0065_internalcourse_bank_transfer_deadline_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='internalcourse',
            old_name='bank_transfer_deadline',
            new_name='bank_transfer_until',
        ),
    ]
