'''
What all a data loader should do?
What all a data feeder should do?
What all an extractor should do?


Extractor : => Takes in the raw data source (i.e., a csv with file names, or a directory name etc.) 
            and extracts the feature and target raw values (file names, feature column, target column etc.)
            and returns the list of file names or feature column and target column name. It also extracts the size
            of the dataset. (Not responsible for data split, it simply reads the source and returns the feature and target sources)

Feeder : => Takes the config and reads the train, val and test data descriptions and passes each to the extractor and is the interface
            to the model which calls the data feeder based on the split, and the feeder simply calls the data loader for that split.
            It also maintains the indices for all data sets.
            
Loader : => gets the indices, loads the data, calls the preprocess and augment pipelines, obtains the batch with data split features
            and targets and returns the batch. Also responsible for splitting the processing into distributed processes.

'''
