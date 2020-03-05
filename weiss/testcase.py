import logging
import re
import unittest

from weiss.mydict import Dict

logging.basicConfig(level=logging.INFO)


class TestDict(unittest.TestCase):

    def setUp(self) -> None:
        logging.info('===========')
        logging.info('setup...')

    def tearDown(self) -> None:
        logging.info('teardown...')

    def test_init(self):
        m = re.search('(?<=abc)def', 'abcdef')
        logging.info('m %s' % m)
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')
