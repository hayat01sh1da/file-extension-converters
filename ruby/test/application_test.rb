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

  def teardown
    FileUtils.rm_rf(dirname) if Dir.exist?(dirname)
  end

  def test_run_in_dry_run_mode_1
    application = Application.run(original_extension:, target_extension:)
    assert_equal(100, Dir.glob(File.join(dirname, "*#{original_extension}")).size)
    assert_equal(0, Dir.glob(File.join(dirname, "*#{target_extension}")).size)
  end

  def test_run_in_dry_run_mode_2
    application = Application.run(original_extension:, target_extension:, mode: 'd')
    assert_equal(100, Dir.glob(File.join(dirname, "*#{original_extension}")).size)
    assert_equal(0, Dir.glob(File.join(dirname, "*#{target_extension}")).size)
  end

  def test_run_in_exec_mode
    application = Application.run(original_extension:, target_extension:, mode: 'e')
    assert_equal(0, Dir.glob(File.join(dirname, "*#{original_extension}")).size)
    assert_equal(100, Dir.glob(File.join(dirname, "*#{target_extension}")).size)
  end

  def test_invalid_mode
    error = assert_raises Application::InvalidModeError do
      Application.run(original_extension:, target_extension:, mode: 'a')
    end
    assert_equal('a is invalid mode. Provide either `d`(default) or `e`.', error.message)
  end

  private

  attr_reader :dirname, :original_extension, :target_extension
end
