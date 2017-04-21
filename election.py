import xlrd
import fire
from collections import Counter


def percent(small, big=False):
    if big:
        return "{0:.0f}%".format((100. * small) / big)
    return "{0:.0f}%".format(100. * small)


class Constituency:
    def __init__(self, name, region, electorate, votes):
        self.name = name
        self.region = region
        self.electorate = int(electorate)
        self.votes = (votes)
        self.counter = Counter()

    def __str__(self):
        return ', '.join([self.name, self.region, self.turn_out()]) + ' turnout'

    def turn_out(self):
        return percent(self.votes, self.electorate)

    def vote(self, party, vote):
        self.counter[party] = vote

    def winner(self):
        return self.counter.most_common(1)[0]

    def stay_home_win(self):
        return self.winner()[1] < (self.electorate - self.votes)


def process_xls(xls):
    book = xlrd.open_workbook(xls)
    # print "The number of worksheets is", book.nsheets
    # print "Worksheet name(s):", book.sheet_names()
    constituencies = []
    sheet = book.sheet_by_name('Party names')
    parties = {sheet.row(r)[0].value: sheet.row(r)[2].value for r in range(sheet.nrows)}
    sheet = book.sheet_by_name('Results for analysis')
    for r in range(1, sheet.nrows - 1):
        c = Constituency(
            sheet.row(r)[1].value,
            sheet.row(r)[2].value,
            sheet.row(r)[7].value,
            sheet.row(r)[8].value
        )
        for v in range(11, len(sheet.row(r))):
            if sheet.row(r)[v].value:
                c.vote(sheet.row(0)[v].value, int(sheet.row(r)[v].value))
        constituencies.append(c)
    return constituencies


def main(show_win_over=False, show_stay_home=False):
    xl = '2015-UK-general-election-data-results-WEB.xlsx'
    constituencies = process_xls(xl)
    cnt = Counter()
    for c in constituencies:
        cnt['total'] += 1
        top_two = c.counter.most_common(2)
        frac = (top_two[0][1] - top_two[1][1]) / (c.electorate - c.votes)
        if frac <= 0.1:
            if show_win_over:
                print '{} ({}) needed {} of stay at home vote to win over {} ({}) in {}'.format(
                    top_two[0][0],
                    top_two[0][1],
                    percent(frac),
                    top_two[1][0],
                    top_two[1][1],
                    c
                )
            cnt['<=10 pc of home win'] += 1
        if c.stay_home_win():
            if show_stay_home:
                print c, c.winner(), c.electorate - c.votes
            cnt['stay home win'] += 1
    print cnt


if __name__ == '__main__':
    fire.Fire(main)
