# Generated by Django 4.2.3 on 2024-04-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_registration', '0048_guestcourseregistration_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='guestcourseregistration',
            name='dojo',
            field=models.CharField(choices=[('AAR', 'Aikido am Rhein'), ('AVE', 'Aikido Verein Emmendingen'), ('AVF', 'Aikido Verein Freiburg'), ('TVD', 'Turnverein Denzlingen')], default='AVF', max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='guestcourseregistration',
            name='exam',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='usercourseregistration',
            name='exam_grade',
            field=models.IntegerField(choices=[(1, '7th Kyu ⚪️'), (2, '5th Kyu 🟡'), (3, '4th Kyu 🟠'), (4, '3rd Kyu 🟢'), (5, '2nd Kyu 🔵'), (6, '1st Kyu 🟤')], default=0),
        ),
    ]
