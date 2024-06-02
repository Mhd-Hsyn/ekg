# Generated by Django 4.1.7 on 2023-05-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('symtoms', '0003_remove_diseasesymtoms_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diseasesymtoms',
            old_name='uid',
            new_name='id',
        ),
        migrations.AddField(
            model_name='diseasesymtoms',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='diseasesymtoms',
            name='question',
            field=models.TextField(default='?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diseasesymtoms',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='diseasesymtoms',
            name='version_list',
            field=models.CharField(choices=[('v1', 'v1'), ('v2', 'v2'), ('v3', 'v3'), ('v4', 'v4'), ('v5', 'v5'), ('v6', 'v6')], default='v1', max_length=5),
            preserve_default=False,
        ),
    ]