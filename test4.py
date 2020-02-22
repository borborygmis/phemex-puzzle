# -*- coding: utf-8 -*-
"""
Try epoch dates and stuff.
1. convert words to hex and then to integer
2. convert integer to string and take first 10 chars (like a unix timestamp with millis)
3. multiply these in various ways


Some results and associated reading:

BTCxETH = 2032-08-02
    https://www.reddit.com/r/Bitcoin/comments/b9sgf9/in_the_year_2032/
    https://www.reddit.com/r/Bitcoin/comments/7b29yp/i_have_a_message_from_the_year_2032_in_regards_to/
    https://www.reddit.com/r/Bitcoin/comments/9lvifi/by_2032_about_99_of_btc_will_be_in_circulation/

BTCxXRP = 2049-09-24
    https://twitter.com/cryptomanran/status/1173879097019289600
    https://www.cryptotapas.com/bitcoin-in-2049/

ETHxXRP = 2053-05-03
    https://medium.com/@david_nage/the-year-2053-what-role-will-crypto-play-in-our-lives-768f213206c

PhemexxBTC = 2091-10-13
    hmmm? https://www.reddit.com/r/Ripple/comments/bgmv4a/sbi_to_use_xrp_with_crypto_fund_business_in_the_us/

ETHxPhemex = 2097-04-16
    https://www.reddit.com/r/AMA/comments/9a1md4/i_am_a_time_traveler_from_2097_ama/

XRPxPhemex = 2132-02-29
    https://enjinx.io/eth/asset/34623068

Phemex = 2250-02-27
    https://beincrypto.com/bitcoin-should-reach-1m-by-2250-through-simple-inflation/

"""
import datetime
from util import *

def s10(n):
    return str(n)[:10]

def u2d(u):
    return datetime.datetime.utcfromtimestamp(int(u)).strftime('%Y-%m-%d %H:%M:%S')

def main():
    words = ['BTC', 'ETH', 'XRP', 'Phemex']
    results = {}
    for w in words:
        i = tohn(w)
        results[w] = i
    sr = []    
    for k,v in results.items():
        for kk, vv in results.items():
            #if kk == k: continue
            print('{}x{} = {}'.format(k, kk, u2d(s10(v*vv))))
            #print('{}x{} = {}'.format(k, kk, u2d(
            sx = s10(v*vv*6)
            sr.append(str(sx))
            #print(sx, slen(sx))

    for p in permutations(sr, 3):
        x = ''.join(p)
        #print(slen(x), x)
        test_int(x)
    print('Phemex = {}'.format(u2d(s10(results['Phemex']))))

if __name__ == '__main__':
    main()

"""
OUTPUT:
BTCxETH = 2032-08-02 12:10:51
BTCxXRP = 2049-09-24 17:27:30
BTCxPhemex = 2091-10-13 09:23:03
ETHxBTC = 2032-08-02 12:10:51
ETHxXRP = 2053-05-03 21:46:13
ETHxPhemex = 2097-04-16 05:52:56
XRPxBTC = 2049-09-24 17:27:30
XRPxETH = 2053-05-03 21:46:13
XRPxPhemex = 2132-02-29 12:09:17
PhemexxBTC = 2091-10-13 09:23:03
PhemexxETH = 2097-04-16 05:52:56
PhemexxXRP = 2132-02-29 12:09:17
Phemex = 2250-02-27 14:07:28

BTCxBTC = 2029-11-17 07:27:02
ETHxETH = 2035-06-02 10:42:27 -- https://www.reddit.com/r/Bitcoin/comments/3d5qb2/its_2035_what_is_a_bitcoin_worth_best_case_and/
XRPxXRP = 2076-03-02 10:57:09
PhemexxPhemex = 2217-09-08 08:17:07
"""
