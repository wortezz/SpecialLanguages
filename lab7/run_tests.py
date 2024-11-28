import coverage
import unittest
import os

def main():
    cov = coverage.Coverage(source=['Commands', 'Core', 'UI'])
    cov.start()

    loader = unittest.TestLoader()
    test_folder = os.path.abspath('../Lab7/./tests')
    tests = loader.discover(test_folder)

    test_runner = unittest.TextTestRunner()
    test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\nCoverage Report:")
    cov.report(show_missing=True)

if __name__ == "__main__":
    main()
