# Generated by Django 5.1.3 on 2024-12-05 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_teacher_contact_alter_teacher_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Contact', models.BigIntegerField()),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
