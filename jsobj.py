class JsObjectInstance(object):
    pass

class JsObject:
    def __init__(self, template: dict):
        self.template = template
        self.obj: Object = JsObjectInstance()
        i = 0
        while i < len(self.template.keys()):
            setattr(self.obj, list(self.template.keys())[i], list(self.template.values())[i])
            i += 1
    
    def addAttr(self, attr: str, value: any):
        if attr not in self.template.keys():
            self.template[attr] = value
            self.obj.__setattr__(attr, value)
        else:
            print("Attribute already taken, please use JsObject.setAttr()")
    
    def delAttr(self, attr: str):
        del self.template[attr]
        delattr(self.obj, attr)

    def setAttr(self, attr: str, value: any):
        if attr in self.template.keys():
            self.template[attr] = value
            setattr(self.obj, attr, value)
        else:
            print("Attribute not added, please use JsObject.addAttr()")

    def getObj(self):
        return self.obj

    def __repr__(self):
        return repr(self.template)