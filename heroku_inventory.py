#!/usr/bin/env python3

import csv
import fileinput
import re
import subprocess
import sys


outfile = csv.writer(sys.stdout)

headers = ["app", "addon", "plan", "price"] 
outfile.writerow(headers)

for app in fileinput.input():
    app = app.strip()
    sys.stderr.write("Querying for (%s)\n" % (app,))
    completed = subprocess.run(['heroku', 'addons', '-a', app], stdout=subprocess.PIPE)
    output_lines = completed.stdout.decode("utf-8").split('\n')
    for addon in output_lines:
        if "created" not in addon:
            continue
        # fields = [addon, plan, price, status]
        fields = [f.strip() for f in re.split(r"  +", addon)]
        # process price
        if fields[2] == "free":
            fields[2] = 0
        elif "billed to" in fields[2]:
            continue
        else:
            price_match = re.match(r"\$(\d+)/month", fields[2])
            fields[2] = int(price_match.groups()[0])
        # strip addon ID
        fields[0] = fields[0].split(" ")[0]
        outfile.writerow([app] + fields[:3])
