'''
Tema Sesiunea 10
Adaugati toate clasele de test create la sesiunea 9 intr-o suita de teste
Definiti in acea suita raportul html
Rulati suita de teste si analizati rezultatele
'''

import unittest

import HtmlTestRunner

from tema9_unittest_elefant_ro.class_contact import Contact
from tema9_unittest_elefant_ro.class_login import Login
from tema9_unittest_elefant_ro.class_search import Search


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test_tema10 = unittest.TestSuite()
        smoke_test_tema10.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Contact),
            unittest.defaultTestLoader.loadTestsFromTestCase(Search)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='report1_elefant', report_name='Smoke Test Tema 10', combine_reports=True
        )
        runner.run(smoke_test_tema10)
