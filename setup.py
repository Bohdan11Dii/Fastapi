from setuptools import setup

setup(
    name = 'app-example',
    version = '0.0.1',
    author = 'Bohdan',
    author_email = 'bodyabrovdiy1@gmail.com',
    destription = 'FastApi app',
    install_requires=[
        'fastapi == 0.70.0',
        'uvicorn == 0.15.0',
        'pytest==6'
    ],
    
    scripts=['app/main.py', 'scripts/create_db.py']
)