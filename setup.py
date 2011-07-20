import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-kanban',
    version='0.1-alpha',
    description='An app for django providing the ability to make kanban boards.',
    long_description=readme,
    author='Darian Moody, Alfredo Aguirre, theTeam',
    author_email='mail@djm.org.uk',
    url='https://github.com/theteam/django-kanban',
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    install_requires=['gevent', 'gevent-websocket', 'gevent-socketio'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ],
)
