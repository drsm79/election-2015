---
layout: default
title: Election Results 2015
---

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

    Counter({'total': 650, 'stay home win': 340, '<=10 pc of home win': 56, 'close call (500)': 13, 'close call (250)': 6, 'close call (100)': 3, 'close call (50)': 2})

Run `python election.py --show-win-over` to get more detail on what fraction of stay at home vote would be needed to change the result. Combine with `grep` to see things like [Conservative seats to target "stay at home" voters](targets.html).

Run `python election.py --show-stay-home` to see seats where the stay at home vote was larger than the winning candidate.

Run `python election.py --show-close` to see information about seats that were narrowly won.

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">In 2015 13 seats were won by 500 votes or less. 2 were won by 50 or less. <a href="https://twitter.com/hashtag/GE2017?src=hash">#GE2017</a> <a href="https://twitter.com/hashtag/GE2015?src=hash">#GE2015</a> <a href="https://twitter.com/hashtag/YourVoteMatters?src=hash">#YourVoteMatters</a></p>&mdash; Simon /\/\e†s0|\| (@drsm79) <a href="https://twitter.com/drsm79/status/855449750207959040">April 21, 2017</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

[1]: http://www.electoralcommission.org.uk/__data/assets/excel_doc/0011/189623/2015-UK-general-election-data-results-WEB.xlsx
