class Hyperparameter:

    def __init__(self, epochs=200, learning_rate=1e-4,
                 data_path='',
                 label_path=''):
        self.epochs = epochs
        self.learning_rate = learning_rate
        self.data_path = data_path
        self.label_path = label_path
