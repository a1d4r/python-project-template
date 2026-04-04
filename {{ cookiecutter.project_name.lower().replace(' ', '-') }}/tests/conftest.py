from typeguard import install_import_hook

install_import_hook(packages=["{{ cookiecutter.package_name }}"])
