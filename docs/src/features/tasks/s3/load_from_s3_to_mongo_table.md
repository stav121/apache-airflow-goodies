### `load_from_s3_to_mongo_table`

#### Overview

The `load_from_s3_to_mongo_table` task, enables the ability to load a file (currently supported `.csv`, `.xls`, `.xlsx`)
directly from an S3 bucket into a MongoDB table, offering the ability to perform actions in between.

#### Transform method options

| option                      | values                                                                                                                      |
|-----------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| airgoodies_transform_method | print_table_contents                                                                                                        |
| custom_transform_method     | `path.to.method`: the method must have the signature `Callable[[pandas.DataFrame], pandas.DataFrame]` (View examples below) |
| output_table_name           | the name of the MongoDB collection to save the result into, default is `{dag_id}_output_table`                              |

#### Example YAML syntax

```yaml
example_task:
  airgoodies_task: load_from_s3_to_mongo_table
  config:
    airgoodies_transform_method: print_table_contents
    output_table_name: my_output_table
```

The above YAML defines a task that will load a file from the configured bucket, print it's contents
and export it into a MongoDB table.

### Example with custom transform method

Let's say we want to load a file from an S3 Bucket, modify the contents and then save the output to MongoDB.

For this case consider the following file `population.csv`

```csv
city,population;year
Athens,3153000;2021
Athens,3154000;2022
Patras,215922;2021
Patras,213984;2011
```

And instead of loading all the cities, we need to load only the ones for `Athens`.

In this case we need to create our own custom method and link it.

Considering the following structure:

```
root/
    \_ dags/
        \_ my_dag.py
            \_ custom/
                \_ transform.py
```

We create a new function in `transform.py`:

```python
import pandas as pd
import logging


def keep_athens(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function that loads the pandas DataFrame and removes the lines that are not
    related to Athens.
    """
    logger: logging.Logger = logging.Logger('airflow.task')
    logger.info('Running custom transform method: keep_athens')

    data.drop(data[data['city'] != 'Athens'].index, inplace=True)

    logger.info(f'New data:\n{data}')
    return data  # Return the DataFrame to write it in MongoDB
```

Now, we need to create a YAML file that creates our task in `Airflow`.
The file should look like this:

```yaml
my_load_data_task:
  airgoodies_task: load_from_s3_to_mongo_table
  config:
    custom_transform_method: custom.transform.keep_athens # Path to our function
```