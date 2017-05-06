# RGR 
rgr mode allows for arbitararly complex dice rolls.

## Examples
`!rgr 1d20`
Rolls a 20 sided dice Normal run of the mill dice roll. Anything calling itself a dice roller can do this.

`!rgr 1d6+4`
The addtion of some arthimatic is hardly unusual.

`!rgr 4+1d6+1d8+2d10`
This is more complicated. Simple dice interpreters can't do this.

`!rgr 4d6k3`
Rolls 4 six-sided dice and keeps only the highest 3.

`!rgr 6#4d6k3`
Does the above 6 times. This produces a starting stat array under DnD rules with one commmand.



## Formal Grammar

### dice
`d <scalar>`            Rolls a die with the specified number of sides.
`<scalar> d <scalar>`   Rolls a number of dice with the specified number of sides. Returns a list of the results.

### math
`<scalar> + <scalar>`
`<scalar> - <scalar>`

### lists
`<list>`                                If encountering a list on it's own it is assumed you want the sum of it's elements.
`[highest|lowest] <scalar> of <list>`   Returns a list composed of only the highest of lowest elements of the given list.
`<list>k<scalar>`                       keeps the highest elements of given list.
`<scalar> # <expression>`               Evaluates the expression given scalar times. Returns a List.


# Other Notable Dice Interpreters

* http://wiki.rolisteam.org/index.php/En:Dice
* http://lmwcs.com/rptools/wiki/Dice_Expressions
