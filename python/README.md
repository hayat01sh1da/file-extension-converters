## 1. Environment

- Python 3.14.5

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ python main.py
Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): .rb
Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): .py
Provide d(dry_run: default) to make sure what directories and files are to be changed in the extensions first. Then, provide e(execution) if you would truly like to change the extensions. This operation is cannot be undone, so be alert to your operation!:

Current Directory is /mnt/c/Users/binlh/Documents/web/file-extensions-converter/ruby
========== [DRY RUN] Total File Extensions Count to Convert: 2 ==========
========== [DRY RUN] Start Converting File Extensions ==========
========== [DRY RUN] Converted File Extension: ./src/application.rb => ./src/application.py ==========
========== [DRY RUN] Converted File Extension: ./test/application_test.rb => ./test/application_test.py ==========
========== [DRY RUN] Total Converted File Extensions Count: 2 ==========
```

## 4. Unit Test

```command
$ pytest .
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: file-extension-converters/python
configfile: pyproject.toml
collected 5 items

test/test_application.py .....                                           [100%]

============================== 5 passed in 1.60s ===============================
```

## 5. Static Code Analysis

```command
$ flake8 .
./main.py:17:80: E501 line too long (83 > 79 characters)
./main.py:18:80: E501 line too long (83 > 79 characters)
./src/application.py:37:80: E501 line too long (84 > 79 characters)
./src/application.py:37:80: E501 line too long (84 > 79 characters)
./src/application.py:41:80: E501 line too long (88 > 79 characters)
./src/application.py:45:80: E501 line too long (82 > 79 characters)
./src/application.py:51:80: E501 line too long (91 > 79 characters)
./src/application.py:51:80: E501 line too long (91 > 79 characters)
./src/application.py:55:80: E501 line too long (83 > 79 characters)
./src/application.py:55:80: E501 line too long (83 > 79 characters)
./src/application.py:78:80: E501 line too long (88 > 79 characters)
./test/test_application.py:38:80: E501 line too long (82 > 79 characters)
$ autoflake8 --in-place --remove-duplicate-keys --remove-unused-variables --recursive .
$ autopep8 --in-place --aggressive --aggressive --recursive .
```

## 6. Type Check

```command
$ mypy .
Success: no issues found in 4 source files
```
