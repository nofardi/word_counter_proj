# Word Counter Project

## Word counter program, a few things to know:
- To execute run the following command from the project root: `python app.py ${APP_MODE} ${YOUR_INPUT} ${WORD_TO_COUNT}`
    - APP_MODE - should be `1` OR `2` 
        - `1` is for count the unique words so far
        - `2` is for counting the occurance so far of the specific word given 
    - YOUR_INPUT - the input you choose, explained further below
    - WORD_TO_COUNT - comes with option `2`, the word you want us to count 
- You're free to enter any input you'd like (as long as it's supported) in any order you think of.
- The supported inputs are:
    - free text (string) - should be surrounded by quotes
    - file path (absolute path that start with `/` and the file be `*.txt`)
    - url that starts with `http://` OR `https://`
- The result of the counters will persist throughout, meaning, for example, if you'll run the app with the same input, there will be no distinct words and the occurance of a specific word will multiply.

## Tests
- I've added some unit test in order to test the basic functionality of the app 
    - To execute the tests run the following command: `python -m unittest tests.unit_tests`