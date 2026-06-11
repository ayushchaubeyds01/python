# from calc import square
# def main():
#     test_square()
# def test_square():
#     # try :
#     #     assert square(2)==4
#     # except:
#     #     print("2 sqared is not 4")
#     # try :
#     #     assert square(3)==9
#     # except:
#     #     print("3 sqared is not 9")
#     # try :
#     #     assert square(-2)==4
#     # except:
#     #     print("-2 sqared is not 4")
#     # try :
#     #     assert square(0)==0
#     # except:
#     #     print("0 sqared is not 0")
# if __name__=="__main__":
#     main()
    
    
    
    ### it increases no of lines of code so we use a library called pytest
    
import pytest
from calc import square
def main():
    test_square()
def test_square():
    assert square(2)==4
    assert square(3)==9
    assert square(-2)==4
    assert square(0)==0
