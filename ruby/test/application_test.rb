# frozen_string_literal: true
# rbs_inline: enabled

require 'minitest/autorun'
require_relative '../src/application'

class ApplicationTest < Minitest::Test
  def setup
    @dirname = File.join('test', 'tmp')
    FileUtils.mkdir_p(dirname)
    @original_extension = '.png'
    1.upto(100).each { |i| File.write(File.join(dirname, "test_file_#{format('%03d', i)}#{original_extension}"), '') }
    @target_extension = '.jpg'
  end

  def teardown
    FileUtils.rm_rf(dirname)
  end

  def test_invalid_extension
    error = assert_raises Application::InvalidExtensionError do
      Application.run(original_extension: 'rb', target_extension:)
    end
    assert_equal('Provide a valid extension starting with `.`', error.message)
  end

  def test_invalid_mode
    error = assert_raises Application::InvalidModeError do
      Application.run(original_extension:, target_extension:, mode: 'a')
    end
    assert_equal('a is invalid mode. Provide either `d`(default) or `e`.', error.message)
  end

  def test_run_in_dry_run_mode_1
    Application.run(original_extension:, target_extension:)

    assert_equal(100, Dir.glob(File.join(dirname, "*#{original_extension}")).length)
    assert_equal(0, Dir.glob(File.join(dirname, "*#{target_extension}")).length)
  end

  def test_run_in_dry_run_mode_2
    Application.run(original_extension:, target_extension:, mode: 'd')

    assert_equal(100, Dir.glob(File.join(dirname, "*#{original_extension}")).length)
    assert_equal(0, Dir.glob(File.join(dirname, "*#{target_extension}")).length)
  end

  def test_run_in_exec_mode
    Application.run(original_extension:, target_extension:, mode: 'e')

    assert_equal(0, Dir.glob(File.join(dirname, "*#{original_extension}")).length)
    assert_equal(100, Dir.glob(File.join(dirname, "*#{target_extension}")).length)
  end

  private

  attr_reader :dirname, :original_extension, :target_extension
end
