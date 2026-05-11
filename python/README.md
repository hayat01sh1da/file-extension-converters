## 1. Environment

- Python 3.14.5

## 2. Install Libraries via requirements.txt

```command
$ pip install -r requirements.txt
```

## 3. Execution

```command
$ python main.py 
Provide the directory which contains files you would like to delete: .
Provide the dirname or filename pattern you would like to delete: *.py
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended:
Target dirname is /mnt/c/Users/binlh/Documents/web/file-cleaner/python
========== [DRY_RUN] Total File Count to Clean: 3 ==========
========== [DRY_RUN] Start Cleaning *.py ==========
========== [DRY_RUN] Cleaning ./main.py ==========
========== [DRY_RUN] Cleaning ./src/application.py ==========
========== [DRY_RUN] Cleaning ./test/test_application.py ==========
========== [DRY_RUN] Cleaned *.py ==========
========== [DRY_RUN] Total Cleaned File Count: 3 ==========
```

## 4. Unit Test

```command
$ pytest
============================= test session starts ==============================
platform linux -- Python 3.14.5, pytest-9.0.3, pluggy-1.6.0
rootdir: /mnt/c/Users/binlh/Documents/development/file-extension-converters/python
configfile: pyproject.toml
collected 5 items

test/test_application.py .....                                           [100%]

============================== 5 passed in 3.04s ===============================
