# drop_columns

This transform method enables the option to drop some columns from the end table.

# Configuration options

| config          | description             | type  | example              |
|-----------------|-------------------------|-------|----------------------|
| drop_column_val | List of columns to drop | [str] | [column_1, column_2] |

# Example

```yaml
my_task:
  airgoodies_task: load_from_s3_to_mongo_table
  config:
    airgoodies_transform_method: drop_columns
    drop_columns_val: [ column_1, column_2 ]
```