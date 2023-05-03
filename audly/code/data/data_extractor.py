def data_extractor():
    extractor = DATA_EXTRACTOR(extractor_function)
    return extractor
    
    
class DATA_EXTRACTOR:
    def __init__(self, extractor_function):
        self.extractor_function = extractor_function
        