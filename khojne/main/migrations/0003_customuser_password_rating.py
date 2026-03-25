# Generated migration for adding password field and Rating model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_customuser_remove_servicerequest_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, '1 - Poor'), (2, '2 - Fair'), (3, '3 - Good'), (4, '4 - Very Good'), (5, '5 - Excellent')])),
                ('comment', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_received', to='main.customuser')),
                ('request', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.servicerequest')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings_given', to='main.customuser')),
            ],
            options={
                'ordering': ['-created_at'],
                'unique_together': {('user', 'expert', 'request')},
            },
        ),
    ]
