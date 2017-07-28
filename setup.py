from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()
setup(
    name='cloud_util_s3',
    version='0.0.1',
    description='Python module to upload an object/file into AWS S3.',
    long_description=readme,
    author='Quadyster_dev_team',
    author_email='vnallamothu@quadyster.com',
    url='https://github.com/nvamshik/cloud_util_s3',
    packages=find_packages(exclude=('tests', 'docs'))
)
