import sys
import importlib

# import helper functions
sys.path.append('./helper_functions')
semrushAnalytics = importlib.import_module('semrushAnalytics')
fetchATRecords = importlib.import_module('fetchATRecords')

def run_script():
    fetchATRecords()


if __name__ == "__main__":
    run_script()

