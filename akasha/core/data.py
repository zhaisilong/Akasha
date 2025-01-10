from typing import List, Dict

import gzip
from akasha.core.constant import DATA_SOURCE_PATH

import yaml
from pathlib import Path
from loguru import logger
import pyarrow.csv as pc
import pyarrow.json as pj
import pyarrow.parquet as pp

class Data:
    def __init__(self, name: str, data_path: str, lazy: bool = False):
        self.name = name
        self.data_path = Path(data_path)
        self.lazy = lazy
        self.data = None
    
    def __str__(self):
        return f"Data(name={self.name}, data_path={self.data_path}, lazy={self.lazy}, data={self.data})"
    
    def load_data(self):
        suffix = self.data_path.suffix
        if suffix == ".gz":
            with gzip.open(self.data_path, "rb") as f:
                unzipped_data_path = self.data_path.with_suffix('')
                if unzipped_data_path.suffix == ".csv":
                    self.data = pc.read_csv(f)

        match suffix:
            case ".gz":
                with gzip.open(self.data_path, "rb") as f:
                    unzipped_data_path = self.data_path.with_suffix('')
                    if unzipped_data_path.suffix == ".csv":
                        self.data = pc.read_csv(f)
            case ".csv":
                self.data = pc.read_csv(self.data_path)
            case ".parquet":
                self.data = pp.read_table(self.data_path)
            case ".json":
                self.data = pj.read_json(self.data_path)
            case _:
                logger.error(f"Unsupported data type: {suffix}")
                return None
    
    @classmethod
    def load_from_info(cls, data_name: str, data_info: dict):
        assert "path" in data_info, "Data path is required"
        return cls(data_name, data_info.get("path", ""), data_info.get("lazy", False))


class DataSource:
    def __init__(self):
        self.data_source_path = Path(DATA_SOURCE_PATH)
        self.data_source = yaml.load(self.data_source_path.read_text(), Loader=yaml.FullLoader)

        logger.debug(f"data source: {self.dataset_list}")

    def __str__(self):
        return str(self.dataset_list)
        
    @property
    def dataset_list(self):
        return list(self.data_source.keys())
    
    def get_data_info(self, data_name: str):
        data_info = self.data_source[data_name]
        return data_info

    def _check_data_source(self, data_name: str):
        if data_name not in self.dataset_list:
            logger.error(f"Data source {data_name} not found")
            return False
        return True

    def load_data(self, data_name: str):
        if not self._check_data_source(data_name):
            return
        data_info = self.data_source[data_name]
        data = Data.load_from_info(data_name, data_info)
        return data
    