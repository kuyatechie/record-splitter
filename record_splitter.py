import pprint
from fixtures import Fixtures

class RecordSplitter:
    def __init__(self, records):
        if isinstance(records, list) and all(isinstance(record, str) for record in records):
            self.records = records
        else:
            raise TypeError("Only list of strings are allowed")
        self.MAX_RECORD_SIZE = 1000000
        self.MAX_BATCH_SIZE = 5000000
        self.MAX_RECORD_NUMBER_PER_BATCH = 500
    
    def set_max_record_size(self, size):
        if isinstance(size, int):
            self.MAX_RECORD_SIZE = size
        else:
            raise TypeError("Only integer are allowed")
    
    def set_max_batch_size(self, size):
        if isinstance(size, int):
            if self.MAX_BATCH_SIZE < self.MAX_RECORD_SIZE:
                raise ValueError("Max Record Size is greater than Max Batch Size. Invalid setting.")
            self.MAX_BATCH_SIZE = size
        else:
            raise TypeError("Only integer are allowed")

    def set_max_record_number_per_batch(self, size):
        if isinstance(size, int):
            self.MAX_RECORD_NUMBER_PER_BATCH = size
        else:
            raise TypeError("Only integer are allowed")

    @staticmethod   
    def get_string_size_in_bytes(string):
        return len(string)
    
    @staticmethod
    def get_list_size_in_bytes(list):
        if len(list):
            return sum(len(string) for string in list)
        return 0

    @staticmethod
    def get_list_size(list):
        return len(list)

    def split_batch(self):
        batch=[]
        while self.get_list_size(self.records):
            if self.get_list_size(batch) >= self.MAX_RECORD_NUMBER_PER_BATCH:
                return batch
            record = self.records.pop(0)
            if self.get_string_size_in_bytes(record) <= self.MAX_RECORD_SIZE:
                batch.append(record)
            if self.get_list_size_in_bytes(batch) >= self.MAX_BATCH_SIZE:
                return batch
            if self.get_list_size(self.records):
                if self.get_list_size_in_bytes(batch) + self.get_string_size_in_bytes(self.records[0]) > self.MAX_BATCH_SIZE:
                    return batch
        return batch
            
    def generate(self):
        list_of_batch = []
        while self.get_list_size(self.records):
            batch = self.split_batch()
            if self.get_list_size(batch):
                list_of_batch.append(batch)
        return list_of_batch

