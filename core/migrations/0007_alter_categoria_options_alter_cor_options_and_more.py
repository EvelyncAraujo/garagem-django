# Generated by Django 5.0.6 on 2024-08-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0006_alter_marca_options_remove_marca_descricao_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categoria",
            options={"verbose_name": "Categoria", "verbose_name_plural": "Categorias"},
        ),
        migrations.AlterModelOptions(
            name="cor",
            options={"verbose_name": "Cor", "verbose_name_plural": "Cores"},
        ),
        migrations.RenameField(
            model_name="cor",
            old_name="descricao",
            new_name="nome",
        ),
    ]