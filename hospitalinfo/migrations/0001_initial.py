# Generated by Django 2.2 on 2019-05-01 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('Department_id', models.AutoField(primary_key=True, serialize=False)),
                ('Department_number', models.CharField(max_length=20)),
                ('Department_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('Doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('nickname', models.CharField(blank=True, default='', max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('Season_id', models.AutoField(primary_key=True, serialize=False)),
                ('Season_name', models.CharField(max_length=45, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('section_id', models.AutoField(primary_key=True, serialize=False)),
                ('section_name', models.CharField(max_length=10)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='hospitalinfo.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='hospitalinfo.Patient')),
                ('season', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sections', to='hospitalinfo.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('registration_id', models.AutoField(primary_key=True, serialize=False)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='hospitalinfo.Patient')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='registrations', to='hospitalinfo.Section')),
            ],
        ),
    ]
