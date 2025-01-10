from absl import app, flags
from akasha.core.data import DataSource, Data
from loguru import logger

FLAGS = flags.FLAGS

flags.DEFINE_string('data_name', 'sample_data', 'The data name to load')

def main(argv):
    data_source = DataSource()
    data: Data = data_source.load_data(FLAGS.data_name)
    data.load_data()
    logger.debug(f"data: {data}")
    
    data_info = data_source.get_data_info(FLAGS.data_name)
    logger.debug(f"data info: {data_info}")

if __name__ == "__main__":
    app.run(main)
