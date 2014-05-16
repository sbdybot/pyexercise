# -*- coding: utf-8 -*-


boo = csvContainer(boofn)

res = boo.aggregate('pax', 'arr_port', lambda a, b: a + b)

top10 = sorted(res, key = res.get, reverse = True)[0:10]

[(i, res[i]) for i in top10]