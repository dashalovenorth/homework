import pytest

from hw1 import statistics

TEST_CASE = (
        ('first_devesion', 
        {'Ana': 2000.0,
         'Sasha': 3000.0,
         'Katya': 5000.0
        }),
)



@pytest.mark.parametrize
def test_statistics():