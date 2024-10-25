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
    puts "Current Directory is #{Dir.getwd}"
    if !target_files.empty?
      puts "========== [#{exec_mode}] Total File Extensions Count to Convert: #{target_files.size} =========="
      puts "========== [#{exec_mode}] Start Converting File Extensions =========="
      target_files.each { |target_file|
        FileUtils.mv(target_file, destination_file(target_file)) if mode == 'e'
        puts "========== [#{exec_mode}] Converted File Extension: #{target_file} => #{destination_file(target_file)} =========="
      }
      puts "========== [#{exec_mode}] Total Converted File Extensions Count: #{target_files.size} =========="
    else
      puts "========== [#{exec_mode}] No File with #{original_extension} Remains =========="
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
end
