# SQA Project Report

## Fuzzing
Since integrating a automated fuzzer into GitHub actions is a complicated task, we received permission to automatically run a manual fuzzer. The file fuzz.yml runs on every push (but requires manually updating of the fuzzer if one of the 5 changes) and manually fuzzes five methods (Average, Median, getFileLength, days_between, and getPythonFileCount) by running it against a variety of inputs. The results of each run can be seen in the "run-python-script" under the "Run Fuzzer" section. An example screenshot is shown below. The fuzzer revealed many common errors.

<img width="1350" height="824" alt="image" src="https://github.com/user-attachments/assets/17f28795-25d7-469f-b7fb-135124885074" />

The primary error in Average() and Median() were the lack of typing or data verification. Both operations are designed for numeric inputs but the lack of verification allow it be attempted with strings, None, empty, or different data types (Ex string and int). Additionally the Average includes division and does not check for division by zero.

The two methods based on file inputs (getFileLength() and getPythonFileCount()) have similar issues to each other as well. These issue primary stem also from a lack of verification or not handling errors from illegal files, illegal filepaths, or not handling empty or none inputs.

The main issue with days between is it requires a date data format and does not handle other forms like strings, none, ints, etc.

In summary, this simple fuzzing revealed that all methods (especially those in python) need to include inputs type verification and/or execption handling to account for corner cases that arise. Pythons dynamic typing of variables prevents guaranteeing that any method where a variable is a parameter from passing in a certain data type so type checks must be handled by the method itself versus the programmer. 

## Forensics
<img width="1153" height="898" alt="image" src="https://github.com/user-attachments/assets/cebd39d2-4453-4260-8464-00492b36983f" />


## Continuous Integration
<img width="1262" height="408" alt="image" src="https://github.com/user-attachments/assets/22d0785a-240d-42c7-b163-97d9e477828e" />

