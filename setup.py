from setuptools import setup


def get_readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='airgoodies',
    version='0.0.2',
    description='Various goodies for Apache Airflow',
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    author='Stavros Grigoriou',
    author_email='unix121@protonmail.com',
    packages=[
        'airgoodies',
        'airgoodies.mongo',
        'airgoodies.xcom',
        'airgoodies.common'
    ],
    install_requires=[
        'pymongo==4.5.0',
        'apache-airflow==2.7.2'
    ]
)
