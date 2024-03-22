import pytest


# def sum (a:int, b:int)-> int:
#     return a+b

# @pytest.mark.parametrize(
#     argnames= "a,b,result",
#     argvalues= [
#         (1,2,3),
#         (2,2,4)
#     ]
# )

# def test_cenas(a,b,result):
#     assert sum(a,b) is result


def get_perimeter(a:int, b:int) -> int:
    return (2 * a) + (2 * b)


def get_area(a:int, b:int) -> int:
    return a * b; 


@pytest.mark.parametrize(
    argnames= "a,b,result",
    argvalues= [
        (2,4,12),
        (2,2,8)
    ]
)

def test_perimeter(a,b,result):
        assert get_perimeter(a,b) is result

def test_area(a,b,result):
     assert get_area(a,b) is result