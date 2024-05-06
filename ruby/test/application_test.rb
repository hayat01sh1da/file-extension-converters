require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @dirname = File.join('test', 'tmp')
    Dir.mkdir(dirname) unless Dir.exist?(dirname)
    @original_extension = '.txt'
    1.upto(100).each { |i| IO.write(File.join(dirname, "test_file_#{format('%03d', i)}#{original_extension}"), '') }
    @target_extension = '.md'
  end

  def test_run_in_dry_run_mode_1
    application = Application.run(original_extension:, target_extension:)
    assert_equal(Dir.glob(File.join(dirname, "*#{original_extension}")).size, 100)
    assert_equal(Dir.glob(File.join(dirname, "*#{target_extension}")).size, 0)
  end

  def test_run_in_dry_run_mode_2
    application = Application.run(original_extension:, target_extension:, mode: '-d')
    assert_equal(Dir.glob(File.join(dirname, "*#{original_extension}")).size, 100)
    assert_equal(Dir.glob(File.join(dirname, "*#{target_extension}")).size, 0)
  end

  def test_run_in_exec_mode
    application = Application.run(original_extension:, target_extension:, mode: '-e')
    assert_equal(Dir.glob(File.join(dirname, "*#{original_extension}")).size, 0)
    assert_equal(Dir.glob(File.join(dirname, "*#{target_extension}")).size, 100)
  end

  def teardown
    files_to_remove = Dir.glob(File.join(dirname, "*#{original_extension}")) | Dir.glob(File.join(dirname, "*#{target_extension}"))
    FileUtils.rm_rf(files_to_remove) if files_to_remove.any?
    Dir.delete(dirname)
  end

  private

  attr_reader :dirname, :original_extension, :target_extension
end
