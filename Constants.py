import datetime
import pandas as pd

# Define global variables

# Uniform first date in all logs
FIRST = datetime.datetime(2016, 1, 1, 0, 0)
# Date range of dates in the dataset
DATE_RANGE = [d.strftime('%Y-%m-%d') for d in pd.date_range("2016-1-1", "2017-2-1")]

# Define color constants, used for plotting
class Color:
    ORANGE = (255/256, 128/256, 0)
    PINK = (255/256, 102/256, 102/256)
    RED = (1, 0, 0)
    DARK_RED = (153/256, 0, 0)
    BLACK = (0, 0, 0)
    YELLOW = (1, 1, 0)
    LIGHT_GREEN = (102/256, 255/256, 102/256)
    GREEN = (0, 1, 0)
    DARK_GREEN = (0/256, 153/256, 0/256)
    LIGHT_BLUE = (102/256, 178/256, 255/256)
    BLUE = (0/256, 128/256, 255/256)
    DARK_BLUE = (0/256, 76/256, 153/256)
    LIGHT_GREY = (192/256, 192/256, 192/256)
    GREY = (128/256, 128/256, 128/256)

    
# define classifiers
class Classifier:
    CASE = {"classifier": lambda row: 0 if row["plot"] else -1,
            "colors": [Color.RED]}
    CASES2 = {"classifier": lambda row: 
              1 if row["pattern"] else (
              0 if row["not_pattern"] else -1),
            "colors": [Color.GREEN, Color.RED]}
    
    BASIC = {"classifier": lambda row: 
             0,
             "colors": [Color.RED]
            }
           
    ALL = {"classifier": lambda row: 
           3 if row["delayed"] else (
           2 if row["batching"] else (
           1 if row["slow"] else 0)),
           "colors": [Color.LIGHT_GREY, Color.BLUE, Color.GREEN, Color.DARK_GREEN]
          }
    DELAYED_BUNDLES = {"classifier": lambda row: 
               1 if (row["delayed1"] and not row["delayed5"]) else (
               2 if (row["delayed5"] and not row["delayed10"]) else(
               3 if (row["delayed10"] and not row["delayed15"]) else(
               4 if (row["delayed15"] and not row["delayed20"]) else (
               5 if row["delayed20"] else (
               0 if not row["instant"] else -1))))),
               "colors": [Color.LIGHT_GREY, Color.YELLOW, Color.LIGHT_GREEN, Color.GREEN, Color.DARK_GREEN, Color.BLACK]
              }
    DELAYED_BUNDLES_EXCL = {"classifier": lambda row: 
                    0 if (row["delayed1"] and not row["delayed5"]) else (
                    1 if (row["delayed5"] and not row["delayed10"]) else(
                    2 if (row["delayed10"] and not row["delayed15"]) else(
                    3 if (row["delayed15"] and not row["delayed20"]) else (
                    4 if row["delayed20"] else  -1)))),
                    "colors": [Color.YELLOW, Color.LIGHT_GREEN, Color.GREEN, Color.DARK_GREEN, Color.BLACK]
                   }
    BATCHING = {"classifier": lambda row:
                1 if row["batching"] else 0,
                "colors": [Color.LIGHT_GREY, Color.RED]
               }
    BATCHING_DURATION = {"classifier": lambda row:
                         1 if (row["batching"] and row["instant"]) else (
                         2 if (row["batching"] and not row["instant"]) else 0),
                         "colors": [Color.LIGHT_GREY, Color.PINK, Color.DARK_RED]
                        }
    HIGH_LOAD = {"classifier": lambda row:
                 1 if row["batching"] else 0,
                 "colors": [Color.LIGHT_GREY, Color.BLUE]
                }
    HIGH_LOAD_DURATION = {"classifier": lambda row:
                         1 if (row["high_load"] and row["instant"]) else (
                         2 if (row["high_load"] and not row["instant"]) else 0),
                         "colors": [Color.LIGHT_GREY, Color.LIGHT_BLUE, Color.DARK_BLUE]
                        }
    BATCHING_END_JENKS = {"classifier": lambda row:
                    1 if ((row["batching"] and row["batching53"]) and not row["batching88"]) else (
                    2 if ((row["batching"] and row["batching88"]) and not row["batching127"]) else (
                    3 if ((row["batching"] and row["batching127"]) and not row["batching176"]) else (
                    4 if ((row["batching"] and row["batching176"]) and not row["batching279"]) else (
                    5 if (row["batching"] and row["batching279"]) else (0))))),
                    "colors": [Color.LIGHT_GREY, Color.GREEN, Color.YELLOW, Color.ORANGE, Color.RED, Color.BLACK]
                   }
    HIGH_LOAD_BUNDLES = {"classifier": lambda row: 
                        1 if ((row["high_load"] and row["high_load1"]) and not row["high_load25"]) else(
                        2 if ((row["high_load"] and row["high_load25"]) and not row["high_load50"]) else(
                        3 if ((row["high_load"] and row["high_load50"]) and not row["high_load75"]) else (
                        4 if ((row["high_load"] and row["high_load75"]) and not row["high_load100"]) else (
                        5 if ((row["high_load"] and row["high_load100"]) and not row["high_load125"]) else (
                        6 if ((row["high_load"] and row["high_load125"]) and not row["high_load150"]) else (
                        7 if ((row["high_load"] and row["high_load150"]) and not row["high_load175"]) else (
                        8 if ((row["high_load"] and row["high_load175"]) and not row["high_load200"]) else (
                        9 if (row["high_load"] and row["high_load200"]) else (0))))))))),
                        "colors": [Color.LIGHT_GREY, Color.LIGHT_GREEN, Color.GREEN, Color.DARK_GREEN, Color.YELLOW, 
                                   Color.ORANGE, Color.PINK, Color.RED, Color.DARK_RED, Color.BLACK]
                       }
    BATCHING_START_JENKS = {"classifier": lambda row:
                1 if ((row["high_load"] and row["high_load53"]) and not row["high_load89"]) else (
                2 if ((row["high_load"] and row["high_load89"]) and not row["high_load127"]) else (
                3 if ((row["high_load"] and row["high_load127"]) and not row["high_load173"]) else (
                4 if ((row["high_load"] and row["high_load173"]) and not row["high_load279"]) else (
                5 if (row["high_load"] and row["high_load279"]) else (0))))),
                "colors": [Color.LIGHT_GREY, Color.GREEN, Color.YELLOW, Color.ORANGE, Color.RED, Color.BLACK]
               }
    DELAYED_BATCHING = {"classifier": lambda row:
                        1 if (row["batching"] and not row["delayed1"]) else (
                        2 if (row["delayed1"] and not row["batching"]) else (
                        3 if (row["batching"] and row["delayed1"]) else (
                        0 ))),
                        "colors": [Color.LIGHT_GREY, Color.RED, Color.GREEN, Color.BLACK]
                       }
    DELAYED_HIGH_LOAD = {"classifier": lambda row:
                        1 if (row["high_load"] and not row["delayed1"]) else (
                        2 if (row["delayed1"] and not row["high_load"]) else (
                        3 if (row["high_load"] and row["delayed1"]) else (
                        0 ))),
                        "colors": [Color.LIGHT_GREY, Color.BLUE, Color.GREEN, Color.BLACK]
                       }
    HIGH_WORKLOAD_BUNDLES = {"classifier": lambda row: 
                        1 if ((row["workload"] and row["workload1"]) and not row["workload20"]) else(
                        2 if ((row["workload"] and row["workload20"]) and not row["workload40"]) else(
                        3 if ((row["workload"] and row["workload40"]) and not row["workload60"]) else (
                        4 if (row["workload"] and row["workload60"]) else (
                        5 if (row["workload_hand"]) else 0)))),
                        "colors": [Color.LIGHT_GREY, Color.GREEN, Color.YELLOW, Color.ORANGE, Color.RED, Color.BLUE]
                       }
    
