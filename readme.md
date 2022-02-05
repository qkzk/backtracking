# Bactrakcing algorithms

Some examples of backtracking algorithms implemented in Python


# One to hundred

Fill a 10x10 board with 1 to 100 integers.

1. Start where you want
2. To write the next number, you must skip 2 cells in a straight line
    or one cell diagonally.

    Two cells are "neighbors" if

        * they are separated by 2 empty cells on a straight line :
            `10 . . 11`
        * or one cell diagonally :
            ```
            10 .  .
            .  .  .
            .  .  11
            ```

3. Repeat last step untill you are strucked or reach 100.

A solution found :

```
  1 43 70 16 42 65 11 41 64 10
 56100 34 55 99 31 52 98 30 51
 71 17 95 82 24 88 79 23 89 78
  2 44 69 15 35 66 12 40 63  9
 57 83 33 54 96 32 53 97 29 50
 72 18 94 81 25 87 80 22 90 77
  3 45 68 14 36 67 13 39 62  8
 58 84 26 47 85 27 48 86 28 49
 73 19 93 74 20 92 75 21 91 76
  4 46 59  5 37 60  6 38 61  7
```
