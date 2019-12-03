from setuptools import setup

setup(
    name='ifconfig-parser',
    version='0.0.5',
    url='https://github.com/KnightWhoSayNi/ifconfig-parser',
    author='KnightWhoSayNi',
    author_email='threeheadedknight@protonmail.com',
    packages=['ifconfigparser'],
    package_dir={'ifconfigparser': 'ifconfigparser'},
    license='MIT license',
    description='ifconfig-parser',
    classifiers=(
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
    ),
)
