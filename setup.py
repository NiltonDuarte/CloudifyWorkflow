from setuptools import setup

setup(
    name='my_workflow',
    version='0.0',
    author='Cloudify',
    packages=['my_workflow_plugin'],
    install_requires=['cloudify-plugins-common>=3.3'],
)