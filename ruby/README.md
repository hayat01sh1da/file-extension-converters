## 1. Environment

- Ruby 4.0.5

## 2. Install Gems via Gemfile and Bundler

```command
$ bundle install
$ bundle lock --add-checksums
```

## 3. Execution

```command
$ rake run_file_extension_converter
Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
.rb
Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)
.py
Provide d(dry_run: default) to make sure what directories and files are to be changed in the extensions first. Then, provide e(execution) if you would truly like to change the extensions. This operation is cannot be undone, so be alert to your operation!

Current Directory is /mnt/c/Users/binlh/Documents/web/file-extensions-converter/ruby
========== [DRY RUN] Total File Extensions Count to Convert: 2 ==========
========== [DRY RUN] Start Converting File Extensions ==========
========== [DRY RUN] Converted File Extension: ./src/application.rb => ./src/application.py ==========
========== [DRY RUN] Converted File Extension: ./test/application_test.rb => ./test/application_test.py ==========
========== [DRY RUN] Total Converted File Extensions Count: 2 ==========
```

## 4. Unit Test

```command
$ rake
Run options: --seed 55190

# Running:

.....

Finished in 10.130123s, 0.4936 runs/s, 0.9872 assertions/s.

5 runs, 10 assertions, 0 failures, 0 errors, 0 skips
```

## 5. Static Code Analysis

```command
$ rubocop
Inspecting 5 files
.....

5 files inspected, no offenses detected
```

## 6. Type Check

```command
$ rbs-inline --output sig/generated/ .
🎉 Generated 2 RBS files under sig/generated
$ steep check
# Type checking files:

....

No type error detected. 🍵
```
