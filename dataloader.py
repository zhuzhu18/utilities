import torch.utils.data as data
import numpy as np

class my_sampler(data.sampler.Sampler):
    def __init__(self, data_source, batch_size):
        self.data_size = len(data_source)
        self.sampler = iter(range(self.data_size))
        self.batch_size = batch_size

    def __iter__(self):
        batch = []
        for index in self.sampler:
            batch.append(index)
            if len(batch) == self.batch_size:
                yield batch
                batch = []
        if len(batch) != 0:
            yield batch

    def __len__(self):
        return (self.data_size + self.batch_size - 1) // self.batch_size

dataset = np.random.normal(0, 1, 100)
batch_sampler = my_sampler(dataset, 6)
data_loader = data.DataLoader(dataset, batch_sampler=batch_sampler)

for x in data_loader:
    print(x)
