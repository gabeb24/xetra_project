"""
File that stores and defines constants
"""

from enum import Enum

class S3FileTypes(Enum):
    """
    supported file types for S3Bucket Connectors
    """
    CSV = 'csv'
    PARQUET = 'parquet'

class MetaProcessFormat(Enum):
    """
    formation for MetaProcess class
    """
    meta_date_format = '%Y-%m-%d'
    meta_process_date_format = "%Y-%m-%d_%H:%M:%S"
    meta_process_date_col = 'source_date'
    meta_process_col = 'datetime_of_processing'
    meta_file_format = 'csv'