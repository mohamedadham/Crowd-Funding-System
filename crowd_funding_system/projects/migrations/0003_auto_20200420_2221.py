# Generated by Django 2.1 on 2020-04-20 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20200419_1709'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment_reports',
            old_name='comment_id',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment_reports',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='category_id',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='project_comments',
            old_name='comment',
            new_name='comment_text',
        ),
        migrations.RenameField(
            model_name='project_comments',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_comments',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='project_pictures',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_ratings',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_ratings',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='project_reports',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='project_reports',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='project_tags',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='user_donations',
            old_name='project_id',
            new_name='project',
        ),
        migrations.RenameField(
            model_name='user_donations',
            old_name='user_id',
            new_name='user',
        ),
    ]