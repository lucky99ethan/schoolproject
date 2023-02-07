# Generated by Django 4.1.5 on 2023-02-07 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interface', '0008_remove_user_last_login_remove_user_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='pass_word',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user',
            name='addUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='add', to='interface.adduser'),
        ),
    ]
