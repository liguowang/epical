#!/usr/bin/env python

import sys
# import logging
import argparse
from dmc._version import __version__
from dmc import helpdoc
from dmc.clock_info import clockinfo
from dmc import methylclocks
from dmc.utils import config_log

__author__ = "Liguo Wang"
__copyright__ = "Copyleft"
__credits__ = []
__license__ = "MIT"
__maintainer__ = "Liguo Wang"
__email__ = "wang.liguo@mayo.edu"
__status__ = "Development"


def epical():
    """
    Invoke various functions to calculate the DNA methylation age.
    """
    general_help = helpdoc.general_help

    # sub commands and help.
    commands = {
        'Horvath13': clockinfo('Horvath13.pkl'),
        'Horvath13_shrunk': clockinfo('Horvath13_shrunk.pkl'),
        'Horvath18': clockinfo('Horvath18.pkl'),
        'Levine': clockinfo('Levine.pkl'),
        'Hannum': clockinfo('Hannum.pkl'),
        'Zhang_EN': clockinfo('Zhang_EN.pkl'),
        'Zhang_BLUP': clockinfo('Zhang_BLUP.pkl'),
        'AltumAge': clockinfo('AltumAge_cpg.pkl'),
        'Lu_DNAmTL': clockinfo('Lu_DNAmTL.pkl'),

        'Ped_Wu': clockinfo('Ped_Wu.pkl'),
        'PedBE': clockinfo('Ped_McEwen.pkl'),

        'GA_Bohlin': clockinfo('GA_Bohlin.pkl'),
        'GA_Haftorn': clockinfo('GA_Haftorn.pkl'),
        'GA_Knight': clockinfo('GA_Knight.pkl'),
        'GA_Mayne': clockinfo('GA_Mayne.pkl'),
        'GA_Lee_CPC': clockinfo('GA_Lee_CPC.pkl'),
        'GA_Lee_RPC': clockinfo('GA_Lee_RPC.pkl'),
        'GA_Lee_rRPC': clockinfo('GA_Lee_refined_RPC.pkl'),

        'Cortical': clockinfo('CorticalClock.pkl'),
        'MEAT': clockinfo('MEAT.pkl'),
        'EPM': helpdoc.epm_help,

        'WLMT': clockinfo('WLMT_mm10.pkl'),
        'YOMT': clockinfo('YOMT_mm10.pkl'),
        'mmLiver': clockinfo('liver_mm10.pkl'),
        'mmBlood': clockinfo('blood_mm10.pkl')
         }

    # create parse
    parser = argparse.ArgumentParser(
        description=general_help, epilog='',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
        )
    parser.add_argument(
        '-v', '--version', action='version', version='%s %s' %
        ('epical', __version__)
        )

    # create sub-parser
    sub_parsers = parser.add_subparsers(help='Sub-command description:')
    parser_Horvath13 = sub_parsers.add_parser(
        'Horvath13', help=commands['Horvath13']
        )
    parser_Horvath13_shrunk = sub_parsers.add_parser(
        'Horvath13_shrunk', help=commands['Horvath13_shrunk']
        )
    parser_Horvath18 = sub_parsers.add_parser(
        'Horvath18', help=commands['Horvath18']
        )
    parser_Levine = sub_parsers.add_parser(
        'Levine', help=commands['Levine']
        )
    parser_Hannum = sub_parsers.add_parser(
        'Hannum', help=commands['Hannum']
        )
    parser_Zhang_EN = sub_parsers.add_parser(
        'Zhang_EN', help=commands['Zhang_EN']
        )
    parser_Zhang_BLUP = sub_parsers.add_parser(
        'Zhang_BLUP', help=commands['Zhang_BLUP']
        )
    parser_AltumAge = sub_parsers.add_parser(
        'AltumAge', help=commands['AltumAge']
        )
    parser_Lu_DNAmTL = sub_parsers.add_parser(
        'Lu_DNAmTL', help=commands['Lu_DNAmTL']
        )
    parser_Ped_Wu = sub_parsers.add_parser(
        'Ped_Wu', help=commands['Ped_Wu']
        )
    parser_PedBE = sub_parsers.add_parser(
        'PedBE', help=commands['PedBE']
        )
    parser_GA_Bohlin = sub_parsers.add_parser(
        'GA_Bohlin', help=commands['GA_Bohlin']
        )
    parser_GA_Haftorn = sub_parsers.add_parser(
        'GA_Haftorn', help=commands['GA_Haftorn']
        )
    parser_GA_Knight = sub_parsers.add_parser(
        'GA_Knight', help=commands['GA_Knight']
        )
    parser_GA_Mayne = sub_parsers.add_parser(
        'GA_Mayne', help=commands['GA_Mayne']
        )
    parser_GA_Lee_CPC = sub_parsers.add_parser(
        'GA_Lee_CPC', help=commands['GA_Lee_CPC']
        )
    parser_GA_Lee_RPC = sub_parsers.add_parser(
        'GA_Lee_RPC', help=commands['GA_Lee_RPC']
        )
    parser_GA_Lee_rRPC = sub_parsers.add_parser(
        'GA_Lee_rRPC', help=commands['GA_Lee_rRPC']
        )
    parser_Cortical = sub_parsers.add_parser(
        'Cortical', help=commands['Cortical']
        )
    parser_EPM = sub_parsers.add_parser(
        'EPM', help=commands['EPM']
        )
    parser_MEAT = sub_parsers.add_parser(
        'MEAT', help=commands['MEAT']
        )
    parser_WLMT = sub_parsers.add_parser(
        'WLMT', help=commands['WLMT']
        )
    parser_YOMT = sub_parsers.add_parser(
        'YOMT', help=commands['YOMT']
        )
    parser_mmLiver = sub_parsers.add_parser(
        'mmLiver', help=commands['mmLiver']
        )
    parser_mmBlood = sub_parsers.add_parser(
        'mmBlood', help=commands['mmBlood']
        )

    # create the parser for the 'Horvath13' sub-command
    parser_Horvath13.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Horvath13.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Horvath13.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Horvath13.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Horvath13.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Horvath13.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Horvath13.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Horvath13.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Horvath13.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Horvath13.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')
    parser_Horvath13.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'Horvath13_shrunk' sub-command
    parser_Horvath13_shrunk.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Horvath13_shrunk.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Horvath13_shrunk.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Horvath13_shrunk.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Horvath13_shrunk.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Horvath13_shrunk.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Horvath13_shrunk.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Horvath13_shrunk.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Horvath13_shrunk.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Horvath13_shrunk.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')
    parser_Horvath13_shrunk.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'MEAT' sub-command
    parser_MEAT.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_MEAT.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_MEAT.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_MEAT.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_MEAT.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_MEAT.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_MEAT.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_MEAT.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_MEAT.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_MEAT.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')
    parser_MEAT.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'Horvath18' sub-command
    parser_Horvath18.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Horvath18.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Horvath18.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Horvath18.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Horvath18.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Horvath18.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Horvath18.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Horvath18.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Horvath18.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Horvath18.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')
    parser_Horvath18.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'PedBE' sub-command
    parser_PedBE.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_PedBE.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_PedBE.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_PedBE.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_PedBE.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_PedBE.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_PedBE.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_PedBE.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_PedBE.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_PedBE.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_PedBE.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Levine' sub-command
    parser_Levine.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Levine.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Levine.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Levine.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Levine.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Levine.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Levine.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Levine.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Levine.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Levine.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_Levine.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Hannum' sub-command
    parser_Hannum.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Hannum.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Hannum.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Hannum.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Hannum.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Hannum.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Hannum.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Hannum.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Hannum.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Hannum.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_Hannum.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Lu_DNAmTL' sub-command
    parser_Lu_DNAmTL.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Lu_DNAmTL.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Lu_DNAmTL.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Lu_DNAmTL.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Lu_DNAmTL.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Lu_DNAmTL.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Lu_DNAmTL.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Lu_DNAmTL.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Lu_DNAmTL.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Lu_DNAmTL.add_argument(
        '--debug', action='store_true',
        help='Print detailed information for debugging.')
    parser_Lu_DNAmTL.add_argument(
        '--overwrite', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'Zhang_BLUP' sub-command
    parser_Zhang_BLUP.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Zhang_BLUP.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Zhang_BLUP.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Zhang_BLUP.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Zhang_BLUP.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Zhang_BLUP.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Zhang_BLUP.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Zhang_BLUP.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Zhang_BLUP.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Zhang_BLUP.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_Zhang_BLUP.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Zhang_EN' sub-command
    parser_Zhang_EN.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Zhang_EN.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Zhang_EN.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Zhang_EN.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Zhang_EN.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Zhang_EN.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Zhang_EN.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Zhang_EN.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Zhang_EN.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Zhang_EN.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_Zhang_EN.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Knight' sub-command
    parser_GA_Knight.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Knight.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Knight.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Knight.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Knight.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Knight.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Knight.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Knight.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Knight.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Knight.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Knight.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Mayne' sub-command
    parser_GA_Mayne.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Mayne.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Mayne.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Mayne.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Mayne.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Mayne.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Mayne.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Mayne.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Mayne.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Mayne.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Mayne.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Bohlin' sub-command
    parser_GA_Bohlin.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Bohlin.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Bohlin.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Bohlin.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Bohlin.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Bohlin.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Bohlin.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Bohlin.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Bohlin.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Bohlin.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Bohlin.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Haftorn' sub-command
    parser_GA_Haftorn.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Haftorn.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Haftorn.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Haftorn.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Haftorn.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Haftorn.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Haftorn.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Haftorn.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Haftorn.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Haftorn.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Haftorn.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Lee_CPC' sub-command
    parser_GA_Lee_CPC.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Lee_CPC.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Lee_CPC.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Lee_CPC.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Lee_CPC.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Lee_CPC.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Lee_CPC.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Lee_CPC.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Lee_CPC.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Lee_CPC.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Lee_CPC.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Lee_RPC' sub-command
    parser_GA_Lee_RPC.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Lee_RPC.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Lee_RPC.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Lee_RPC.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Lee_RPC.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Lee_RPC.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Lee_RPC.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Lee_RPC.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Lee_RPC.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Lee_RPC.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Lee_RPC.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'GA_Lee_rRPC' sub-command
    parser_GA_Lee_rRPC.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_GA_Lee_rRPC.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_GA_Lee_rRPC.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_GA_Lee_rRPC.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_GA_Lee_rRPC.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_GA_Lee_rRPC.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_GA_Lee_rRPC.add_argument(
        '-l', '--log', type=str, metavar='mog_file', default=None,
        help=helpdoc.log_help)
    parser_GA_Lee_rRPC.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_GA_Lee_rRPC.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_GA_Lee_rRPC.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_GA_Lee_rRPC.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Ped_Wu' sub-command
    parser_Ped_Wu.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Ped_Wu.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Ped_Wu.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Ped_Wu.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Ped_Wu.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Ped_Wu.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Ped_Wu.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Ped_Wu.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Ped_Wu.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Ped_Wu.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_Ped_Wu.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'AltumAge' sub-command
    parser_AltumAge.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_AltumAge.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_AltumAge.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_AltumAge.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_AltumAge.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_AltumAge.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_AltumAge.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_AltumAge.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_AltumAge.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_AltumAge.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_AltumAge.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the 'Cortical' sub-command
    parser_Cortical.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_Cortical.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_Cortical.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_Cortical.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_Cortical.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_Cortical.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_Cortical.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_Cortical.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_Cortical.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_Cortical.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')
    parser_Cortical.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the 'EPM' sub-command
    parser_EPM.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_EPM.add_argument(
        'meta', type=str, metavar='meta_file', help=helpdoc.epm_meta_help)
    parser_EPM.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.epm_output_help)
    parser_EPM.add_argument(
        '-p', '--pcc', type=float, default=0.85, help='Threshold of absolute \
            Pearson correlation coefficient between chronological age and \
            beta values. This cutoff is used to select age-associated CpG \
            sites.')
    parser_EPM.add_argument(
        '-n', '--niter', type=int, default=100, help='Iteration times of \
            expectation–maximization.')
    parser_EPM.add_argument(
        '-k', '--kfold', type=int, default=10, help='\
        Folds for cross-valiation.')
    parser_EPM.add_argument(
        '-e', '--etol', type=float, default=1e-5, help='Error tolerance \
            during model fitting. The acceptable level of deviation between \
            the EPM predicted age and the chronological age.')
    parser_EPM.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_EPM.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_EPM.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_EPM.add_argument(
        '-i', '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_EPM.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_EPM.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)

    # create the parser for the mouse 'WLMT' sub-command
    parser_WLMT.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_WLMT.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_WLMT.add_argument(
       '-g', '--genome', type=str, choices=('mm10', 'mm39'), default='mm10',
       help="The reference genome for Mouse (Mus musculus) used for RRBS or\
           WGBS reads alignment. Must be 'mm10' or 'mm39'. default is 'mm10'.")
    parser_WLMT.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_WLMT.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_WLMT.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_WLMT.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_WLMT.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_WLMT.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_WLMT.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_WLMT.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_WLMT.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the mouse 'YOMT' sub-command
    parser_YOMT.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_YOMT.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_YOMT.add_argument(
       '-g', '--genome', type=str, choices=('mm10', 'mm39'), default='mm10',
       help="The reference genome for Mouse (Mus musculus) used for RRBS or\
           WGBS reads alignment. Must be 'mm10' or 'mm39'. default is 'mm10'.")
    parser_YOMT.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_YOMT.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_YOMT.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_YOMT.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_YOMT.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_YOMT.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_YOMT.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_YOMT.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_YOMT.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the mouse 'mmLiver' sub-command
    parser_mmLiver.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_mmLiver.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_mmLiver.add_argument(
       '-g', '--genome', type=str, choices=('mm10', 'mm39'), default='mm10',
       help="The reference genome for Mouse (Mus musculus) used for RRBS or\
           WGBS reads alignment. Must be 'mm10' or 'mm39'. default is 'mm10'.")
    parser_mmLiver.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_mmLiver.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_mmLiver.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_mmLiver.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_mmLiver.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_mmLiver.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_mmLiver.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_mmLiver.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_mmLiver.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    # create the parser for the mouse 'mmBlood' sub-command
    parser_mmBlood.add_argument(
        'input', type=str, metavar='Input_file', help=helpdoc.input_help)
    parser_mmBlood.add_argument(
        '-o', '--output', type=str, metavar='out_prefix', default=None,
        help=helpdoc.output_help)
    parser_mmBlood.add_argument(
       '-g', '--genome', type=str, choices=('mm10', 'mm39'), default='mm10',
       help="The reference genome for Mouse (Mus musculus) used for RRBS or\
           WGBS reads alignment. Must be 'mm10' or 'mm39'. default is 'mm10'.")
    parser_mmBlood.add_argument(
        '-p', '--percent', type=float, default=0.2, help=helpdoc.na_help)
    parser_mmBlood.add_argument(
        '-d', '--delimiter', type=str, default=None, help=helpdoc.del_help)
    parser_mmBlood.add_argument(
        '-f', '--format', type=str, choices=['pdf', 'png'], default='pdf',
        help=helpdoc.format_help)
    parser_mmBlood.add_argument(
        '-m', '--metadata', type=str, metavar='meta_file', default=None,
        help=helpdoc.meta_help)
    parser_mmBlood.add_argument(
        '-l', '--log', type=str, metavar='log_file', default=None,
        help=helpdoc.log_help)
    parser_mmBlood.add_argument(
        '--impute', type=int, choices=range(-1, 11), default=0,
        help=helpdoc.imputation_help)
    parser_mmBlood.add_argument(
        '-r', '--ref', type=str, metavar='ref_file', default=None,
        help=helpdoc.ext_ref_help)
    parser_mmBlood.add_argument(
        '--debug', action='store_true', help=helpdoc.debug_help)
    parser_mmBlood.add_argument(
        '--overwrite', action='store_true',
        help='If set, over-write existing output files.')

    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(0)
    elif len(sys.argv) >= 2:
        command = sys.argv[1]
        if command == 'Horvath13':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20, cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Horvath13_shrunk':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20, cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Horvath18':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'MEAT':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'PedBE':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Levine':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_levine_hannum(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Hannum':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_levine_hannum(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Lu_DNAmTL':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_levine_hannum(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Zhang_BLUP':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_blup_en(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Zhang_EN':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_blup_en(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Knight':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Mayne':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Bohlin':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Haftorn':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Lee_CPC':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Lee_RPC':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'GA_Lee_rRPC':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_GA(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Ped_Wu':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                adult_age=48,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'AltumAge':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.altum_age(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'Cortical':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_horvath(
                beta_file=args.input,
                outfile=args.output,
                metafile=args.metadata,
                delimiter=args.delimiter,
                adult_age=20, cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'EPM':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_epm(
                beta_file=args.input,
                metafile=args.meta,
                outfile=args.output,
                delimiter=args.delimiter,
                imputation_method=args.impute,
                ext_file=args.ref,
                pcc_cut=args.pcc,
                iter_n=args.niter,
                error_tol=args.etol,
                cv_folds=args.kfold,
                frmt=args.format,
                cname=command
                )

        elif command == 'WLMT':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_mouse(
                beta_file=args.input,
                outfile=args.output,
                genome=args.genome,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'YOMT':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_mouse(
                beta_file=args.input,
                outfile=args.output,
                genome=args.genome,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'mmLiver':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_mouse(
                beta_file=args.input,
                outfile=args.output,
                genome=args.genome,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        elif command == 'mmBlood':
            config_log(switch=args.debug, logfile=args.log)
            methylclocks.clock_mouse(
                beta_file=args.input,
                outfile=args.output,
                genome=args.genome,
                metafile=args.metadata,
                delimiter=args.delimiter,
                cname=command,
                ff=args.format,
                na_percent=args.percent,
                ovr=args.overwrite,
                imputation_method=args.impute,
                ext_file=args.ref
                )
        else:
            print("Unknown command!")
            parser.print_help(sys.stderr)
            sys.exit(0)
