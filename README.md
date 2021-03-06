# ACMnotlost
ACM Boston Local NotLost problem using pyhton
Redfur is exploring the concept of orienteering. He has obtained a compass and a pedometer and is trying them out. He goes to a place with a lot of open fields, chooses a direction, and walks some disatnce in that direction. Then he chooses another direction and walks another disatnce in that direction. And so forth.
At the end of several such 'legs' he wants to know how to get back directly to his starting point. What direction should he walk in, and how far away is it?

Input
-----
For each of several test cases, first a test case name line, and then lines each describing one leg of his walk in the form:

  direction length

where direction is the direction of the leg and length is its length. Directions are angles in degrees in degrees with

    North            0 degrees
    North East      45 degrees
    East            90 degrees
    South East     135 degrees
    South          180 degrees
    South West     225 degrees
    West           270 degrees
    North West     315 degrees
  
Lengths are in feet.

    0 <= direction < 360
    0 < length <= 10,000
  
The direction description lines are followed by a line containing just '*'.

Lines are at most 80 columns long.

Output
------
For each test case, first an exact copy of the test case name input line, and a single line of the form:

    direction length
  
that says that to get back to his starting point from the end of the last leg, Redfur must walk 'length' feet in the given 'direction'.
Directions should be accurate to the nearest degree and lengths to the nearest foot. you cn round output to the nearest integer if you like, but you do not have to.

Output lines are printed to standard output. Output ends when the program terminates.

Sample Input
------ -----

    -- SAMPLE 1 --
    90 100
    0 100
    270 100
    *

    -- SAMPLE 2 --
    45 1414
    180 2000
    *

    -- SAMPLE 3 --
    20 100
    200 100
    200 100
    *

    -- SAMPLE 4 --
    45 100
    90 100
    135 100
    180 100
    225 100
    270 100
    315 100
    *

    -- SAMPLE 5 --
    125 170
    85 1410
    *

    Sample Output
    ------ ------

    -- SAMPLE 1 --
    180 100
    -- SAMPLE 2 --
    315 1414
    -- SAMPLE 3 --
    20 100
    -- SAMPLE 4 --
    0 100
    -- SAMPLE 5 --
    269 1544

    File:      notlost.txt
    Author:    Bob Walton <walton@seas.harvard.edu>
    Date:      Tue Sep 27 11:55:12 EDT 2016 .

The authors have placed this file in the public domain; they make no warranty and accept no liability for this file.
