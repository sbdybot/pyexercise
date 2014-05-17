# -*- coding: utf-8 -*-


#boo = csvContainer(boofn)
#
#res = boo.aggregate('pax', 'arr_port', lambda a, b: a + b)
#
#top10 = sorted(res, key = res.get, reverse = True)[0:10]
#
#[(i, res[i]) for i in top10]


#sea = csvContainer(seafn)
#res = sea.join_step1()
#
#top10 = sorted(res, key = res.get, reverse = True)[0:10]
#[(i, res[i]) for i in top10]
#
#bot10 = sorted(res, key = res.get)[0:10]
#[(i, res[i]) for i in bot10]
#
#filt = {('ZFV', 'EWR', '2013-11-06'), 56}
#filt = {('NCE', 'LGW', '2014-06-28'), 1468}
#
#sea = csvContainer(seafn)
#sea.join_step2_search(filt)
#
sea = csvContainer(seafn)

res = sea.aggregate('RoundTrip', 'Seg1Date', lambda a, b: a + b)

st = sorted(res)

filtr = {('NCE', 'LGW', '2013-06-28'): 1, ('PRG', 'XNA', '2014-09-21'): 11, ('SAN', 'SFO', '2013-11-15'): 13, ('BSB', 'POA', '2013-07-06'): 4, ('NCE', 'LGW', '2014-06-28'): 0, ('STO', 'OSL', '2013-08-10'): 6, ('LHR', 'ARN', '2013-11-02'): 19, ('ZFV', 'EWR', '2013-11-06'): 10, ('FRA', 'BKK', '2013-12-20'): 5, ('CKG', 'LAX', '2014-01-23'): 15, ('SFO', 'FCO', '2013-11-29'): 14, ('DUS', 'MIA', '2014-03-14'): 17, ('MUC', 'LON', '2013-05-25'): 9, ('STO', 'LON', '2013-12-09'): 3, ('RUH', 'JED', '2013-01-16'): 7, ('FRA', 'FTU', '2014-02-13'): 18, ('CLO', 'ZRH', '2013-12-10'): 16, ('AHB', 'RUH', '2013-08-12'): 8, ('FRA', 'NYC', ''): 2, ('MUC', 'PUJ', '2014-02-04'): 12}
filtr = {('SAN', 'SFO', '2013-11-15'): 13}
filtr = {('RUH', 'JED', '2013-01-16'): 7}

sea = csvContainer(seafn)
sea.join_step2_search(filtr)
boo = csvContainer(boofn)
boo.join_step2_book(filtr)

#>>> boo = csvContainer(boofn)
#>>> res = boo.aggregate('pax', 'brd_time', lambda a, b: a + b)
#>>> len(res)
#167848
#>>> st = sorted(res)
#>>> len(st)
#167848
#>>> st[0]
#'2012-03-02 12:15:00'
#>>> st[-1]
#'2014-12-20 13:35:00'

#>>> sea = csvContainer(seafn)
#>>> res = sea.aggregate('RoundTrip', 'Seg1Date', lambda a, b: a + b)
#>>> len(res)
#717
#>>> st = sorted(res)
#>>> len(st)
#717
#>>> st[0]
#''
#>>> st[1]
#'2013-01-01'
#>>> st[-1]
#'2014-12-22'
