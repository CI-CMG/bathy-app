import unittest
from grid_task import GridTask


class MyTestCase(unittest.TestCase):
    def test_construct_commandline_args(self):
        datafiles = {
            'csb': '/Users/jcc/Downloads/210dd2f9-d781-4106-9f9d-b7f9a05b4502.xyz',
            'multibeam': '/Users/jcc/Downloads/8803e78e-5c20-408b-a3e7-e15b76aa29a6_mbfiles.txt'
        }
        gridTask = GridTask(1234, datafiles, {'bbox': [1, 2, 3, 4], 'resolution':30, 'format': 1})
        args = gridTask.get_commandline_args()
        self.assertEqual(len(args), 10)

    def test_execute(self):
        datafiles = {
            'csb': '/Users/jcc/Downloads/210dd2f9-d781-4106-9f9d-b7f9a05b4502.xyz',
            'multibeam': '/Users/jcc/Downloads/8803e78e-5c20-408b-a3e7-e15b76aa29a6_mbfiles.txt'
        }
        gridTask = GridTask(1234, datafiles, {'bbox': [1, 2, 3, 4], 'resolution':30, 'format': 1})
        gridTask.execute()
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
