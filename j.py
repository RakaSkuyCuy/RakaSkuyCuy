from setuptools import setup

setup(
    name='kensploitspam',
    version='0.1',
    py_modules=['kensploitspam'],
    install_requires=[
        'colorama',
        'pyfiglet',
        'requests',
        'fake_useragent',
        'rich',
    ],
    entry_points={
        'console_scripts': [
            'kensploitspam=kensploitspam:main',
        ],
    },
)
