from setuptools import setup, find_packages

setup(
    name='matches',
    version='0.0.1',
    description='A little bit of Pattern matching for Python',
    author='Lincoln Clarete',
    author_email='lincoln@clarete.li',
    url='http://github.com/clarete/matches',
    packages=find_packages(exclude=['*tests*']),
    zip_safe=False,
)
