Description:
Rule 30 is a one-dimensional binary cellular automaton. You can have some information here: https://en.wikipedia.org/wiki/Rule_30

Complete the function that takes as input an array of 0s and 1s and a non-negative integer n that represents the number of iterations. This function has to perform the nth iteration of Rule 30 with the given input.

The rule to derive a cell from itself and its neigbour is:

Current cell	000	001	010	011	100	101	110	111
New cell	0	1	1	1	1	0	0	0
As you can see the new state of a certain cell depends on his neighborhood. In Current cell you have the nth cell with its left and right neighbor, for example the first configuration is 000:

left neighbor = 0
current cell = 0
right neighbor = 0
The result for the current cell is 0, as reported in the New cell row.

You also have to pay attention to the following things:

the borders of the list are always 0
you have to return an array of 0 and 1
Here a small example step by step, starting from the list [1] and iterating 5 times:

We have only one element so first of all we have to follow the rules adding the border, so the result will be [0, 1, 0]
Now we can apply the rule 30 to all the elements and the result will be [1, 1, 1] (first iteration)
Then, after continuing this way for 4 times, the result will be [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1]
In Python you can also use a support function to print the sequence named printRule30. This function takes as parameters the current list of 0 and 1 to print, the max level that you can reach (number of iterations) and the length of initial array.
```
def printRule30(list_, maxLvl, startLen):
  ...
```
The last two parameters are optional and are useful if you are printing each line of the iteration to center the result like this:

░░▓░░ -> step 1
░▓▓▓░ -> step 2
▓▓░░▓ -> step 3

If you pass only the array of 0 and 1 the previous result for each line will be like this:

▓ -> step 1
▓▓▓ -> step 2
▓▓░░▓ -> step 3

Note: the function can print only the current list that you pass to it, so you have to use it in the proper way during the interactions of the rule 30.