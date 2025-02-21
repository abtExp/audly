from audly.code.utils.base import BASE


def preprocess(process_y=False):
    def wrapper(preprocess_fn):
        preprocess = PREPROCESS(preprocess_fn, process_y)
        return preprocess
    return wrapper
    
    
class PREPROCESS(BASE):
    def __init__(self, preprocess_fn, process_y=False):
        self.preprocess_fn = preprocess_fn
        self.process_y = process_y
        
    def __call__(self, x, y):
        processed_x, processed_y = [], []
        for i in range(len(x)):
            processed_x.append(self.preprocess_fn(x[i]))
        
        if self.process_y:
            for i in range(len(y)):
                processed_y.append(self.preprocess_fn(y[i]))
        else:
            processed_y = y
            
        return processed_x, processed_y