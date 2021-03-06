from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

import sys
if sys.platform.startswith("win"):
    import _locale
    # pylint: disable=protected-access
    _locale._getdefaultlocale = (lambda *args: ['en_US', 'utf8'])

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class TranslatorTest(StageTest):
    def generate(self):
        return [
            TestCase(stdin='fr\nhello\n'),
        ]

    def check(self, reply, attach):
        if '200 OK' not in reply:
            return CheckResult.wrong("There isn't internet connection identificator.")

        print(reply.count('['))
        print('Translation' in reply)

        if reply.count('[') >= 2 and 'Translation' in reply:
            return CheckResult.correct()

        return CheckResult.wrong("Try to print lists of translations in both "
                                 "stages or not to delete first word 'Translation' from it")


if __name__ == '__main__':
    TranslatorTest('translator.translator').run_tests()
