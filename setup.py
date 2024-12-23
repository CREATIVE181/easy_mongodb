from setuptools import setup, find_packages

setup(
    name='easy_mongodb',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pymongo',
    ],
    author='CREATIVE',
    author_email='sony.creative.tg1@gmail.com',
    description='A simple interface for MongoDB interactions',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/CREATIVE181/easy_mongodb',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
