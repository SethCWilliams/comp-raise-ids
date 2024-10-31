import pandas as pd

# Load the CSV files
raise_ids = pd.read_csv('raise_ids.csv')
fundraiser_ids = pd.read_csv('fundraiser_ids.csv')

# Convert columns to sets for easy comparison
raise_id_set = set(raise_ids['id'])
fundraiser_id_set = set(fundraiser_ids['id'])
fundraiser_service_id_set = set(fundraiser_ids['fundraiser_service_id'])
raise_service_id_set = set(raise_ids['fundraiser_service_id'])

# 1. Find IDs in raise_ids.csv that aren't in fundraiser_ids.csv
ids_in_raise_not_in_fundraiser = raise_ids[raise_ids['id'].isin(raise_id_set - fundraiser_id_set)]['id']

# Save to CSV (only 'id' column)
ids_in_raise_not_in_fundraiser.to_csv('ids_in_raise_not_in_fundraiser.csv', index=False, header=True)

# 2. Find rows in fundraiser_ids.csv where:
# - id is present
# - fundraiser_service_id is present
# - fundraiser_service_id is not in raise_ids.csv
missing_in_raise = fundraiser_ids[
    (fundraiser_ids['id'].notna()) &
    (fundraiser_ids['fundraiser_service_id'].notna()) &
    (~fundraiser_ids['fundraiser_service_id'].isin(raise_service_id_set))
]

# Save to CSV
missing_in_raise.to_csv('missing_in_raise.csv', index=False)

print("CSV files created: 'ids_in_raise_not_in_fundraiser.csv' and 'missing_in_raise.csv'")
