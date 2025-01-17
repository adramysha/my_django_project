# Generated by Django 5.1.2 on 2024-10-30 08:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0002_assessment'),
    ]

    operations = [
        migrations.CreateModel(
            name='AirwayAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mallampati_score', models.CharField(max_length=20)),
                ('neck_mobility', models.CharField(blank=True, max_length=50)),
                ('dental_conditions', models.TextField(blank=True)),
                ('other_notes', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='airway_assessments', to='patient_records.patient')),
            ],
        ),
        migrations.CreateModel(
            name='AnaestheticPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anaesthetic_technique', models.CharField(max_length=20)),
                ('anticipated_difficulties', models.CharField(blank=True, max_length=50)),
                ('pre_op_instructions', models.TextField(blank=True)),
                ('post_op', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='anaesthetic_plan', to='patient_records.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Investigations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=20)),
                ('result', models.CharField(blank=True, max_length=50)),
                ('date', models.TextField(blank=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investigations', to='patient_records.patient')),
            ],
        ),
        migrations.CreateModel(
            name='Medications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dosage', models.CharField(blank=True, max_length=100)),
                ('frequency', models.TextField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications', to='patient_records.patient')),
            ],
        ),
    ]