class Short:
    ACTIVITY = {
        'A_Create Application|COMPLETE': 'ACR',
        'A_Submitted|COMPLETE': 'ASU',
        'A_Concept|COMPLETE': 'ACO',
        'A_Validating|COMPLETE': 'AVA',
        'A_Pending|COMPLETE': 'APE',
        'A_Complete|COMPLETE': 'ACO',
        'A_Cancelled|COMPLETE': 'ACA',
        'A_Accepted|COMPLETE': 'AAC',
        'A_Incomplete|COMPLETE': 'AIN',
        'O_Create Offer|COMPLETE': 'OCO',
        'O_Created|COMPLETE': 'OCR',
        'O_Sent (mail and online)|COMPLETE': 'OSE',
        'O_Cancelled|COMPLETE': 'OCA',
        'O_Returned|COMPLETE': 'ORE',
        'O_Accepted|COMPLETE': 'OAC',
        'W_Handle leads|SCHEDULE': 'WHL.SCH',
        'W_Handle leads|WITHDRAW': 'WHL.WIT',        
        'W_Complete application|START': 'WCA.STA',
        'W_Complete application|SCHEDULE': 'WCA.SCH',
        'W_Complete application|SUSPEND': 'WCA.SUS',
        'W_Complete application|COMPLETE': 'WCA.COM',       
        'W_Call after offers|START': 'WCO.STA',
        'W_Call after offers|SCHEDULE': 'WCO.SCH',
        'W_Call after offers|SUSPEND': 'WCO.SUS',
        'W_Call after offers|RESUME': 'WCO.RES',
        'W_Call after offers|ATE_ABORT': 'WCO.ABO',       
        'W_Validate application|START': 'WVA.STA',
        'W_Validate application|SCHEDULE': 'WVA.SCH',
        'W_Validate application|SUSPEND': 'WVA.SUS',
        'W_Validate application|RESUME': 'WVA.RES',
        'W_Validate application|COMPLETE': 'WVA.COM',
        'W_Validate application|ATE_ABORT': 'WVA.ABO',
        'W_Call incomplete files|START': 'WCF.STA',
        'W_Call incomplete files|SCHEDULE': 'WCF.SCH',
        'W_Call incomplete files|SUSPEND': 'WCF.SUS',
        'W_Call incomplete files|RESUME': 'WCF.RES',
        'W_Call incomplete files|ATE_ABORT': 'WCF.ABO'
    }
    ACTIVITY_INV = {
        'ACR': 'A_Create Application|COMPLETE',
        'ASU': 'A_Submitted|COMPLETE',
        'ACO': 'A_Concept|COMPLETE',
        'AVA': 'A_Validating|COMPLETE',
        'APE': 'A_Pending|COMPLETE',
        'ACO': 'A_Complete|COMPLETE',
        'ACA': 'A_Cancelled|COMPLETE',
        'AAC': 'A_Accepted|COMPLETE',
        'AIN': 'A_Incomplete|COMPLETE',
        'OCO': 'O_Create Offer|COMPLETE',
        'OCR': 'O_Created|COMPLETE',
        'OSE': 'O_Sent (mail and online)|COMPLETE',
        'OCA': 'O_Cancelled|COMPLETE',
        'ORE': 'O_Returned|COMPLETE',
        'OAC': 'O_Accepted|COMPLETE',
        'WHL.SCH': 'W_Handle leads|SCHEDULE',
        'WHL.WIT': 'W_Handle leads|WITHDRAW',        
        'WCA.STA': 'W_Complete application|START',
        'WCA.SCH': 'W_Complete application|SCHEDULE',
        'WCA.SUS': 'W_Complete application|SUSPEND',
        'WCA.COM': 'W_Complete application|COMPLETE',       
        'WCO.STA': 'W_Call after offers|START',
        'WCO.SCH': 'W_Call after offers|SCHEDULE',
        'WCO.SUS': 'W_Call after offers|SUSPEND',
        'WCO.RES': 'W_Call after offers|RESUME',
        'WCO.ABO': 'W_Call after offers|ATE_ABORT',       
        'WVA.STA': 'W_Validate application|START',
        'WVA.SCH': 'W_Validate application|SCHEDULE',
        'WVA.SUS': 'W_Validate application|SUSPEND',
        'WVA.RES': 'W_Validate application|RESUME',
        'WVA.COM': 'W_Validate application|COMPLETE',
        'WVA.ABO': 'W_Validate application|ATE_ABORT',
        'WCF.STA': 'W_Call incomplete files|START',
        'WCF.SCH': 'W_Call incomplete files|SCHEDULE',
        'WCF.SUS': 'W_Call incomplete files|SUSPEND',
        'WCF.RES': 'W_Call incomplete files|RESUME',
        'WCF.ABO': 'W_Call incomplete files|ATE_ABORT'
    }
    
    TYPE = {"delayed": "DEL", "batching_start": "BST", "batching_end": "BEN", "workload": "WLD", "workload_hand": "WLH"}
    
