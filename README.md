# comp-raise-ids
Quick script to compare the ids between services via exported csvs


## Pre Reqs
- Run the `requirements.txt` file with `pip install -r requirements.txt` to install Pandas
- This should work with the native Python version on your Mac

## Getting Data
** This can obviously be modified to fit whatever your requirements are **
- Run this query in Fundraisers db
`SELECT id as fundraiser_service_id, "raiseFundraiserUserId" as id FROM "FundraiserManager";`
- Export as fundraiser_ids.csv
- Run this query in Raise db
`select id, fundraiser_service_id from fundraiser_users where role = 'coach';`
- Export as raise_ids.csv

- Export both as CSVs and save them to the root of this project

## Running the Script
- Just run `python3 id_comp_script` and you will get two new CSVs

### Happy Hunting!