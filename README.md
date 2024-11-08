# looprint

`looprint` is a Python utility designed to enhance the visibility of loops by providing real-time progress updates in the console. It works seamlessly with any iterable and updates the console output to reflect the current state of processing, making it especially useful for long-running tasks.

## Features

- **Real-time updates:** Displays progress information in the console while iterating over an iterable.
- **Elapsed and remaining time:** Provides estimates for how long the iteration has been running and how much time is left until completion.
- **Customizable loop name:** Allows you to specify a name for the loop for better context in your logs.
- **Compatibility:** Works with any iterable, including lists, dictionaries, sets, etc.

## Installation

```bash
pip install looprint
```

No additional installation is required.

## Usage

To use `looprint`, import it into your script and then iterate over any iterable by passing it as loopprint argument. Here’s a simple example demonstrating its functionality:

```python
from looprint import looprint

# Example data
#-----------------------------------
myList = ['value1', 'value2', 'value3']
myDict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
#-----------------------------------

# Example loops with processing logs
#-----------------------------------
for value in looprint(myList):
  print(value)  # Your processing logic
  # ...

for key, value in looprint(data.items()):
    print(key, ':', value)  # Your processing logic
    # ...
#-----------------------------------
```

## Parameters

- data (Iterable): The iterable you want to process (e.g., list, dict, set).
- loopName (str): Optional. A name for the loop that will be displayed in the progress messages (default is "Loop").

## How it works

1. When you start the loop, looprint will print an initial message indicating the beginning of processing.

2. For each item in the iterable, it will update the console with the current progress, including:

- The number of items processed so far.
- The total number of items.
- The percentage of completion.
- The elapsed time and the estimated remaining time.

4. After processing all items, it will print a summary of the total items processed and the total time taken.

## Example Output

When using the looprint class with the above examples, the console will show updates like this:

```
---------- Loop
value1
value2
----------
Processing Loop... 2 of 3 (66.66%) | Elapsed: 4.0000 sec - Remaining: 2.0000 sec
----------
```

```
---------- Loop
key1 : value1
key2 : value2
----------
Processing Loop... 2 of 3 (66.66%) | Elapsed: 4.0000 sec - Remaining: 2.0000 sec
----------
```

## Notes

- Make sure that the output device (e.g., terminal or console) supports ANSI escape codes for proper formatting.
- Use time.sleep() or similar calls in your processing to see the progress updates in action.

## License

This project is open-source and available under the MIT License. Feel free to use, modify, and distribute it as needed.
