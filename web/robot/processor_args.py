import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--notebook'
                    ,action='store_true'
                    ,help='Set this flag to output to a Jupyter Notebook instead of a .py file'
                    )
parser.add_argument('--palette', '-pa'
                    ,default='corning_96_wellplate_360ul_flat'
                    ,help='Optional argument to specify the kind of labware to use as the palette plate. Use Opentrons standard names.'
                    )
parser.add_argument('--pipette', '-pi'
                    ,default='p10_single'
                    ,help='Optional argument to specify the pipette type. Use Opentrons standard names.'
                    )

args = vars(parser.parse_args())