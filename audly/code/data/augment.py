from audly.utils.base import BASE


def augmentation(prob=0.5, augment_y=False):
    def wrapper(augment_fn):
        augmentation = AUGMENTATION(augment_fn, apply_prob, augment_y)
        return augmentation
    return wrapper
    
    
class AUGMENTATION(BASE):
    def __init__(self, augment_fn, apply_prob, augment_y):
        self.augment_fn = augment_fn
        self.apply_prob = apply_prob
        self.augment_y = augment_y
        
    def __call__(self, x, y, run_y=False):
        augmented_x, augmented_y = [], []
        for i in range(len(x)):
            augmented_x.append(self.augment_fn(x[i]))
        
        if self.augment_y:
            for i in range(len(y)):
                augmented_y.append(self.augment_fn(y[i]))
        else:
            augmented_y = y
            
        return augmented_x, augmented_y