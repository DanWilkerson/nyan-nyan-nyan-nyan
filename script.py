import json
import os
import sys
from datetime import date, timedelta
nul = open(os.devnull, 'w')

sys.stdout = nul

mappings = {
  0: 0,
  1: 5,
  2: 30,
  3: 50,
  4: 80
}

f = open('./data.json', 'r')
squares = json.loads(f.read())
init_date = date(2018, 2, 4);
moving_date = init_date
end_date = date(2017, 3, 16);
for week in squares:
  week = week[::-1]
  for day in week:
    moving_date = moving_date - timedelta(1)
    if moving_date.isoformat() == end_date.isoformat():
      break
    counter = 0
    while counter < mappings[day['color']]:
      counter += 1
      date_str = moving_date.isoformat() + ' 09:00:01'
      filename = '{ds}-{c}.txt'.format(ds=date_str, c=counter)
      os.system('rm *.txt; touch "{f}"; git add -A; git commit -am "{f}" --quiet; git commit --amend --date="{d}" -am "amend {f}" --quiet'.format(
        f=filename,
        d=date_str
        )
      ) 
