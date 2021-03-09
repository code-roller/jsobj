from jsobj import JsObject

idealApple = JsObject({
    "crunchy": True,
    "juicy": True,
    "will_make_teeth_fall_out": False,
    "juice_level": 100
})

idealApple.addAttr("green", True)
print(idealApple)

idealApple.setAttr("juice_level", 75)
print(idealApple)

idealApple.delAttr("will_make_teeth_fall_out")
print(idealApple)

print(idealApple.getObj())