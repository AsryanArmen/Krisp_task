# Add your review suggestions inline as python comments


def get_value(data, key, default, lookup=None, mapper=None):
    """
    Finds the value from data associated with key, or default if the
    key isn't present.
    If a lookup enum is provided, this value is then transformed to its
    enum value.
    If a mapper function is provided, this value is then transformed
    by applying mapper to it.

    Changes made:
    1. Using `data.get(key, default)` to safely retrieve the value, which prevents KeyError.
    2. The check for an empty string is performed after the initial attempt to retrieve the value.
    3. Handling `lookup` through `lookup.get(return_value, 'No enum value')` for safe value transformation and error prevention.
    4. Applying `mapper` is wrapped in a `try-except` block to handle possible errors during value transformation.
    
    """
    return_value = data.get(key, default) # Safely retrieve the value by key or use the default value
  
    if return_value == "":  # If the value is an empty string
        return_value = default  # Use the default value

    if lookup:  # If a lookup dictionary is provided
        return_value = lookup.get(return_value, 'No enume value')    # Transform the value using lookup or return 'No enum value'

    if mapper:   # If a mapper function is provided
        try:
            return_value = mapper(return_value) # Apply the mapper function to the value

        except Exception as e:
            print(f'Mapper applying Error: {e}')    # Handle errors and print a message

    return return_value 



def ftp_file_prefix(namespace):
    """
    Given a namespace string with dot-separated tokens, returns the
    string with
    the final token replaced by 'ftp'.
    Example: a.b.c => a.b.ftp
    """
    return ".".join(namespace.split(".")[:-1]) + '.ftp' # Split the string by dots, remove the last token, add 'ftp'





def string_to_bool(string):
    """
    Returns True if the given string is 'true' case-insensitive,
    False if it is
    'false' case-insensitive.
    Raises ValueError for any other input.
    """
    if string.lower() == 'true':
        return True
    if string.lower() == 'false':
        return False
    raise ValueError(f'String {string} is neither true nor false')   # If the string doesn't match 'true' or 'false', raise an error




def config_from_dict(dict):
    """
    Given a dict representing a row from a namespaces csv file,
    returns a DAG configuration as a pair whose first element is the
    DAG name
    and whose second element is a dict describing the DAG's properties
    """
    namespace = dict['Namespace']   # Retrieve the value of 'Namespace' from the dictionary
    return (dict['Airflow DAG'],
        {"earliest_available_delta_days": 0,    # Set a default value for earliest_available_delta_days
        "lif_encoding": 'json',  # Set the value 'json' for lif_encoding
        "earliest_available_time":
        get_value(dict, 'Available Start Time', '07:00'), # Retrieve or set the start time for availability
        "latest_available_time":
        get_value(dict, 'Available End Time', '08:00'),  # Retrieve or set the end time for availability
        "require_schema_match":
        get_value(dict, 'Requires Schema Match', 'True', mapper=string_to_bool),  # Retrieve or set the schema match requirement with string to bool conversion
        "schedule_interval":
        get_value(dict, 'Schedule', '1 7 * * * '), # Retrieve or set the schedule
        "delta_days":
        get_value(dict, 'Delta Days', 'DAY_BEFORE',lookup=DeltaDays),  # Retrieve or set delta_days with conversion through the DeltaDays enum
        "ftp_file_wildcard":
        get_value(dict, 'File Naming Pattern', None),   # Retrieve or set the file naming pattern
        "ftp_file_prefix":
        get_value(dict, 'FTP File Prefix', ftp_file_prefix(namespace)),  # Retrieve or set the FTP file prefix
        "namespace": namespace   # Add namespace to the configuration
        }
    )

"""
What this code does:

This code is designed to handle DAG (Directed Acyclic Graph) configurations in the context of working with the Airflow workflow management system.

1. The `get_value` function:
   - Retrieves a value from the configuration dictionary by key, ensuring safe handling of missing keys and empty strings.
   - Can transform values through the `lookup` dictionary (e.g., via an enum) or the `mapper` function (e.g., to convert strings to boolean values).

2. The `ftp_file_prefix` function:
   - Transforms the `namespace` string by replacing the last token with 'ftp'. This is useful for creating file name prefixes.

3. The `string_to_bool` function:
   - Converts strings 'true' and 'false' (case-insensitive) into boolean values True or False. 
   - If the string doesn't match 'true' or 'false', it raises an exception.

4. The `config_from_dict` function:
   - Takes a configuration row from a CSV file and creates a pair: the DAG name and a dictionary with various parameters and settings for the DAG.
   - Uses the `get_value`, `ftp_file_prefix`, and `string_to_bool` functions to process values and build the final configuration.

These functions together provide flexibility and reliability when working with DAG configurations, allowing for convenient data processing, error prevention,
and ensuring the correct functioning of DAGs in the Airflow system.
"""