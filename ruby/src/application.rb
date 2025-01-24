require 'fileutils'

class Application
  class InvalidModeError < StandardError; end

  def self.run(original_extension:, target_extension:, mode: 'd')
    instance = new(original_extension, target_extension, mode)
    instance.validate_mode!
    instance.run
  end

  def initialize(original_extension, target_extension, mode)
    @target_files     = Dir.glob(File.join('.', '**', "*#{original_extension}"))
    @target_extension = target_extension
    @mode             = mode
  end

  def validate_mode!
    case mode
    when 'd', 'e'
      return
    else
      raise InvalidModeError, "#{mode} is invalid mode. Provide either `d`(default) or `e`."
    end
  end

  def run
    output "Current Directory is #{File.absolute_path('.')}"
    if !target_files.empty?
      output "========== [#{exec_mode}] Total File Extensions Count to Convert: #{target_files.size} =========="
      output "========== [#{exec_mode}] Start Converting File Extensions =========="
      target_files.each { |target_file|
        FileUtils.mv(target_file, destination_file(target_file)) if mode == 'e'
        output "========== [#{exec_mode}] Converted File Extension: #{target_file} => #{destination_file(target_file)} =========="
      }
      output "========== [#{exec_mode}] Total Converted File Extensions Count: #{target_files.size} =========="
    else
      output "========== [#{exec_mode}] No File with #{original_extension} Remains =========="
    end
  end

  private

  attr_reader :target_files, :target_extension, :mode

  def exec_mode
    mode == 'e' ? 'EXECUTION' : 'DRY RUN'
  end

  def destination_file(target_file)
    "#{File.dirname(target_file)}/#{File.basename(target_file, '.*')}#{target_extension}"
  end

  def test_env?
    caller[-1].split('/').last.match?(/minitest\.rb/)
  end

  def output(message)
    puts message unless test_env?
  end
end
