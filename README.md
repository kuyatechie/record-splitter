# record-splitter
A library to split record using different parameters

## Prerequisite
Linux Environment
Python 3.10+

## How to test (using unittest)
Testing is defined in test_record_splitter.py
Sample fixtures used in the code are in fixtures.py

$ python -m unittest test_record_splitter.py -v
test_generate (test_record_splitter.TestRecordSplitterMethods) ... ok
test_get_list_size (test_record_splitter.TestRecordSplitterMethods) ... ok
test_get_list_size_in_bytes (test_record_splitter.TestRecordSplitterMethods) ... ok
test_get_string_size_in_bytes (test_record_splitter.TestRecordSplitterMethods) ... ok
test_input_invalid (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_batch_size (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_batch_size_invalid (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_record_number_per_batch (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_record_number_per_batch_invalid (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_record_size (test_record_splitter.TestRecordSplitterMethods) ... ok
test_set_max_record_size_invalid (test_record_splitter.TestRecordSplitterMethods) ... ok
test_sample_with_combination_of_entries (test_record_splitter.TestUseCases) ... ok
test_sample_with_max_batch (test_record_splitter.TestUseCases) ... ok
test_sample_with_max_entries (test_record_splitter.TestUseCases) ... ok
test_sample_with_max_record (test_record_splitter.TestUseCases) ... ok

----------------------------------------------------------------------
Ran 15 tests in 0.016s

OK
