from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_alter_zayavka_payment_alter_zayavka_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zayavka',
            name='datetime',
            field=models.DateTimeField(verbose_name='Дата и время записи'),
        ),
    ]
