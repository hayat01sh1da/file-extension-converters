# rbs_inline: enabled

require 'fileutils'

class Application
  class InvalidExtensionError < StandardError; end
  class InvalidModeError < StandardError; end

  # @rbs original_extension: String
  # @rbs target_extension: String
  # @rbs mode: String
  # @rbs return: void
  def self.run(original_extension: '', target_extension: '', mode: 'd')
    instance = new(original_extension:, target_extension:, mode:)
    instance.validate_extension!
    instance.validate_mode!
    instance.run
  end

  # @rbs original_extension: String
  # @rbs target_extension: String
  # @rbs mode: String
  # @rbs return: void
  def initialize(original_extension: '', target_extension: '', mode: 'd')
    @original_extension = original_extension
    @target_files       = Dir.glob(File.join('.', '**', "*#{original_extension}"))
    @target_extension   = target_extension
    @mode               = mode
  end

  # @rbs return: void
  def validate_extension!
    if !original_extension.start_with?('.') || !target_extension.start_with?('.')
      raise InvalidExtensionError, 'Provide a valid extension starting with `.`'
    end
  end

  # @rbs return: void
  def validate_mode!
    case mode
    when 'd', 'e'
      return
    else
      raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
    end
  end

  # @rbs return: void
  def run
    output "Current Directory is #{File.absolute_path('.')}"
    if !target_files.empty?
      output "========== [#{exec_mode}] Total File Extensions Count to Convert: #{target_files.length} =========="
      output "========== [#{exec_mode}] Start Converting File Extensions =========="
      target_files.each { |target_file|
        FileUtils.mv(target_file, destination_file(target_file)) if mode == 'e'
        output "========== [#{exec_mode}] Converted File Extension: #{target_file} => #{destination_file(target_file)} =========="
      }
      output "========== [#{exec_mode}] Total Converted File Extensions Count: #{target_files.length} =========="
    else
      output "========== [#{exec_mode}] No File with #{original_extension} Remains =========="
    end
  end

  private

  attr_reader :original_extension, :target_files, :target_extension, :mode

  # @rbs return: String
  def exec_mode
    @exec_mode ||= mode == 'e' ? 'EXECUTION' : 'DRY RUN'
  end

  # @rbs target_file: String
  # @rbs return: String
  def destination_file(target_file)
    "#{File.dirname(target_file)}/#{File.basename(target_file, '.*')}#{target_extension}"
  end

  # @rbs return: bool
  def test_env?
    caller[-1].split('/').last.match?(/minitest\.rb/)
  end

  # @rbs message: String
  # @rbs return: void
  def output(message)
    puts message unless test_env?
  end
end
