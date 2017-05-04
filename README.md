# RGR 
rgr mode allows for arbitararly complex dice rolls, it can for 
instance roll a starting stat array under DnD rules with one commmand 
`!rgr 6#highest 3 of 4d6`.

## dice
`d <scalar>`            Rolls a die with the specified number of sides.
`<scalar> d <scalar>`   Rolls a number of dice with the specified number of sides. Returns a list of the results.

## math
`<scalar> + <scalar>`
`<scalar> - <scalar>`

## lists
`<list>`                                If encountering a list on it's own it is assumed you want the sum of it's elements.
`[highest|lowest] <scalar> of <list>`   Returns a list composed of only the highest of lowest elements of the given list.
`<list>k<scalar>`                       keeps the highest elements of given list.
`<scalar> # <expression>`               Evaluates the expression given scalar times. Returns a List.


# Other Notable Dice Interpreters

* http://wiki.rolisteam.org/index.php/En:Dice
* http://lmwcs.com/rptools/wiki/Dice_Expressions
