from test import support

from scraping.test.test_yamls import VerifyClassesYaml


def test_main():
    support.run_unittest(VerifyClassesYaml)


if __name__ == "__main__":
    test_main()
