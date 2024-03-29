#GrapeJam
__all__ = ["dumps", "loads", "dump", "load"]
import json
from datetime import datetime

class GrapeJamError(Exception):
    def __init__(self, message):
        pass
def dumps(obj):
    if isinstance(obj, bytes):
        newlist = list(obj)
        return  f"?{json.dumps(newlist)[1:][:-1]}"
    elif isinstance(obj, bytearray):
        newlist = list(obj)
        return f"/{json.dumps(newlist)}"
    elif obj in [True, False]:
        return f"!{json.dumps(obj)}"
    elif isinstance(obj, int):
        return f"@{str(obj)}"
    elif isinstance(obj, str):
        return f"#{str(obj)}"
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            if isinstance(item, (list, tuple)): 
                obj[i] = [chr(7), dumps(item)]
        return f"${json.dumps(obj)}"
    elif isinstance(obj, tuple):
        obj = list(obj)
        for i, item in enumerate(obj):
            if isinstance(item, set): 
                obj[i] = ["*py-set-obj", list(item)]
            elif isinstance(item, tuple):
                obj[i] = ["*py-tuple-obj", list(item)]
        return f"%{json.dumps(obj)}"
    elif isinstance(obj, float):
        return f"^{json.dumps(obj)}"
    elif isinstance(obj, dict):
        return f"&{json.dumps(obj)}"
    elif obj == None:
        return "*N"
    elif isinstance(obj, range):
        return f"+{json.dumps(list(obj))}"
    elif isinstance(obj, complex):
        return f"-{str(obj)}"
    elif isinstance(obj, set):
        newlist = list(obj)
        return f"~{json.dumps(newlist)}"
    elif isinstance(obj, frozenset):
        newlist = list(obj)
        return f":{json.dumps(newlist)}"
    elif isinstance(obj, datetime):
        converted = obj.strftime("%Y\n%m\n%d\n%H\n%M\n%S\n%f").splitlines();
        return f"_{json.dumps(converted)}"
    else:
        raise GrapeJamError("problem processing object")
def loads(string):
    valid = '!@#$%^&*+-~:?/_'
    if string[0] not in valid:
        raise GrapeJamError("problem processing string")
    string = list(string)
    t = string.pop(0)
    string = "".join(string)
    if t == "!":
        return bool(json.loads(string))
    elif t == "@":
        return int(string)
    elif t == "#":
        return string
    elif t == "$":
        parsed = json.loads(string)
        for i, _obj in enumerate(parsed):
            if isinstance(_obj, list):
                if _obj[0] == chr(7):
                    parsed[i] = loads(_obj[1])
                else:
                    pass
        return parsed
    elif t == "%":
        parsed = json.loads(string)
        for i, _obj in enumerate(parsed):
            if isinstance(_obj, list):
                if _obj[0] == "py-set-obj":
                    parsed[i] = set(_obj[1])
                elif _obj[0] == "py-tuple-obj":
                    parsed[i] = tuple(_obj[1])
                else:
                    pass
        return tuple(parsed)
    elif t == "^" or t == "&":
        return json.loads(string)
    elif t == "*":
        if string == "*N":
            return None
        
    elif t == "+":
        m = json.loads(string)
        n = min(m)
        o = max(m) + 1
        return range(n, o)
    elif t == "-":
        return complex(string)
    elif t == "~":
        return set(json.loads(string))
    elif t == ":":
        return frozenset(json.loads(string))
    elif t == "?":
        return bytes(json.loads("[" + string + "]"))
    elif t == "/":
        return bytearray(json.loads(string))
    elif t == "_":
        a = json.loads(string)
        a = "-".join(a)
        return datetime.strptime(a, "%Y-%m-%d-%H-%M-%S-%f")
    else:
        raise GrapeJamError("problem processing string")
def dump(obj, file):
    stringified = dumps(obj)
    file.write(stringified)
def load(file):
    s = file.read()
    parsed = loads(s)
    return parsed
def test():
    a = dumps("hello")
    b = dumps(["mouse", [2, 8, 4, "string"], None, ("tuple",)])
    c = dumps(range(15))
    d = loads(a)
    e = loads(b)
    f = loads(c)
    for obj in a, b, c, "\n", d, e, f:
        print(obj)
    
if __name__ == "__main__":
    test()
