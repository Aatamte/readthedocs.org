# Generated by Django 3.2.18 on 2023-03-15 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0098_pdf_epub_opt_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproject',
            name='urlpattern',
            field=models.CharField(blank=True, default=None, help_text='A Python regex pattern used when evaluating a multi version or single version project. For multi version projects it needs to declare the following replacement fields: language, version, and filename. For single version projects it needs to declare the filename replacement field only. The default pattern for multi version projects is: `^/{language}(/({version}(/{filename})?)?)?$`. The default pattern for single version projects is: `^/{filename}?$`.', max_length=255, null=True, verbose_name='Custom URL pattern for multi version and single version projects'),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='urlpattern_subproject',
            field=models.CharField(blank=True, default=None, help_text='A Python regex pattern used when evaluating a subproject. It needs to declare the following replacement fields: subproject and filename. This pattern will be used to identify the subproject, to change the URL pattern of the subproject itself, change `urlpattern` attribute in the subproject. The default pattern is: `/projects/{subproject}(/{filename})?$`. ', max_length=255, null=True, verbose_name='Custom URL pattern for subprojects'),
        ),
        migrations.AddField(
            model_name='project',
            name='urlpattern',
            field=models.CharField(blank=True, default=None, help_text='A Python regex pattern used when evaluating a multi version or single version project. For multi version projects it needs to declare the following replacement fields: language, version, and filename. For single version projects it needs to declare the filename replacement field only. The default pattern for multi version projects is: `^/{language}(/({version}(/{filename})?)?)?$`. The default pattern for single version projects is: `^/{filename}?$`.', max_length=255, null=True, verbose_name='Custom URL pattern for multi version and single version projects'),
        ),
        migrations.AddField(
            model_name='project',
            name='urlpattern_subproject',
            field=models.CharField(blank=True, default=None, help_text='A Python regex pattern used when evaluating a subproject. It needs to declare the following replacement fields: subproject and filename. This pattern will be used to identify the subproject, to change the URL pattern of the subproject itself, change `urlpattern` attribute in the subproject. The default pattern is: `/projects/{subproject}(/{filename})?$`. ', max_length=255, null=True, verbose_name='Custom URL pattern for subprojects'),
        ),
    ]
