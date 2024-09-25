import unittest
from record_splitter import RecordSplitter
from fixtures import Fixtures

class TestRecordSplitterMethods(unittest.TestCase):
    def setUp(self):
        self.record_splitter = RecordSplitter(Fixtures.COUNT)
    
    def tearDown(self):
        del self.record_splitter

    def test_input_invalid(self):
        with self.assertRaises(TypeError):
            self.record_splitter = RecordSplitter([1,2,3])

    def test_set_max_record_size_invalid(self):
        with self.assertRaises(TypeError):
            self.record_splitter = RecordSplitter(Fixtures.COUNT)
            self.record_splitter.set_max_record_size("I am string")   

    def test_set_max_batch_size_invalid(self):
        with self.assertRaises(TypeError):
            self.record_splitter = RecordSplitter(Fixtures.COUNT)
            self.record_splitter.set_max_batch_size("I am string")    

    def test_set_max_record_number_per_batch_invalid(self):
        with self.assertRaises(TypeError):
            self.record_splitter = RecordSplitter(Fixtures.COUNT)
            self.record_splitter.set_max_record_number_per_batch("I am string")    

    def test_set_max_batch_size(self):
        self.record_splitter.set_max_batch_size(20)
        self.assertEqual(self.record_splitter.MAX_BATCH_SIZE, 20)

    def test_set_max_record_number_per_batch(self):
        self.record_splitter.set_max_record_number_per_batch(9)
        self.assertEqual(self.record_splitter.MAX_RECORD_NUMBER_PER_BATCH, 9)
  
    def test_set_max_record_size(self):
        self.record_splitter.set_max_record_size(3)
        self.assertEqual(self.record_splitter.MAX_RECORD_SIZE, 3)

    def test_get_list_size_in_bytes(self):
        self.assertEqual(self.record_splitter.get_list_size_in_bytes(['one', 'two', 'three', 'four', 'five']), 19)

    def test_get_string_size_in_bytes(self):
        self.assertEqual(self.record_splitter.get_string_size_in_bytes("hello"), 5)

    def test_get_list_size(self):
        self.assertEqual(self.record_splitter.get_list_size(['one', 'two', 'three', 'four', 'five']), 5)
   
    def test_generate(self):
        self.record_splitter.set_max_record_number_per_batch(5)
        self.assertEqual(self.record_splitter.generate(), [['one', 'two', 'three', 'four', 'five'],['six', 'seven', 'eight', 'nine', 'ten']])
        
class TestUseCases(unittest.TestCase):
    def setUp(self):
        self.record_splitter = RecordSplitter(Fixtures.BASE_SAMPLE)

    def tearDown(self):
        del self.record_splitter

    def test_sample_with_max_record(self):
        self.record_splitter = RecordSplitter(Fixtures.SAMPLE_WITH_MAX_RECORD)
        self.assertEqual(self.record_splitter.generate(), [["this_string_is_not_oversized_1", "this_string_is_not_oversized_2"]])

    def test_sample_with_max_batch(self):
        self.record_splitter = RecordSplitter(Fixtures.SAMPLE_WITH_MAX_BATCH)
        result = self.record_splitter.generate()
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[0][0]), 1000000)
        self.assertEqual(len(result[1][0]), 500000)

    def test_sample_with_max_entries(self):
        self.record_splitter = RecordSplitter(Fixtures.SAMPLE_WITH_501_ENTRIES)
        result = self.record_splitter.generate()
        self.assertEqual(len(result), 2)
        self.assertEqual(len(result[1][0]), 5)

    def test_sample_with_combination_of_entries(self):
        self.record_splitter = RecordSplitter(Fixtures.SAMPLE_COMBINATION)
        result = self.record_splitter.generate()
        self.assertEqual(len(result), 3) 
        self.assertEqual(len(result[0]), 6) # first batch contains 2 unfiltered record and maxed out batch size
        self.assertEqual(result[0][0], "this_string_is_not_oversized_1")
        self.assertEqual(result[0][1], "this_string_is_not_oversized_2")
        self.assertEqual(len(result[0][3]), 1000000)
        self.assertEqual(len(result[0][5]), 1000000)
        self.assertEqual(len(result[1]), 500) # second batch contains 2 unfiltered record and maxed out batch quantity
        self.assertEqual(len(result[1][0]), 1000000)
        self.assertEqual(len(result[1][1]), 500000)
        self.assertEqual(len(result[1][499]), 5)
        self.assertEqual(len(result[2]), 53) # third batch contains the rest of the random entries

if __name__ == '__main__':
    unittest.main()
