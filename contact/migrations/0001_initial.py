# Generated by Django 3.2.12 on 2022-07-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('priemail', models.EmailField(max_length=100)),
                ('extmail', models.EmailField(max_length=100)),
                ('jobdesc', models.TextField(max_length=50)),
                ('resume', models.FileField(max_length=50, upload_to='uploads/resume/')),
                ('date', models.DateField()),
                ('photo', models.FileField(max_length=50, upload_to='uploads/photos/')),
                ('phone', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address', models.TextField(max_length=200)),
                ('message', models.TextField(max_length=200)),
            ],
        ),
    ]
