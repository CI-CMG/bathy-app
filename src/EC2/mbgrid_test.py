"""
generate_grid.py

monitors SQS queue for messages requesting grid generation. Orchestrates the staging of data, execution of mbgrid,
staging of output, update of orders database table, and responding to step function
"""
import logging
import argparse
from os import path
from grid_task import GridTask


def main():
            try:
                # get order/dataset info from DynamoDB
                grid_params = {
                    'format': 3,
                    'resolution': 10,
                    'bbox': [-96.739, 26.712, -96.626, 26.792]
                }
                order_id = '52ac98d3-92e8-41bc-ab18-3637771b0f4e'
                csv_file = 'csb_sample/8aab940c-5fb4-40ed-a1df-cbea8467e874.csv'

                data_files = {
                 'csb': convert_csv_to_xyz(csv_file)
                }
                # prep input and execute mbgrid
                grid_task = GridTask(order_id, data_files, grid_params)
                grid_task.execute()
                logger.info("mbgrid execution complete")
                logger.debug(grid_task.stdout)

            except Exception as e:
                logger.error(e)
                logger.error('Failed to process message and will not retry')

        # wait before getting the next batch from the queue




def read_large_file(file_handler):
    for line in file_handler:
        yield line.strip()


def convert_csv_to_xyz(filename):
    """
    Convert incoming CSV file to XYZ optimized for MB-System processing.

    CSV file produced by Athena has quotes around all fields (including numeric
    ones) which mbgrid does not like.  Also strip out unnecessary attributes
    and standardize lon/lat coordinate precision to reduce file size and speed
    processing.

    :param filename: fully-qualified CSV filename downloaded from S3
    :return: fully-qualified file name of XYZ file
    """
    # file naming convention is "/path/to/file/<executionid>.csv"
    execution_id = filename.split('/')[-1].split('.')[0]
    output_filename = f'{INCOMING_DIR}{execution_id}.xyz'
    if path.exists(output_filename):
        logger.warning(f'WARNING: file {output_filename} already exists, no action taken')
        return output_filename

    output_file = open(output_filename, 'a')
    with open(filename) as file_handler:
        header = file_handler.readline()
        for line in read_large_file(file_handler):
            # pull out the first 3 values (x,y,z) and standardize precision
            values = [float(value.replace('"', '')) for value in line.split(',')[0:3]]
            # limit lon, lat precision to ~1.1m at equator
            values[0] = str(round(values[0], 5))
            values[1] = str(round(values[1], 5))
            values[2] = str(round(values[2], 1))
            output_file.write(','.join(values) + "\n")
    output_file.close()
    return output_filename


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    ch = logging.StreamHandler()
    logger.addHandler(ch)

    arg_parser = argparse.ArgumentParser(
        description="""monitor AWS queue and generate grid from CSB points and/or multibeam FBT files. Notify Step function when complete"""
    )
    arg_parser.add_argument("--profile", default="default", help="AWS profile")
    arg_parser.add_argument("--file", help="input CSV file")
    args = arg_parser.parse_args()

    INCOMING_DIR = '/home/ec2-user/incoming/'


    main()
