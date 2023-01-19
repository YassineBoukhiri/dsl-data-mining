class MetricsBuilder: 

    def __init__(self):
        self.metrics = []
        self.all_metrics_ = ["accuracy", "loss"]
        self.used_metrics = []
        self.accuracy_used = False
        self.loss_used = False
    
    def accuracy(self):
        if self.accuracy_used:
            raise ValueError("ERROR: The accuracy can only be specified once.")
        self.metrics.append("accuracy")
        return self

    def loss(self):
        if self.loss_used:
            raise ValueError("ERROR: The loss can only be specified once.")
        self.metrics.append("loss")
        return self