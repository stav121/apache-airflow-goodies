### Airgoodies

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/stav121/apache-airflow-goodies/build_wheel.yaml?branch=main&style=flat&label=build)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/stav121/apache-airflow-goodies/mdbook.yaml?branch=main&label=docs)
![PyPI - Version](https://img.shields.io/pypi/v/airgoodies)
![GitHub License](https://img.shields.io/github/license/stav121/apache-airflow-goodies)
![PyPI - Downloads](https://img.shields.io/pypi/dm/goodies)
![GitHub contributors](https://img.shields.io/github/contributors/stav121/apache-airflow-goodies)

Airgoodies is a project that contains various APIs to interact with external services inside Apache Airflow using
minimum configuration (see `airgoodies.{module}.variables.json` for each module).

Current version matrix:

| Airgoodies Version                                                                         | Apache Airflow Version | Python Version | Project tag                                                                                 |
|--------------------------------------------------------------------------------------------|------------------------|----------------|---------------------------------------------------------------------------------------------|
| [0.0.4](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.4)             | 2.7.2                  | 3.11           | [v0.0.4](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.4)             |
| [0.0.3](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.3)             | 2.7.2                  | 3.11           | [v0.0.3](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.3)             |
| [0.0.2](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.2)             | 2.7.2                  | 3.11           | [v0.0.2](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.2)             |
| [0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) | 2.7.2                  | 3.11           | [v0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) |

Provided goodies for version [0.0.4](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.4):

| Module             | Description                                     | Dependency Versions                                      |
|--------------------|-------------------------------------------------|----------------------------------------------------------|
| airgoodies.command | API for dynamic task configuration through YAML | pyyaml==6.0.1                                            |
| airgoodies.aws     | API for easy interaction with AWS               | pandas==2.1.1<br>apache-airflow-providers-amazon===8.7.1 |
| airgoodies.mongo   | API for easy interaction with MongoDB           | pymongo==4.5.0                                           |
| airgoodies.xcom    | API for managing variables through XCom         | *None*                                                   |

### Installation

Add the following requirement in your `requirements.txt`

```
# requirements.txt
airgoodies=0.0.4
```

### Example usage

For the official documentation, see [here](https://stav121.github.io/apache-airflow-goodies)

For an example of how to use this project, see [here](https://github.com/stav121/apache-airflow-goodies-examples)

### Building the project

To build the project:

```shell
$ python3 setup.py sdist bdist_wheel
```

### License

This project is available under the MIT License.

### Author

Stavros Grigoriou ([stav121](https://github.com/stav121))
