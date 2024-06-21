from setuptools import setup, find_packages

setup(
    name='havbruk-taksonomi',
    version='0.1.0',
    description='A taxonomy management tool for havbruk',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nicbechntnu/havbruk-taksonomi',
    author='Nic Bech',
    author_email='nic@example.com',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'pandas', 'numpy'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
