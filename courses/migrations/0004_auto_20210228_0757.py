# Generated by Django 3.1.7 on 2021-02-28 13:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='courses.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='courses.level'),
        ),
        migrations.AlterField(
            model_name='course',
            name='subcategory_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to='courses.category'),
        ),
    ]
