require_relative './src/application'

puts 'Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)'
original_extension = gets.chomp.strip

puts 'Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)'
target_extension = gets.chomp.strip

puts 'Provide d(dry_run: default) to make sure what directories and files are to be changed in the extensions first. Then, provide e(execution) if you would truly like to change the extensions. This operation is cannot be undone, so be alert to your operation!'
mode = gets.chomp.strip

params = { original_extension:, target_extension:, mode: }.reject { |_, value| value.empty? }

Application.run(**params)
