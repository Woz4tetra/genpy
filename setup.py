from setuptools import setup
setup(
    packages=['genpy'],
    package_dir={'': 'src'},
    requires=['genmsg']
)