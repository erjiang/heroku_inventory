# heroku_inventory

Get a CSV file of all of your add-ons across all of your apps:

| app         | addon             | plan        | price |
| ----------- | ----------------- | ----------- | ----- |
| myfirstapp  | heroku-postgresql | hobby-basic | 9     |
| myfirstapp  | papertrail        | choklad     | 0     |
| mysecondapp | heroku-postgresql | hobby-basic | 9     |

# Requirements

* Python 3.5+
* heroku-cli set up and in your PATH

# Usage

## Prepare a list of apps

You first need a text file listing all of the apps for which you want to collect add-ons. You can get all of the apps for a team by doing:

```
heroku apps -t myteamname | tail -n +2 | head -n -1 > my-apps.txt
```

## Run heroku_inventory.py

```
python3 heroku_inventory.py < my-apps.txt > my-heroku-addons.csv
```