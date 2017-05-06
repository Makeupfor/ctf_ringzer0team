# Number game - Challenge 130

The random number is between 0 and 10000.

We'll use this simple method to win the game 10 times :

1. Start at 5000

2. If number is too high:
 * set max_value = current_val.
 * next number = current_val / 2


3. If number is too low:
 * next number = current_val + (max value - current_val) / 2

Sometimes it's not fast enough and you have to try again.

[challenge130.py](challenge130.py)
