from unittest import mock
import time




class Mock:
    def __init__(self):
        self.mock_method = mock.Mock(
            return_value = {'returnState':{
                'stateCode':0,
                'errorMsg':'something went wrong'}}
        )

    def main(self,method,url,data=None,header=None):
        print(data)
        return self.mock_method(method,url,data,header)
