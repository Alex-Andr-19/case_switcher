from setuptools import setup, find_packages

setup(
    name="my_package",
    version="0.1",
    packages=find_packages(),
    install_requires=[],  # Сюда можно добавить зависимости
    author="Ваше имя",
    author_email="ваш_email@example.com",
    description="Описание вашего пакета",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/Alex-Andr-19/case_switcher",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
