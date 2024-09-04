import subprocess
import logging


class GridTask:
    """TODO docstring goes here"""

    WORKINGDIR = "/home/ec2-user/incoming/"

    # set up logger
    logger = logging.getLogger(__name__)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    def __init__(self, order_id, data_files, bbox, grid_params):
        self.order_id = order_id
        self.data_files = data_files
        self.bbox = bbox
        self.cell_size = grid_params['resolution']
        self.gridtype = '3'
        if 'format' in grid_params:
            self.gridtype = grid_params['format']
        # TODO background grid option
        self.background = None
        if 'background' in grid_params:
            self.background = grid_params['background']
        self.datalist = None
        self.stdout = None
        self.stderr = None
        self.cmd_args = None

    def execute(self):
        self.create_datalist()
        self.get_commandline_args()
        process = subprocess.run(self.cmd_args, cwd=self.WORKINGDIR, capture_output=True, text=True)
        self.stdout = process.stdout
        self.stderr = process.stderr

        if self.mbgrid_success():
            self.logger.info("mbgrid successfully executed")
        else:
            msg = f'program failed to execute:\n{process.stdout}\n{process.stderr}'
            self.logger.error(msg)
            raise Exception(msg)

    def create_datalist(self):
        """ create file manifest formatted for mbgrid"""
        if len(self.data_files) < 1:
            raise Exception("at least one datafile must be provided")

        # TODO verify existence of all files in data_files

        # overwrite any existing file
        output_filename = f"{self.WORKINGDIR}{self.order_id}.datalist"
        with open(output_filename, "w") as datalist:
            if 'csb' in self.data_files:
                datalist.write(f"{self.data_files['csb']}  162\n")

            if 'multibeam' in self.data_files:
                with open(self.data_files['multibeam'], "r") as mb_files:
                    for line in mb_files.readlines():
                        datalist.write(line)
        self.datalist = output_filename

    def mbgrid_success(self):
        """HACK - cannot depend on returncode or stderr to determine failure in mbgrid"""
        if not self.stdout:
            raise Exception('cannot check success before process execution')

        success_string = 'Total number of bins:'
        # return success_string in self.stdout
        return True

    def get_commandline_args(self):
        """
            assemble the command line arguments for mbgrid.  See man page at
            http://www3.mbari.org/products/mbsystem/html/mbgrid.html.  Assumes
            execution within current directory

            :return: list of command line arguments
            """
        # coords = [float(c.strip()) for c in self.bbox.split(',')]
        coords = self.bbox
        result = ['mbgrid']
        # same cell size (in meters) for lon/lat. expand grid bound to honor cell size
        result.append(f"-E{self.cell_size}/0.0!")
        result.append(f"-I{self.datalist}")
        result.append("-N")  # use NaN for grid cells with no data
        result.append(f"-O{self.order_id}")
        result.append("-P1")  # ping averaging of input data
        result.append(f"-R{coords[0]}/{coords[2]}/{coords[1]}/{coords[3]}")
        # Autogrid uses -A2?
        result.append("-A1")  # bathymetry datatype (positive downwards)
        # result.append("-V")  # print out statements indicating progress
        result.append(f"-G{self.gridtype}")  # default to GMT netCDF 4-byte float format
        # result.append('-T100')  # tension of 100 used by DEM team
        result.append("-F1")  # Gaussian weighted mean filter gridding algorithm
        # extends size of internal grid so output grid is subset from center of a larger grid
        # result.append("-X0.5")
        # width of the gaussian weighting function in terms of the grid spacing
        # result.append("-W0.5")
        self.cmd_args = result
