# Generated by Django 4.0 on 2022-01-02 15:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('user_type', models.CharField(choices=[('candidate', 'candidate'), ('interviewer', 'interviewer')], default='candidate', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Slots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('available_from', models.DateTimeField(verbose_name='available from')),
                ('available_to', models.DateTimeField(verbose_name='available to')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview_apis.users')),
            ],
        ),
    ]
