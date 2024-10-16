from setuptools import setup, find_packages

setup(
    name="DataScraper",
    version="0.1.0",
    description="A web scraper to extract URLs, content from websites and convert DOCX to PDF.",
    long_description=open('README.md').read(),
    url='https://github.com/mukhtarulislam/Datascrapper.git'
    author="Mukhtar ul Islam",
    author_email="mukhtarulislam88@hotmail.com",
    packages=find_packages(),
    install_requires=[
        "requests",
        "beautifulsoup4",
        "python-docx",
        "reportlab"
    ],
    entry_points={
        'console_scripts': [
            'data-scraper=data_scraper:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License ",
        "Operating :: OS Independent"
    ]
)
