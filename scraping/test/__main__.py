from test import support

from scraping.test.test_yamls import TestYamls


def test_main():
    support.run_unittest(TestYamls)


if __name__ == "__main__":
    test_main()
