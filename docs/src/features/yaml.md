### Task generation using YAML Files

`airgoodies` enables the ability to dynamically create tasks using YAML files with a specific syntax.

Currently the supported syntax offers the following commands:

```yaml
$task_name: # This is the name that will appear for the task (task_id)
  $task: <task> # The task to execute
  config: # The configuration of the task
    $options: $values
    airgoodies_transform_method | custom_transform_method: $method_name
```

#### Options for `$task`:

| option          | explanation                                                              |
|-----------------|--------------------------------------------------------------------------|
| airgoodies_task | use a predefined `airgoodies` task from [this list](tasks/airgoodies.md) |
| custom_task     | run a custom python task, by providing the path of the callable          |

### Options for `config`:

Config enables the configuration of the task, and the options are defined by the `$task` option you have chosen.