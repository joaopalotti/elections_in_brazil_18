from pysocialwatcher import watcherAPI
import os
import json
import pandas as pd

from pysocialwatcher import constants
#constants.SLEEP_TIME = 10

PATH_TO_CREDENTIALS="~/github/elections_brazil_18/credentials.csv"
PATH_TO_JSON="~/github/elections_brazil_18/elections_in_brazil.json"

watcher = watcherAPI()
watcher.load_credentials_file(os.path.expanduser(PATH_TO_CREDENTIALS))

df = watcher.run_data_collection(os.path.expanduser(PATH_TO_JSON))

print("UNIQUE_TIME_ID:", constants.UNIQUE_TIME_ID)
