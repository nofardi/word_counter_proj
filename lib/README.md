# Word Counter Project

## Word counter program, a few things to know:
- To execute run the following command from the project root: `python app.py`
- When the app starts to run you can terminate it after as much rounds as you like.
- You're free to enter any input you'd like (as long as it's supported) in any order you think of.
- The supported inputs are:
    - free text (string) 
    - file path (absolute path that start with "/" and the file be *.txt)
    - url that starts with http:// OR https://
- The result of the counters will throughout the run, meaning if you'll run the app with the same input, there will be no distinct words and the occurance of a specific word will multiply.

## Tests
- I've added some unit test in order to test the basic functionality of the app 
    - To execute the tests run the following command: `python -m unittest tests.unit_tests`