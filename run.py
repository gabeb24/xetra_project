"""Running the Xetra ETL application"""

import logging
import logging.config
import yaml

def main():
    """
    entrypoing to run the xetra ETL job
    """
    # Parsing YAML file
    config_path = "C:/programming/xetra_project/xetra_project/configs/xetra_report_1_config.yml"
    config = yaml.safe_load(open(config_path))

    # configure loggin
    log_config = config['logging']
    logging.config.dictConfig(log_config) # load our yaml file to a dictionary
    logger = logging.getLogger(__name__) # creates a logger using the name of our logger in the config file. 
    logger.info("This is a test.")

if __name__ == '__main__':
    main()