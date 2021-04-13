# Example

Name.py contains a Name class that you instantiate giving it a name to parse or a name in the firstName middleName lastName format like so:

    myNameObject = Name("William","C","Wyatt") #first, middle, last name syntax
    myNameObject = Name(first="William",middle="C",last="Wyatt") #first, middle, last name syntax (same as above)
    
    myNameObject = Name.parse("William C Wyatt") #Using the basic parser
    
    print(myNameObject)
    # output: WILLIAM C WYATT


Once you have name as a name object you can compare it to other names like this,

    score = myNameObject.compare("William J Wyatt") #Will implicitly parse the name
    print(score) #Returns 3
    
    score = myNameObject.compare(Name("William","J","Wyatt")) #Explicitly defining the first, middle, last name
    print(score) #Returns 3

The parser is really rudimentary, if you have complex names, don’t use it; write your own parser and explicitly define the first middle and name name components. The file `NAME_MATCH_SCORE.json` will show you what each score from the compare function means.

In example.py I show how to use the Name class to do a comparison of all aliases and get the best batches and pull the column from it. It is `O(k)` computational complexity for each of `k` aliases or `O(kn)` given `n` names with `k` aliases.

Please let me know if you have any questions, I am trying to make this code a decent library.
