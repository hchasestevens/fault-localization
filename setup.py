from setuptools import setup

setup(
    name='fault-localization',
    packages=['fault_localization'],
    platforms='any',
    version='0.1.5',
    description='A fault localization tool for Python\'s pytest testing framework.',
    author='H. Chase Stevens',
    author_email='chase@chasestevens.com',
    url='https://github.com/hchasestevens/fault-localization',
    license='MIT',
    install_requires=[
        'pytest>=3.1.2',
    ],
    entry_points={
        'pytest11': [
            'fault-localization = fault_localization.plugin',
        ]
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ]
)
