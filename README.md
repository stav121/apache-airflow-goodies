### Airgoodies

[![.github/workflows/build_wheel.yaml](https://github.com/stav121/apache-airflow-goodies/actions/workflows/build_wheel.yaml/badge.svg?branch=main)](https://github.com/stav121/apache-airflow-goodies/actions/workflows/build_wheel.yaml)
![PyPI - Version](https://img.shields.io/pypi/v/airgoodies)
![GitHub License](https://img.shields.io/github/license/stav121/apache-airflow-goodies)
![PyPI - Downloads](https://img.shields.io/pypi/dm/goodies)
![GitHub contributors](https://img.shields.io/github/contributors/stav121/apache-airflow-goodies)

Airgoodies is a project that contains various APIs to interact with external services inside Apache Airflow using
minimum configuration (see `airgoodies.{module}.variables.json` for each module).

Current version matrix:

| Airgoodies Version                                                                         | Apache Airflow Version | Python Version | Project tag                                                                                 |
|--------------------------------------------------------------------------------------------|------------------------|----------------|---------------------------------------------------------------------------------------------|
| [0.0.2](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.2)             | 2.7.2                  | 3.11           | [v0.0.2](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.2)             |
| [0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) | 2.7.2                  | 3.11           | [v0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) |

Provided goodies for version [0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha):

| Module           | Description                             | Dependency Versions |
|------------------|-----------------------------------------|---------------------|
| airgoodies.mongo | API for easy interaction with MongoDB   | pymongo==4.5.0      |
| airgoodies.xcom  | API for managing variables through XCom | *None*              |

### Usage

```
# requirements.txt
airgoodies=0.0.2
```

### Example usage

For an example of how to use this project, see [here](https://github.com/stav121/apache-airflow-goodies-examples)

### Building the project

To build the project:

```shell
$ python3 setup.py sdist bdist_wheel
```

### Author

Stavros Grigoriou ([stav121](https://github.com/stav121))