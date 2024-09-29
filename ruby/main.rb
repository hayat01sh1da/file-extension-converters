require_relative './src/application'

puts 'Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)'
original_extension = gets.chomp

puts 'Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)'
target_extension = gets.chomp

puts 'Provide -e(execution) if you would truly like to delete the files. This operation is cannot be undone, so trying to run without -e once is strongly recommended'
mode = gets.chomp

Application.run(original_extension:, target_extension:, mode:)
