# Variables
Variables aren't really possible, so it's used for the true/false in the input/output of the logic stuff in UB.

    define Button myButton
define a button, named myButton. Simple enough. you can do these with other types, of course:
    define Button myButton
    define Button myOtherButton
    define Button anotherButton
    define Switch switch
    define Raycast inTheWay
    define Node notAUselessVariableISwear
    define Display score

To make a variable react to input, just do:
    notAUselessVariableISwear()
Here, we just activate the node notAUselessVariableISwear.

If you want to for example, hook a button to this node, you can do this:
    if (myButton) then
        notAUselessVariableISwear()
    end

For `Display`s, you need to do this to change their values:
    score(0,0,1,0)

# If, Else statements
Most useful part probably.

    if (myButton) then
        notAUselessVariableISwear()
    else
        if (myOtherButton) then
            score(1,0,1,0)     
        else
            score(1,0,0,0)
        end
    end

Here, if myButton is held, it triggers a node. And if not, it check if another button is pressed, and sets the score to a number (i cant do bitwise math but it doesnt matter). And if that button isnt pressed it defaults to setting the score display to 1.

You can also use AND and OR, of course.

    if (switch&&anotherButton) then
        display(1,0,0,0)
    else
        if (switch||anotherButton) then
            display(0,1,0,0)
        end
    end
If switch and anotherButton is activated, it sets the score to 1. But if either of them are pressed, it sets the score to 2.