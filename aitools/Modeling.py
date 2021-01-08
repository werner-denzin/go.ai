from .Toolbox import Tool

class Train(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Train is ready!')

class Validate(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Validate is ready!')

class Evaluate(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Evaluate is ready!')