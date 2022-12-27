# Deep time-it
Deep time-it is an open source module that was intended to be an extension of the timeit library, that not only times a function, but can also time each individual line and chunk of code within it, and produce a visual break-down of the slower and faster parts to aid with debugging and refactoring.

## Important
Be careful if your function that you are timing has side effects. If it does, then as sometimes the function may be run twice, the side effect might occur twice. To disable double running, set the `maxrepeats` flag to None.

## Installation
To install the Deep time-it library, use `pip install deep_timeit`. The documentation can be found at TODO. We support Python versions 3.6 to 3.10.

## Usage
Run `deep_timeit.deepTimeit(function)`, and replace `function` with a reference to the function you want to time. It includes the additional flags `args` and `kwargs`, which you can set to a list and dictionary respectively that includes additional arguments and keyword arguments to include when timing the function. The other flags are `maxrepeats`, which if set to an integer, which it is by default, will check if any lines are run more than the threshold and in which case will reattempt timing the function without timing those particular lines. This is a feature because if it times a line a large number of times, the timing itself will start to contribute to the time taken. The function returns an `Info` object, which can be displayed by running `infoob.show()`. 

For example:
```
import deep_timeit

def add(a, b):
    accumilator = 0
    for i in range(a):
      accumilator += 1
    for i in range(b):
      accumilator += 1
    print(f"The result of the addition of a and b is: {accumilator}")

deep_timeit.deepTimeit(add, args=[10000, 20000]).show()
```



## Release notes
TODO

## Similar libraries
- timeit
- line_profiler
- pprofile

## TODO's
Make code work with functions that have:
- Multiline brackets