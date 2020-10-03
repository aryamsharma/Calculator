# Calculator
Calculator in Python + pygame

Calculator which supports the basic operations on integers. 
It works with English words for numbers and operators.

The calculator input is read from stdin consisting of one expression 
per line and terminated by an empty line. The results are written to 
stdout, one result per line. See sample input and output.

In case of errors it should emit "ERROR" as the calculation result. 
If any intermediate result is outside the range of valid numbers this 
is also considered an error.

Valid Operators:
	+, plus
	-, minus
	*, times
	/, divided by

Numbers all integers in the range -9.999.999 to 9.999.999 (inclusive) 
