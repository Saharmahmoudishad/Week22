# Generated by Django 4.2.7 on 2023-11-19 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('employe_rewards', models.CharField(choices=[('To', 'Time off'), ('G', 'Gifts'), ('WH', 'Work from home days'), ('Gc', 'Gift cards'), ('C', 'Certificates')], default='None', max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('expert', models.CharField(max_length=50)),
                ('experience', models.IntegerField()),
                ('categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff', to='home.category')),
            ],
        ),
    ]
