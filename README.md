# Deep time-it
Deep time-it is an open source module that was intended to be an extension of the timeit library, that not only times a function, but can also time each individual line and chunk of code within it, and produce a visual break-down of the slower and faster parts to aid with debugging and refactoring.

## Important
This was not intended to compete with the timeit library, as both modules have their advantages. For example, this module only times functions once, whereas timeit does it several times, which gives a better average of how long the code takes to execute.
Also, be careful if your function that you are timing has side effects. If it does, then as sometimes the function may be run twice, the side effect might occur twice. To disable double running, set the `reattempt` flag to false.

## Installation
To install the Deep time-it library, use `pip install deep_timeit`. The documentation can be found at TODO. We support Python versions 3.6 to 3.10.

## Usage
Run `deep_timeit.deepTimeit(function)`, and replace `function` with a reference to the function you want to time. It includes the additional flags `args` and `kwargs`, which you can set to a list and dictionary respectively that includes additional arguments and keyword arguments to include when timing the function. The other flags are `reattempt`, which if set to True, which it is by default, will check if any lines are run more than a large threshhold e.g. 10,000 and in which case will reattempt timing the function without timing those particular lines. This is a feature because if it times a line a large number of times, the timing itself will start to contribute to the time taken. The `show` keyword, which is set to True by default, defines whether or not to display the time breakdown, or if set to False, to simply return an `Info` object, which can be displayed by running `infoob.show()`. Finally, the `mintime` keyword, if it is not set to None, which it is by default, will set every colour to green if the code executes faster than the `mintime` flag.

## Release notes
TODO

## TODO's
Make code work with functions that have:
- globals
- empty lines
- comments
- multi-line strings