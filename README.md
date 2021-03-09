# pyJsObject
 Javascript type objects in Python

# Usage
 To make a new `JsObject`:
 ```python
 import jsobj

 a = jsobj.JsObject({
    "first_letter": True, # `A` is the first letter of the alphabet
    "vowel": True, # `A` is a vowel
    "alphabet_position": 1, # `A` is the first letter of the alphabet
    "consonant": False, # `A` is not a consonant
    "examples_of_use": ["apple", "alkali", "algebra", "alligator", "acid"] # `A` is used in all these words
    "famous_example": "apple" # Out of all words, apple is the most well known that starts with `A`
})
 ```

 To add an attribute:
 ```python
 a.addAttr("in_hello", False) # adds the attribute `in_hello` and sets it to boolean `False`
 ```

 To change the value of an existing attribute:
 ```python
 a.setAttr("examples_of_use", ["apple", "alkali", "algebra", "alligator", "acid", "all"]) # changes the list of examples
 ```

 To delete an attribute:
 ```python
 a.delAttr("consonant") # deletes the consonant attribute
 ```

 To get the object:
 ```python
 a_object = a.getObj()
 ```
