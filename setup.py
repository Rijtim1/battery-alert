from setuptools import setup

setup(
    name='battery-alert',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'psutil==5.8.0',
        'discord_webhook==0.11.0',
    ],
    py_modules=[
        'main',
    ],
)
