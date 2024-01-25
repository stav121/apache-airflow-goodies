### Airgoodies


Airgoodies is a project that contains various APIs to interact with external services inside Apache Airflow using minimum configuration (see `airgoodies.{module}.variables.json` for each module).


Current version matrix:


| Airgoodies Version                                                                         | Apache Airflow Version | Python Version | Project tag                                                                                 |
|--------------------------------------------------------------------------------------------|------------------------|----------------|---------------------------------------------------------------------------------------------|
| [0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) | 2.7.2                  | 3.11           | [v0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha) |


Provided goodies for version [0.0.1-alpha](https://github.com/stav121/apache-airflow-goodies/releases/tag/v0.0.1-alpha):


| Module           | Description                             | Dependency Versions |
|------------------|-----------------------------------------|---------------------|
| airgoodies.mongo | API for easy interaction with MongoDB   | pymongo==4.5.0      |
| airgoodies.xcom  | API for managing variables through XCom | *None*              |


### Building


To build the project:


```shell
$ python3 setup.py sdist bdist_wheel
```


### Author


Stavros Grigoriou ([stav121](https://github.com/stav121))