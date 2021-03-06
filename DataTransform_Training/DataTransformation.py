from os import listdir
import pandas
from application_logging.logger import App_Logger
from parameters import read_params


class dataTransform:
    """
    This class shall be used for transforming the Good Raw Training Data before loading it in Database!!.
    """

    def __init__(self):
        self.config = read_params(config_path='config/params.yaml')
        self.goodDataPath = self.config['data_preparation']['good_validated_raw_dir']
        self.logger = App_Logger()

    def replaceMissingWithNull(self):
        """
            Method Name: replaceMissingWithNull
            Description: This method replaces the missing values in columns with "NULL" to
                        store in the table. We are using substring in the first column to
                        keep only "Integer" data for ease up the loading.
                        This column is anyways going to be removed during training.
        """

        log_file = open("Training_Logs/dataTransformLog.txt", 'a+')
        try:
            onlyfiles = [f for f in listdir(self.goodDataPath)]
            for file in onlyfiles:
                csv = pandas.read_csv(self.goodDataPath + "/" + file)
                csv.fillna('NULL', inplace=True)
                csv['Wafer'] = csv['Wafer'].str[6:]
                csv.to_csv(self.goodDataPath + "/" + file, index=None, header=True)
                self.logger.log(log_file, " %s: File Transformed successfully!!" % file)

        except Exception as e:
            self.logger.log(log_file, "Data Transformation failed because:: %s" % e)
            log_file.close()
        log_file.close()
