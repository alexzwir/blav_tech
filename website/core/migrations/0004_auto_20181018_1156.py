# Generated by Django 2.1.2 on 2018-10-18 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20181016_0213'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactmodel',
            old_name='email_contact',
            new_name='contact_email',
        ),
        migrations.RenameField(
            model_name='contactmodel',
            old_name='name_contact',
            new_name='contact_message',
        ),
        migrations.RenameField(
            model_name='contactmodel',
            old_name='phone_contact',
            new_name='contact_phone',
        ),
        migrations.AddField(
            model_name='contactmodel',
            name='contact_name',
            field=models.CharField(default='Empty', max_length=50),
            preserve_default=False,
        ),
    ]
