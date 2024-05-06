require_relative './src/application'

original_extension, target_extension, mode, *_ = ARGV
Application.run(original_extension:, target_extension:, mode:)
