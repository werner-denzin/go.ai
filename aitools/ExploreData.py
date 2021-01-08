from .Toolbox import Tool

class Fetch(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Fetch is ready!')        

class Clean(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Clean is ready!')     

class Prepare(Tool):
    
    def __init__(self):
        Tool.__init__(self)
        print('Prepare is ready!')