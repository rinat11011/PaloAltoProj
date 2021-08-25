import json
import pandas as pd


def json_to_dataframe(rules_d):
    # Parse JSON string and convert it into a dictionary
    rules_obj = json.loads(rules_d)

    # Create the rules table
    rules_df = pd.DataFrame(rules_obj['rules'])

    return rules_df
