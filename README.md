## 1. Common Environment

- WSL(Ubuntu 20.04.6 LTS)

## 2. READMEs

- [Ruby](./ruby/README.md)
- [Python](./python/README.md)

## 3. How to Use

In you terminal, provide the following 3 parameters via interactive user inputs.

- `original_extension`: The original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
- `target_extension`: The target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
- `mode`: The operation is done as the execution mode with `-e` and the dry_run mode without any option

### 3-1. For Ruby Lovers

```command
$ cd ./ruby/
$ ruby main.rb 
Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
.rb
Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
.py
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e(dry_run) once is strongly recommended

Current Directory is /mnt/c/Users/binlh/Documents/web/file-extensions-converter/ruby
========== [DRY RUN] Total File Extensions Count to Convert: 3 ==========
========== [DRY RUN] Start Converting File Extensions ==========
========== [DRY RUN] Converted File Extension: ./main.rb => ./main.py ==========
========== [DRY RUN] Converted File Extension: ./src/application.rb => ./src/application.py ==========
========== [DRY RUN] Converted File Extension: ./test/application_test.rb => ./test/application_test.py ==========
========== [DRY RUN] Total Converted File Extensions Count: 3 ==========
```

### 3-2. For Python Lovers

```command
$ cd ./python/
$ python main.py
Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): .py
Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): .rb
Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e(dry_run) once is strongly recommended:
Target dirname is /mnt/c/Users/binlh/Documents/web/file-extensions-converter/python
========== [DRY_RUN] Total File Extensions Count to Convert: 3 ==========
========== [DRY_RUN] Start Converting File Extensions
========== [DRY_RUN] Cleaning ./main.py ==========
========== [DRY_RUN] Converted File Extension: ./main.py => ./main.rb ==========
========== [DRY_RUN] Cleaning ./src/application.py ==========
========== [DRY_RUN] Converted File Extension: ./src/application.py => ./src/application.rb ==========
========== [DRY_RUN] Cleaning ./test/test_application.py ==========
========== [DRY_RUN] Converted File Extension: ./test/test_application.py => ./test/test_application.rb ==========
========== [DRY_RUN] Total Converted File Extensions Count: 3 ==========
```
