"""ETL Components"""

from typing import NamedTuple
from src.common.s3 import S3BucketConnector
import logging

class XetraSourceConfig(NamedTuple):
    """
    Class for source configuration data
    These are the expected data types of the names of our columns

    src_first_extract_date: determines the date data was extracted from source
    src_columns: source column names
    src_col_date: column name for 'date' in source
    src_col_isin: column name for 'isin' in source
    src_col_time: column name for 'time' in source
    src_col_start_price: column name for 'starting_price' in source
    src_col_min_price: column name for 'minimum price' in source
    src_col_max_price: column name for 'maximum price' in source
    src_col_traded_vol: column name for 'traded volume' in source
    """

    src_first_extract_date: str
    src_columns: list
    src_col_date: str
    src_col_isin: str
    src_col_time: str
    src_col_start_price: str
    src_col_min_price: str
    src_col_max_price: str
    src_col_traded_vol: str

class XetraTargetConfig(NamedTuple):
    """
    Class for source configuration data
    These are the expected data types of the names of our columns

    trg_col_isin: column name for 'isin' in target
    trg_col_date: column name for 'date' in target
    trg_col_opening_price: column name for 'opening_price' in target
    trg_col_closing_price: column name for 'closing_price' in target
    trg_col_min_price: column name for 'minimum price' in target
    trg_col_max_price: column name for 'maximum price' in target
    trg_col_dail_trad_vol: column name for 'daily traded volume' in target
    trg_col_change_prev_close: column name for c'change to previous day closing price' in target
    trg_key: basic key of target file
    trg_key_date_format: date format of the target file key
    trg_format: file format of the target file
    """

    trg_col_isin: str
    trg_col_date: str
    trg_col_opening_price: str
    trg_col_closing_price: str
    trg_col_min_price: str
    trg_col_max_price: str
    trg_col_dail_trad_vol: str
    trg_col_change_prev_close: str
    trg_key: str
    trg_key_date_format: str
    trg_format: str

class XetraETL():
    """
    Reads Xetra data, transforms data, writes the transformed data to target
    """

    def __init__(self, s3_bucket_src: S3BucketConnector,
                s3_bucket_trg: S3BucketConnector, meta_key: str,
                src_args: XetraSourceConfig, trg_args: XetraTargetConfig):

        """
        Constructor for XetraTransformer
        :param s3_bucket_src: connection to source s3 bucket
        :param s3_bucket_trg: connection to target S3 bucket
        :param meta_key: used as self.meta_key -> key/location of meta file
        :param src_args: NamedTuple class with source configuration data
        :param trg_args: NamedTuple class with target configuration data
        """
        self._logger = logging.getLogger(__name__)
        self.s3_bucket_src = s3_bucket_src
        self.s3_bucket_trg = s3_bucket_trg
        self.meta_key = meta_key
        self.src_args = src_args
        self.trg_args = trg_args
        self.extract_date = 
        self.extract_date_list = 
        self.meta_update_list =

    def extract(self):
        pass

    def transform_report1(self):
        pass

    def load(self):
        pass

    def etl_report1(self):
        pass
 
