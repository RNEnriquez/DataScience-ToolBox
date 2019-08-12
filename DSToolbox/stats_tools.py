import numpy as np

class Descriptive_Statistics:

    def __init__(self, data):
        self.data = list(data)

    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        self.data.sort()
        if len(self.data) % 2 != 0:
            idx = int((len(self.data) - 1) / 2)
            return self.data[idx]
        else:
            idx_1 = self.data[int((len(self.data) / 2))]
            idx_2 = self.data[int((len(self.data) / 2) - 1)]
            return (idx_1 + idx_2) / 2

    def mode(self):
        counts = {}
        unique_nums = set(self.data)
        for digit in unique_nums:
            counts[digit] = self.data.count(digit)
        if max(counts.values()) == 1:
            print("No Mode exists")
        else:
            for key, value in counts.items():
                if value == max(counts.values()):
                    return key

    def variance(self):
        self.data = np.array(self.data)
        return ((self.data - self.mean())**2).sum() / len(self.data)

    def standardDev(self):
        return self.variance()**(0.5)

    def coef_variation(self):
        return (self.standardDev() / self.mean()) * 100

    def summary(self):
        return {"Mean": self.mean(), "Median": self.median(),
                "Mode": self.mode(), "Variance": self.variance(),
                "StandardDeviation": self.standardDev(),
                "CoefficientOfVariation": self.coef_variation()}

class Inferential_Statistics:
    pass

class Bayesian_Statistics:
    pass
