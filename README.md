# python_calculator
programs for the numworks calculator for physics, calculus, and more.

<b>standards to follow when making a pull request</b>
- make sure your file is in the "OtherStuff" folder, JaranStuff is for Jaran's stuff, PaigeStuff is for Paige's stuff

- for private methods use a double underscore at the beginnging on the method name. this garuntees it won't show up in the function variables in the list when using them on the calculator.
  - ex: use `def __sort_list:` instead of `def sort_list:`
  
- use snake case for all variable names
  - ex: use `one_two = [1, 2]` not `oneTwo = [1, 2]`
  
- make sure someone could use your code from a commandline without knowing what it does
  - ask for inputs, not function parameters (unless you use both and request input when no parameters are provided)
  - make a clear function name
  - tell your user what to input, don't assume they know
  - if giving an angle as an output, output in radians and degrees

- if necessary, use enput in your function for getting input
  - these functions evaluate the input so that mathemtical expressions are reduced to a single number
  - ex: if you wanted the volume as an input, someone might want to input 5\*3\*6, this would let them do that with no additional work on your end
  - this can be gotten easily by putting `from input_handler import __input_eval as enput` at the top of your script

- test your code before you commit
