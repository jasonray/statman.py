from setuptools import setup, find_packages

setup(
    name='statman',
    version='0.0.2',
    author='Mighty Pulpo',
    author_email='jayray.net@gmail.com',
    description='Collection of metrics collection tools, including simple stopwatch',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)