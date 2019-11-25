from setuptools import setup, find_packages

def readme():
    with open("README.rst") as f:
        return f.read()

setup(
    name='lyrics_processor',
    python_requires='>3.7',
    version='1.0',
    description='Lyrics processing code',
    long_description=readme(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords='lyricsgenius genius lyrics',
    url='https://github.com/Mitchwatts93/lyrics_processor',
    author='https://github.com/Mitchwatts93',
    author_email='',
    license='MIT',
    packages=find_packages(),
    install_requires = [
    'pandas>=0.23.4',
    'argparse>=1.1',
    're>=2.2.1',
    'json>=2.0.9',
    'lyricsgenius>=1.8.0'
        ],
    include_package_data=True,
    test_suite='nose.collector',
    tests_require=['nose']
    )
