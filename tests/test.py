from mypackage import myModule

def test_top_n():
    """ to make sute top_n works properly
    top_n(items,n)
    """

    assert myModule.top_n([8,2,3,7,4],3)==[8,7,4] , 'incorrect'
    assert myModule.top_n([10,1,12,9,2],2)==[12,10] , 'incorrect'
    assert myModule.top_n([1,2,3,4,5],5)==[5,4,3,2,1] , 'incorrect'