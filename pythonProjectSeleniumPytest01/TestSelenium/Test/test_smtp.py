import pytest
import smtplib

'''
https://docs.pytest.org/en/7.1.x/how-to/output.html
pytest --junitxml=test.xml

pip install pytest-reportlog
pytest --report-log=result.log
'''

@pytest.fixture
def smtp():
    return smtplib.SMTP("smtp.orange.fr")


def test_ehlo(smtp):
    response, msg = smtp.ehlo()
    assert response == 250
    # assert 0  # for demo purposes
