from setuptools import setup, find_packages

setup(
    name='mylibrary',
    version='0.1',
    packages=find_packages(),
    install_requires=["solana==0.27.0", "tronpy==0.5.0", "bitcoinlib==0.7.1", "requests==2.32.3", "python-dotenv==1.0.1"],
    tests_require=['pytest'],
    test_suite='tests',
    author='Ваше ім’я',
    author_email='ваш_емейл@domain.com',
    description='Опис вашої бібліотеки',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mylibrary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
