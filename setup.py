#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'ipywidgets',
    'nibabel',
    'ipyvolume',
    'matplotlib',
    'numpy',
    'scipy',
    'nilearn',
    'scikit-learn',
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Jan Freyberg, Bjoern Soergel, others, Jacob Reinhold",
    author_email='jcreinhold@gmail.com',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="Neuroimaging widgets for jupyter notebooks ",
    install_requires=requirements,
    license="Apache Software License 2.0",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='niwidgets',
    name='niwidgets',
    packages=find_packages(include=['niwidgets', 'niwidgets.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/jcreinhold/niwidgets',
    version='0.2.3',
    zip_safe=False,
)
