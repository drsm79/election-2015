# election-2015
Some data analysis on the 2015 election result

## The data

I used this [file from the electoral commission][1].


## Install

    pipfile install


## The script

    pipfile shell
    python election.py -- --help
    python election.py

Returns something like:

    Counter({'total': 650, 'stay home win': 340, '<=10 pc of home win': 56})

Run `python election.py --show-win-over` to get more detail on what fraction of stay at home vote would be needed to change the result.

Run `python election.py --show-stay-home` to see seats where the stay at home vote was larger than the winning candidate.



[1]: http://www.electoralcommission.org.uk/__data/assets/excel_doc/0011/189623/2015-UK-general-election-data-results-WEB.xlsx
