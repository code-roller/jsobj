class JsObjectInstance(object):
    pass

class JsObject:
    def __init__(self, template: dict):
        self.template = template
        self.obj: JsObjectInstance = JsObjectInstance()
        

    
    def addAttr(self, attr: str, value: any):
        if attr not in self.template.keys():
            self.template[attr] = value
            self.obj.__setattr__(attr, value)
        else:
            print("Attribute already taken, please use JsObject.setAttr().")

    def addMethod(self, method):
        if method.__name__ not in self.template.keys():
            self.template[method.__name__] = method
            self.obj.__setattr__(method.__name__, method)
        else:
            print("Method already present.")
    
    def delAttr(self, attr: str):
        del self.template[attr]
        delattr(self.obj, attr)

    def setAttr(self, attr: str, value: any):
        if attr in self.template.keys():
            self.template[attr] = value
            setattr(self.obj, attr, value)
        else:
            print("Attribute not added, please use JsObject.addAttr().")

    def get(self):
        return self.obj

    def __repr__(self):
        return repr(self.template)