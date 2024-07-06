from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='Plotium',
    version='1.1.0',
    description='Python Library to plot and visualize chemical trends',
    long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='https://github.com/rohankishore/Plotium',
    author='Rohan Kishore',
    author_email='rohankishore746@outlook.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['calculator', 'chemistry', 'chemical plots'],
    packages=find_packages(),
    install_requires=['matplotlib']
)
