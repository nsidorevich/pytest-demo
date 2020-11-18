import logging

import pytest

LOGGER = logging.getLogger('ui')

def test_passed():
    LOGGER.info('PASS')
    assert 1 == 1, 'is not as expected'


def test_failed():
    LOGGER.info('FAIL')
    assert 1 != 1, 'is not as expected'


@pytest.mark.skip(reason="skipping this")
def test_skipped():
    LOGGER.info('SKIP')
    assert 1 != 1, 'is not as expected'


@pytest.mark.xfail(reason="xfail: expected")
def test_xfailed():
    LOGGER.info('XFAIL')
    assert 1 != 1, 'is not as expected'