# define segments
class Segments:
    SEGMENTS_PATTERN7 = ['W_Call after offers|SUSPEND - A_Cancelled|COMPLETE',
                         'W_Call after offers|SUSPEND - O_Create Offer|COMPLETE']
    
    SEGMENTS_PATTERN10 = ['O_Sent (mail and online)|COMPLETE - W_Call after offers|ATE_ABORT',
                         'W_Call incomplete files|SUSPEND - O_Returned|COMPLETE',
                         'O_Sent (mail and online)|COMPLETE - W_Call incomplete files|RESUME',
                         'O_Sent (online only)|COMPLETE - W_Call incomplete files|ATE_ABORT',
                         'W_Assess potential fraud|SUSPEND - W_Assess potential fraud|RESUME',
                         'W_Validate application|SUSPEND - W_Validate application|RESUME']
    
    SEGMENTS_PATTERN12 = ['W_Assess potential fraud|SUSPEND - W_Assess potential fraud|RESUME',
                         'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
                         'W_Validate application|SUSPEND - O_Accepted|COMPLETE',
                         'W_Call incomplete files|SUSPEND - O_Create Offer|COMPLETE',
                         'W_Validate application|SUSPEND - W_Validate application|RESUME',
                         'W_Call after offers|SUSPEND - O_Create Offer|COMPLETE',
                         'W_Call after offers|SCHEDULE - W_Call after offers|WITHDRAW',
                         'O_Sent (mail and online)|COMPLETE - W_Call incomplete files|RESUME']
    
    SEGMENTS_PATTERN25 = ['W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
                         'O_Sent (mail and online)|COMPLETE - W_Call incomplete files|ATE_ABORT',
                         'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT',
                         'W_Complete application|SUSPEND - O_Create Offer|COMPLETE']
    
    SEGMENTS_PATTERN11 = ['O_Sent (mail and online)|COMPLETE - O_Create Offer|COMPLETE',
                         'O_Sent (mail and online)|COMPLETE - W_Call after offers|ATE_ABORT',
                         'W_Call incomplete files|SUSPEND - O_Returned|COMPLETE',
                         'O_Sent (online only)|COMPLETE - W_Call after offers|ATE_ABORT',
                         'W_Assess potential fraud|SUSPEND - W_Assess potential fraud|RESUME',
                         'O_Sent (online only)|COMPLETE - W_Call incomplete files|ATE_ABORT',
                         'O_Sent (mail and online)|COMPLETE - W_Call after offers|RESUME',
                         'W_Validate application|SUSPEND - W_Validate application|RESUME']
    
    SEGMENTS_BASIC = ['A_Concept|COMPLETE - A_Accepted|COMPLETE',
    'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT',
    'W_Call after offers|SUSPEND - W_Call after offers|RESUME',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|ATE_ABORT',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|RESUME',
    'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
    'W_Validate application|SUSPEND - W_Validate application|RESUME',
    'W_Validate application|SUSPEND - O_Accepted|COMPLETE',
    'W_Complete application|SUSPEND - A_Accepted|COMPLETE',
    'W_Complete application|SUSPEND - W_Complete application|RESUME']

    SEGMENTS_DETAILED = ['A_Concept|COMPLETE - A_Accepted|COMPLETE',
    'A_Accepted|COMPLETE - O_Create Offer|COMPLETE',
    'O_Create Offer|COMPLETE - O_Created|COMPLETE',
    'O_Created|COMPLETE - O_Sent (mail and online)|COMPLETE',
    'W_Complete application|SUSPEND - W_Complete application|RESUME',
    'W_Complete application|SUSPEND - A_Accepted|COMPLETE',
    'W_Call after offers|SCHEDULE - W_Call after offers|START',
    'W_Call after offers|START - A_Complete|COMPLETE',
    'A_Complete|COMPLETE - W_Call after offers|SUSPEND',
    'W_Call after offers|SUSPEND - W_Call after offers|RESUME',
    'W_Call after offers|RESUME - W_Call after offers|SUSPEND',
    'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT',
    'W_Validate application|SCHEDULE - W_Validate application|START',
    'W_Validate application|START - A_Validating|COMPLETE',
    'W_Validate application|SUSPEND - W_Validate application|RESUME',
    'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
    'W_Validate application|SUSPEND - O_Accepted|COMPLETE',
    'W_Call incomplete files|SCHEDULE - W_Call incomplete files|START',
    'W_Call incomplete files|START - A_Incomplete|COMPLETE',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|RESUME',
    'W_Call incomplete files|RESUME - W_Call incomplete files|SUSPEND',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|ATE_ABORT']

    SEGMENTS_COMPLETE = ['A_Create Application|COMPLETE - A_Submitted|COMPLETE',
    'A_Submitted|COMPLETE - W_Handle leads|SCHEDULE',
    'W_Handle leads|SCHEDULE - W_Handle leads|WITHDRAW',
    'W_Handle leads|WITHDRAW - W_Complete application|SCHEDULE',
    'A_Create Application|COMPLETE - W_Complete application|SCHEDULE',
    'W_Complete application|SCHEDULE - A_Concept|COMPLETE',
    'A_Concept|COMPLETE - W_Complete application|START',
    'W_Complete application|SCHEDULE - W_Complete application|START',
    'W_Complete application|START - A_Concept|COMPLETE',
    'W_Complete application|START - W_Complete application|SUSPEND',
    'W_Complete application|SUSPEND - A_Accepted|COMPLETE',
    'A_Concept|COMPLETE - A_Accepted|COMPLETE',
    'W_Complete application|START - A_Accepted|COMPLETE',
    'A_Accepted|COMPLETE - O_Create Offer|COMPLETE',
    'O_Create Offer|COMPLETE - O_Created|COMPLETE',
    'O_Created|COMPLETE - O_Sent (mail and online)|COMPLETE',
    'O_Sent (mail and online)|COMPLETE - W_Complete application|COMPLETE',
    'W_Complete application|COMPLETE - W_Call after offers|SCHEDULE',
    'W_Call after offers|SCHEDULE - W_Call after offers|START',
    'W_Call after offers|START - A_Complete|COMPLETE',
    'A_Complete|COMPLETE - W_Call after offers|SUSPEND',
    'W_Call after offers|SUSPEND - O_Create Offer|COMPLETE',
    'W_Call after offers|SUSPEND - W_Call after offers|RESUME',
    'W_Call after offers|RESUME - W_Call after offers|SUSPEND',
    'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT',
    'W_Call after offers|SUSPEND - A_Cancelled|COMPLETE',
    'A_Cancelled|COMPLETE - O_Cancelled|COMPLETE',
    'O_Cancelled|COMPLETE - W_Call after offers|ATE_ABORT',
    'W_Call after offers|ATE_ABORT - W_Validate application|SCHEDULE',
    'W_Validate application|SCHEDULE - W_Validate application|START',
    'W_Validate application|START - A_Validating|COMPLETE',
    'A_Validating|COMPLETE - O_Returned|COMPLETE',
    'O_Returned|COMPLETE - W_Validate application|SUSPEND',
    'A_Validating|COMPLETE - W_Validate application|SUSPEND',
    'W_Validate application|SUSPEND - W_Validate application|RESUME',
    'W_Validate application|RESUME - W_Validate application|SUSPEND',
    'W_Validate application|RESUME - W_Validate application|COMPLETE',
    'W_Validate application|COMPLETE - W_Call incomplete files|SCHEDULE',
    'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
    'W_Validate application|SUSPEND - O_Accepted|COMPLETE',
    'O_Accepted|COMPLETE - A_Pending|COMPLETE',
    'A_Pending|COMPLETE - W_Validate application|ATE_ABORT',
    'W_Validate application|ATE_ABORT - W_Call incomplete files|SCHEDULE',
    'W_Validate application|ATE_ABORT - O_Cancelled|COMPLETE',
    'W_Call incomplete files|SCHEDULE - W_Call incomplete files|START',
    'W_Call incomplete files|START - A_Incomplete|COMPLETE',
    'A_Incomplete|COMPLETE - W_Call incomplete files|SUSPEND',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|RESUME',
    'W_Call incomplete files|RESUME - W_Call incomplete files|SUSPEND',
    'W_Call incomplete files|SUSPEND - W_Call incomplete files|ATE_ABORT',
    'W_Call incomplete files|ATE_ABORT - W_Validate application|SCHEDULE']

    SEGMENTS_COMPLETE_1 = SEGMENTS_COMPLETE[:28]
    SEGMENTS_COMPLETE_2 = SEGMENTS_COMPLETE[28:]0
    
    SEGMENTS_HIGH_WORKLOAD = ['A_Create Application|COMPLETE - W_Complete application|SCHEDULE', 
                              'W_Complete application|SCHEDULE - W_Complete application|START', 
                              'W_Complete application|START - A_Concept|COMPLETE', 
                              'W_Complete application|START - W_Complete application|SUSPEND', 
                              'A_Concept|COMPLETE - A_Accepted|COMPLETE', 
                              'W_Complete application|START - A_Accepted|COMPLETE', 
                              'A_Accepted|COMPLETE - O_Create Offer|COMPLETE', 
                              'O_Create Offer|COMPLETE - O_Created|COMPLETE', 
                              'O_Created|COMPLETE - O_Sent (mail and online)|COMPLETE', 
                              'O_Sent (mail and online)|COMPLETE - W_Complete application|COMPLETE', 
                              'W_Complete application|COMPLETE - W_Call after offers|SCHEDULE', 
                              'W_Call after offers|SCHEDULE - W_Call after offers|START', 
                              'W_Call after offers|START - A_Complete|COMPLETE', 
                              'A_Complete|COMPLETE - W_Call after offers|SUSPEND', 
                              'W_Call after offers|RESUME - W_Call after offers|SUSPEND', 
                              'A_Cancelled|COMPLETE - O_Cancelled|COMPLETE', 
                              'O_Cancelled|COMPLETE - W_Call after offers|ATE_ABORT', 
                              'W_Call after offers|ATE_ABORT - W_Validate application|SCHEDULE', 
                              'W_Validate application|SCHEDULE - W_Validate application|START', 
                              'W_Validate application|START - A_Validating|COMPLETE', 
                              'A_Validating|COMPLETE - O_Returned|COMPLETE', 
                              'O_Returned|COMPLETE - W_Validate application|SUSPEND', 
                              'A_Validating|COMPLETE - W_Validate application|SUSPEND', 
                              'W_Validate application|RESUME - W_Validate application|SUSPEND', 
                              'W_Validate application|RESUME - W_Validate application|COMPLETE', 
                              'W_Validate application|COMPLETE - W_Call incomplete files|SCHEDULE', 
                              'O_Accepted|COMPLETE - A_Pending|COMPLETE', 
                              'A_Pending|COMPLETE - W_Validate application|ATE_ABORT', 
                              'W_Validate application|ATE_ABORT - W_Call incomplete files|SCHEDULE', 
                              'W_Validate application|ATE_ABORT - O_Cancelled|COMPLETE', 
                              'W_Call incomplete files|SCHEDULE - W_Call incomplete files|START', 
                              'W_Call incomplete files|START - A_Incomplete|COMPLETE', 
                              'A_Incomplete|COMPLETE - W_Call incomplete files|SUSPEND', 
                              'W_Call incomplete files|RESUME - W_Call incomplete files|SUSPEND', 
                              'W_Call incomplete files|ATE_ABORT - W_Validate application|SCHEDULE']
    
    SEGMENTS_HIGH_WORKLOAD_HAND = ['W_Complete application|SUSPEND - A_Accepted|COMPLETE', 
                                   'W_Call after offers|SUSPEND - O_Create Offer|COMPLETE', 
                                   'W_Call after offers|SUSPEND - W_Call after offers|RESUME', 
                                   'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT', 
                                   'W_Call after offers|SUSPEND - A_Cancelled|COMPLETE', 
                                   'W_Validate application|SUSPEND - W_Validate application|RESUME', 
                                   'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT', 
                                   'W_Validate application|SUSPEND - O_Accepted|COMPLETE', 
                                   'W_Call incomplete files|SUSPEND - W_Call incomplete files|RESUME', 
                                   'W_Call incomplete files|SUSPEND - W_Call incomplete files|ATE_ABORT']
    
    SEGMENTS_CASCADE0 = ['A_Create Application|COMPLETE - A_Submitted|COMPLETE',
                         'A_Submitted|COMPLETE - W_Handle leads|SCHEDULE',
                         'W_Handle leads|SCHEDULE - W_Handle leads|WITHDRAW',
                         'W_Handle leads|WITHDRAW - W_Complete application|SCHEDULE',
                         'A_Create Application|COMPLETE - W_Complete application|SCHEDULE',
                         'W_Complete application|SCHEDULE - A_Concept|COMPLETE',
                         'A_Concept|COMPLETE - W_Complete application|START',
                         'W_Complete application|SCHEDULE - W_Complete application|START',
                         'W_Complete application|START - W_Complete application|SUSPEND',
                         'W_Complete application|SUSPEND - A_Accepted|COMPLETE',
                         'A_Concept|COMPLETE - A_Accepted|COMPLETE']
                         
    SEGMENTS_CASCADE1 = ['A_Accepted|COMPLETE - O_Create Offer|COMPLETE',
                         'O_Create Offer|COMPLETE - O_Created|COMPLETE',
                         'O_Created|COMPLETE - O_Sent (mail and online)|COMPLETE',
                         'O_Sent (mail and online)|COMPLETE - W_Complete application|COMPLETE',
                         'W_Complete application|COMPLETE - W_Call after offers|SCHEDULE',
                         'W_Call after offers|SCHEDULE - W_Call after offers|START',
                         'W_Call after offers|START - A_Complete|COMPLETE',
                         'A_Complete|COMPLETE - W_Call after offers|SUSPEND',
                         'W_Call after offers|SUSPEND - W_Call after offers|RESUME',
                         'W_Call after offers|SUSPEND - W_Call after offers|ATE_ABORT',
                         'W_Call after offers|SUSPEND - A_Cancelled|COMPLETE',
                         'A_Cancelled|COMPLETE - O_Cancelled|COMPLETE',
                         'O_Cancelled|COMPLETE - W_Call after offers|ATE_ABORT']
                         
    SEGMENTS_CASCADE2 = ['W_Call after offers|ATE_ABORT - W_Validate application|SCHEDULE',
                         'W_Validate application|SCHEDULE - W_Validate application|START',
                         'W_Validate application|START - A_Validating|COMPLETE',
                         'A_Validating|COMPLETE - O_Returned|COMPLETE',
                         'O_Returned|COMPLETE - W_Validate application|SUSPEND',
                         'A_Validating|COMPLETE - W_Validate application|SUSPEND',
                         'W_Validate application|SUSPEND - W_Validate application|RESUME',
                         'W_Validate application|RESUME - W_Validate application|COMPLETE',
                         'W_Validate application|COMPLETE - W_Call incomplete files|SCHEDULE',
                         'W_Validate application|SUSPEND - W_Validate application|ATE_ABORT',
                         'W_Validate application|SUSPEND - O_Accepted|COMPLETE',
                         'O_Accepted|COMPLETE - A_Pending|COMPLETE',
                         'A_Pending|COMPLETE - W_Validate application|ATE_ABORT',
                         'W_Validate application|ATE_ABORT - W_Call incomplete files|SCHEDULE',
                         'W_Call incomplete files|SCHEDULE - W_Call incomplete files|START',
                         'W_Call incomplete files|START - A_Incomplete|COMPLETE',
                         'A_Incomplete|COMPLETE - W_Call incomplete files|SUSPEND',
                         'W_Call incomplete files|SUSPEND - W_Call incomplete files|RESUME',
                         'W_Call incomplete files|SUSPEND - W_Call incomplete files|ATE_ABORT']
    
0