import os
import pandas as pd
from parameters import read_params


class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.
    """
    def __init__(self, file_object, logger_object):
        self.config = read_params(config_path='config/params.yaml')
        self.training_file = os.path.join(self.config['data_preparation']['Training_FileFromDB'], self.config['data_preparation']['master_csv'])
        self.file_object = file_object
        self.logger_object = logger_object

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception
        """
        self.logger_object.log(self.file_object, 'Entered the get_data method of the Data_Getter class')
        try:
            self.data = pd.read_csv(self.training_file)  # reading the data file
            self.logger_object.log(self.file_object,
                                   'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,
                                   'Exception occurred in get_data method of the Data_Getter class. Exception message: '
                                   + str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()
