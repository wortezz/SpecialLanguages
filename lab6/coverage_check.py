import os
import sys
import unittest
import coverage

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../lab2")))

def main():

    cov = coverage.Coverage()
    cov.start()

    loader = unittest.TestLoader()
    test_folder = os.path.dirname(os.path.abspath(__file__))
    tests = loader.discover(test_folder, pattern="test_*.py")

    test_runner = unittest.TextTestRunner(verbosity=2)
    result = test_runner.run(tests)

    cov.stop()
    cov.save()

    print("\nCoverage Report:")
    cov.report(show_missing=True)

    if result.wasSuccessful():
        print("Усі тести пройшли успішно.")
    else:
        print("Є невдалі тести.")

if __name__ == "__main__":
    main()
