import logging

import pytest

LOGGER = logging.getLogger('demo')


@pytest.mark.alex
def test_passed():
    LOGGER.info('Sample log 001')
    LOGGER.info('Sample log 002')
    LOGGER.info('Sample log 003')
    assert 1 == 1, 'is not as expected'


def test_failed():
    LOGGER.info('FAIL :(')
    assert 1 != 1, 'is not as expected'


@pytest.mark.skip(reason="skipping this")
def test_skipped():
    LOGGER.info('SKIP')
    assert 1 != 1, 'is not as expected'

@pytest.mark.dmishin
@pytest.mark.xfail(reason="xfail: expected")
def test_xfailed():
    LOGGER.info('XFAIL')
    assert 1 != 1, 'is not as expected'
