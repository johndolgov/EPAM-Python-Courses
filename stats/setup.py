# License MIT

from setuptools import setup, find_packages
import os

DISTRO_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def extract_requirements(file):
    """
    Extracts requirements from requirements file

    :param file: path to requirements file
    :type file:str
    :return: list[str] -- list of requirements
    """
    with open(file, 'r') as file:
        return file.read().splitlines()


setup(
    name='statistical-functions-distro',
    version='0.1',
    description='statistical-function is a set of functions created for training purposes within the epam course.',
    author='Ivan Dolgov',
    author_email='johndolgov@gmail.com',
    license='MIT',
    classifiers=[
        'Topic :: Education',
        'Programming language :: Python :: 3.6',
    ],
    packages=find_packages(exclude=['tests']),
    install_requires=extract_requirements(os.path.join(DISTRO_ROOT_PATH,
                                                       'requirements', 'base.txt')),
    tests_require=extract_requirements(os.path.join(DISTRO_ROOT_PATH,
                                                    'requirements', 'test.txt')),
    test_suite='nose.collector'
)
