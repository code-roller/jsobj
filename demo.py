from jsobj import JsObject

idealApple = JsObject({
    "crunchy": True,
    "juicy": True,
    "will_make_teeth_fall_out": False,
    "juice_level": 100
})

# Add attr
idealApple.addAttr("green", True)
print(idealApple)

# Change existing attr
idealApple.setAttr("juice_level", 75)
print(idealApple)

# Remove attr
idealApple.delAttr("will_make_teeth_fall_out")
print(idealApple)

# Get/refresh the object
appleObj = idealApple.getObj()
print(appleObj.crunchy)

# Add method
def applePrint():
    print("I love apples")

idealApple.addMethod(applePrint)
appleObj = idealApple.getObj()
appleObj.applePrint()