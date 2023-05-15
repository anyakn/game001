import random
import time
import local_karolina as ru
import local_Uly.ru as r
import local_anya as ar

v_health = 150
v_money = 100
v_shelter = 500

health_n = 150
money_n = 100
weapon_n = 500

money_d = 100
health_d = 150
potion = 500

l = [1, 2, 3]
random.shuffle(l)
a = int(l[0])
d = int(l[1])
c = int(l[2])

print(r.gr_1)
time.sleep(5)
print('')
print(r.gr_2)
time.sleep(10)
print('')
print(r.gr_3)
time.sleep(10)
print('')
print(r.gr_4)
time.sleep(10)
print('')
print(r.gr_5)
time.sleep(10)
print('')
print(r.gr_6)
time.sleep(10)
print('')
print(r.gr_7)
time.sleep(10)
print('')
print(r.gr_8)
time.sleep(10)
print('')
print(r.gr_9)
time.sleep(10)
print('')
print(r.gr_10)
print('')
time.sleep(10)

fb1 = input(ar.fb1)
if fb1 != '1':
    print(ar.mtv1)
    print('')
time.sleep(5)
print(ar.dst1, a)
print(ar.dst2, d)
print(ar.dst3, c)
print('')
print(ar.dst4)
print('')
time.sleep(5)
fb2 = input(ar.fb2)
if fb2 == '1':
    print(ar.ans1)
    print('')
else:
    print(ar.mtv1)
    print('')
time.sleep(5)

while health_d > 0 and v_health > 0 and health_n > 0:
    print(ru.st1)
    print('')
    print(ru.st2)
    print('')
    time.sleep(1)
    print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
    time.sleep(3)
    print('')
    print(ru.st3)
    time.sleep(3)
    print(ru.ch1)
    time.sleep(2)
    print('')
    print(ru.plot_1)
    print(ru.plot_2)
    print(ru.plot_3)
    print('')
    time.sleep(9)
    print(ru.plot_4)
    print(ru.plot_5)
    print(ru.plot_6)
    print('')
    time.sleep(9)
    print(ru.plot_7)
    print(ru.plot_8)
    print(ru.plot_9)
    print('')
    time.sleep(5)
    print(ru.altering_1)
    print(ru.altering_2)
    print('')
    time.sleep(3)
    print(ru.plot_10)
    print('')
    time.sleep(3)
    print(ru.altering_3)
    print('')
    time.sleep(2)
    print(ru.plot_11)

    ans_1 = input(ru.des_1)
    if ans_1 == 1:
        if v_health >= 10 and potion >= 20:
            v_health -= 10
            v_money += 20
            potion -= 20
        else:
            v_shelter += 20
            print(ru.outcome_1)
    elif ans_1 == 2:
        v_shelter += 20
    print('')
    print(ru.st4)
    print('')
    time.sleep(2)
    if  v_health == 0:
        print(ru.outcome_5)
        break
    time.sleep(2)
    ans_10 = input(ru.res0)
    print('')
    if ans_10 == 1:
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
        print('')
    else:
        print(ru.st5)
        print('')


    print(r.prm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
    time.sleep(5)
    print('')
    print(r.chc_1)
    time.sleep(5)
    print('')
    print(r.dcn_1)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch20, '\n', r.cns_ch15)
    print(r.dff_enemy, '\n', r.hlt_ch30, '\n', r.ptn_ch30)
    time.sleep(5)
    print('')
    print(r.dcn_2)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch30, '\n', r.wpn_ch20)
    print(r.dff_ppl, '\n', r.hlt_ch_pl30, '\n', r.sht_ch_pl10)
    time.sleep(5)
    print('')
    sl_1 = input(r.sl)
    if sl_1 == '1':
        if health_n >= 20:
            health_n -= 20
            money_n += 15
            health_d -= 30
            potion -= 30
        else:
            print(r.rsr)
    elif sl_1 == '2':
        if health_n >= 30 and weapon_n >= 20:
            health_n -= 30
            weapon_n -= 20
            v_health += 30
            v_shelter += 10
        else:
            print(r.rsr)
    print('')
    print(r.dn)
    time.sleep(5)
    print('')
    if health_n <= 0 or health_d <= 0 or v_health <= 0:
        break
    stt_1 = input(r.stt)
    print('')
    if stt_1 == '1':
        print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        print('')
    else:
        print(r.pl_fur)
        print('')

    print(ar.check1, money_d, ar.check2, health_d, ar.check3, potion, ar.check4)
    print('')
    time.sleep(5)
    print(ar.cha1)
    time.sleep(10)
    print('')
    print(ar.cha2)
    print(ar.cha3, '\n', ar.cha4, '\n', ar.cha5)
    print(ar.cha6, '\n', ar.cha7, '\n', ar.cha8)
    time.sleep(10)
    print('')
    print(ar.cha9)
    print(ar.cha3, '\n', ar.cha10, '\n', ar.cha11)
    print(ar.cha12,  '\n', ar.cha13)
    time.sleep(10)
    print('')
    ch1 = input(ar.ch1)
    if ch1 == '1':
        if health_d >= 14 and potion >= 11:
            health_d -= 14
            potion -= 11
            health_n -= 15
            weapon_n -= 10
        else:
            print(ar.rfs1)
    elif ch1 == '2':
        if health_d >= 12 and potion >= 13:
            health_d -= 12
            potion -= 13
            v_shelter -= 25
        else:
            print(ar.rfs1)
    print(ar.mtv2)
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <=0 or v_health <= 0:
        break
    ch2 = input(ar.ch2)
    if ch2 == '1':
        print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
        print('')
    else:
        print(ar.ans2)
        print('')


    print(ru.st6)
    print('')
    print(ru.st7)
    time.sleep(2)
    rand_event1_v = random.randint(1, 2)
    if rand_event1_v == 1:
        print(ru.possible_1)
        v_money += 20
    else:
        print(ru.possible_2)
        if v_shelter >= 40:
            v_shelter -= 40
        else:
            v_shelter = 0
        time.sleep(1)
        print(ru.possible_3)
        time.sleep(1)
        ans_3 = input(ru.des_2)
        if ans_3 == 1:
            if v_money >= 30:
                v_money -= 30
                v_shelter += 20
            else:
                print(ru.outcome_2)
        else:
            print(ru.outcome_8)

    if v_health == 0:
        print(ru.outcome_4)
        break

    ans_4 = input(ru.res0)
    print('')
    if ans_4 == 1:
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
        print('')
    else:
        print(ru.st5)
        print('')

    print(r.rd)
    print('')
    print(r.be_rd_1)
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print(r.event_1)
        weapon_n += 50
        print('')
        pr_1 = input(r.stt)
        if pr_1 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.pl_fur)
    else:
        print(r.event_2)
        if health_n >= 20:
            health_n -= 20
        else:
            health_n = 0
        if weapon_n >= 20:
            weapon_n -= 20
        else:
            weapon_n = 0
        print('')
        print(r.rsr_lw)
        time.sleep(5)
        print('')
        pr_2 = input(r.pch_1)
        if pr_2 == '1':
            if money_n >= 30:
                money_n -= 30
                weapon_n += 10
            else:
                print(r.cns_lw)
        else:
            print(r.pl_fur)
        if health_n <= 0:
            break
        pr_3 = input(r.stt)
        if pr_3 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.pl_fur)
            print('')

    fb3 = input(ar.randa1)
    if fb3 != '1':
        print(ar.mtv3)
    print('')
    time.sleep(5)
    rand_event1_d = random.randint(1,2)
    if rand_event1_d == 1:
        print(ar.randa2)
        health_d += 30
        potion += 20
        fb4 = input(ar.ch2)
        if fb4 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
    else:
        print(ar.randa3)
        if health_d >= 20:
            health_d -= 20
        else:
            health_d = 0
        if potion >= 30:
            potion -= 30
        else:
            potion = 0
        fb4 = input(ar.ch2)
        if fb4 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
        time.sleep(5)
        fb5 = input(ar.randa4)
        if fb5 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 20
                print(ar.fb3)
                print('')
            else:
                print(ar.rfs2)
        else:
            print(ar.fb4)
            print('')
        if health_d <= 0:
            break

    print(ru.st6)
    print('')
    time.sleep(3)
    print(ru.ch1)
    time.sleep(2)
    print('')
    print(ru.plot_12)
    print(ru.plot_13)
    time.sleep(5)
    print('')
    print(ru.altering_4)
    print(ru.altering_5)
    time.sleep(3)
    print('')
    print(ru.plot_14)
    print(ru.plot_15)
    print(ru.plot_16)
    print(ru.plot_17)
    time.sleep(9)
    print('')
    print(ru.altering_6)
    print(ru.altering_7)
    time.sleep(3)
    print('')
    print(ru.plot_11)
    time.sleep(1)
    ans_1 = input(ru.des_3)
    if ans_1 == 1:
        if v_health >= 20:
            if health_n >= 20:
                v_health -= 20
                health_n -= 20
            else:
                v_health -= 20
                health_n = 0
        else:
            print(ru.outcome_3)

    elif ans_1 == 2:
        v_health += 10
        if health_n >= 30:
            health_n -= 30
        else:
            health_n = 0
    print('')
    print(ru.st4)
    print('')
    time.sleep(2)

    if health_n == 0:
        print(ru.outcome_4)
        break
    elif v_health == 0:
        print(ru.outcome_5)
        break
    ans_40 = input(ru.res0)
    print('')
    if ans_40 == 1:
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
        print('')
    else:
        print(ru.st5)
        print('')



    print(r.chc_2)
    time.sleep(5)
    print('')
    print(r.event_3, '\n', r.dcn_3)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch20, '\n', r.wpn_ch20)
    print(r.dff_enemy, '\n', r.hlt_ch40, '\n', r.ptn_ch10)
    time.sleep(5)
    print('')
    print(r.dcn_4)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch10, '\n', r.cns_ch30)
    print(r.dff_ppl, '\n', r.cns_ch_pl20, '\n', r.sht_ch_pl30)
    time.sleep(5)
    print('')
    sl_2 = input(r.sl)
    if sl_2 == '1':
        if health_n >= 20 and weapon_n >= 20:
            health_n -= 20
            weapon_n -= 20
            health_d -= 40
            potion -= 10
        else:
            print(r.rsr)
    elif sl_2 == '2':
        if health_n >= 10 and money_n >= 30:
            health_n -= 10
            money_n -= 30
            v_money += 20
            v_shelter += 30
        else:
            print(r.rsr)
    print('')
    print(r.dn)
    time.sleep(5)
    print('')
    if health_d <= 0 or health_n <= 0 or v_health <= 0:
        break
    stt_2 = input(r.stt)
    print('')
    if stt_2 == '1':
        print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        print('')
    else:
        print(r.pl_fur)
        print('')

    cp = input(ar.chb1)
    if cp != '1':
        print(ar.mtv1)
        print('')
    print(ar.check1, money_d, ar.check2, health_d, ar.check3, potion, ar.check4)
    print('')
    time.sleep(5)
    print(ar.chb2)
    print(ar.chb3)
    time.sleep(10)
    print('')
    print(ar.chb4)
    print(ar.chb5, '\n', ar.chb6, '\n', ar.chb7, '\n', ar.chb8)
    print(ar.chb9, '\n', ar.chb10)
    print(ar.chb11, '\n', ar.chb12, '\n', ar.chb13)
    time.sleep(10)
    print('')
    print(ar.chb14)
    print(ar.chb5, '\n', ar.chb15, '\n', ar.chb16)
    print(ar.chb9,  '\n', ar.chb17, '\n', ar.chb18)
    time.sleep(10)
    print('')
    ch3 = input(ar.ch1)
    if ch3 == '1':
        if health_d >= 5 and potion >= 25:
            health_d -= 5
            potion -= 25
            money_d += 20
            weapon_n -= 30
            v_health -= 20
            v_shelter -= 15
        else:
            print(ar.rfs1)
    elif ch3 == '2':
        if health_d >= 10 and potion >= 20:
            health_d -= 10
            potion -= 20
            weapon_n -= 25
            health_n -= 5
        else:
            print(ar.rfs1)
    print(ar.mtv2)
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <= 0 or v_health <= 0:
        break
    ch4 = input(ar.ch2)
    if ch4 == '1':
        print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
        print('')
    else:
        print(ar.ans2)
        print('')

    print(ru.st9)
    print(ru.st7)
    time.sleep(3)
    rand_event1_d = random.randint(1, 2)
    if rand_event1_d == 1:
        print(ru.possible_4)
        v_money += 20
    else:
        print(ru.possible_5)
        if v_shelter >= 30:
            v_shelter -= 30
            if v_health >= 20:
                v_health -= 20
            else:
                v_health = 0
        else:
            v_shelter = 0
        print(ru.possible_3)
        time.sleep(1)
        print('')
    ans_6 = input(ru.des_4)
    print('')
    if ans_6 == 1:
        if v_money >= 30:
            v_money -= 30
            v_shelter += 15
        else:
            print(ru.outcome_6)
            ans_7 = input(ru.des_5)
            print('')
            if ans_7 == 1:
                if v_money >= 20:
                    v_money -= 20
                    v_health += 10
                else:
                    print(ru.outcome_6)
    else:
        ans_80 = input(ru.des_5)
        print('')
        if ans_80 == 1:
            if v_money >= 20:
                v_money -= 20
                v_health += 10
            else:
                print(ru.outcome_6)
        else:
            print('Похоже, вы уверены в своих силах! Так держать!')
            print('')

    if v_health == 0:
        break
        print(ru.outcome_5)

    ans_5 = input(ru.res0)
    print('')
    if ans_5 == 1:
        print('')
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
        print('')
    else:
        print(ru.st5)
    print('')

    print(r.chc_3)
    print('')
    print(r.be_rd_2)
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print(r.event_4)
        health_n += 20
        print('')
        pr_4 = input(r.stt)
        if pr_4 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.mt_1)
    else:
        print(r.event_5)
        if weapon_n >= 50:
            weapon_n -= 50
        else:
            weapon_n = 0
        print('')
        print(r.mt_2)
        time.sleep(5)
        print('')
        pr_5 = input(r.pch_2)
        if pr_5 == '1':
            if money_n >= 30:
                money_n -= 30
                weapon_n += 30
            else:
                print(r.cns_lw)
        else:
            print(r.pl_fur)
        if health_n <= 0:
            break
        pr_6 = input(r.stt)
        if pr_6 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.pl_fur)
            print('')

    fb6 = input(ar.randb1)
    if fb6 != '1':
        print(ar.mtv3)
    print('')
    time.sleep(5)
    rand_event1_d = random.randint(1,2)
    if rand_event1_d == 1:
        print(ar.randb2)
        health_d += 30
        potion += 10
        fb7 = input(ar.ch2)
        if fb7 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
    else:
        print(ar.randb3)
        if health_d >= 30:
            health_d -= 30
        else:
            health_d = 0
        fb7 = input(ar.ch2)
        if fb7 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
        time.sleep(5)
        fb8 = input(ar.randb4)
        if fb8 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 30
                print(ar.fb3)
                print('')
            else:
                print(ar.rfs2)
        elif fb8 == '2':
            if money_d >= 25:
                money_d -= 25
                potion += 30
                print(ar.fb3)
                print('')
            else:
                print(ar.rfs2)
        else:
            print(ar.fb4)
            print('')
        if health_d <= 0:
            break

    print(ru.st9)
    print('')
    time.sleep(3)
    print(ru.ch1)
    time.sleep(2)
    print('')
    print(ru.plot_17)
    print(ru.plot_18)
    time.sleep(5)
    print('')
    print(ru.altering_10)
    print(ru.altering_11)
    time.sleep(3)
    print('')
    print(ru.plot_19)
    print(ru.plot_20)
    print('')
    time.sleep(9)
    print(ru.altering_12)
    print(ru.altering_13)
    time.sleep(3)
    print('')
    print(ru.plot_11)
    time.sleep(1)
    ans_14 = input(ru.des_6)
    if ans_14 == 1:
        if v_health >= 20:
            if health_n >= 20:
                v_health -= 20
                health_d -= 20
            else:
                v_health -= 20
                health_n = 0
        else:
            print(ru.outcome_7)
            if v_money >= 20:
                v_money -= 20
                money_n += 20
                health_n += 10
            else:
                money_n += v_money
                v_money = 0
                health_n += 10

    elif ans_14 == 2:
        if v_money >= 20:
            v_money -= 20
            money_n += 20
            health_n += 10
        else:
            money_n += v_money
            v_money = 0
            health_n += 10
    print('')
    print(ru.st4)
    print('')
    time.sleep(2)

    if v_health == 0:
        print(ru.outcome_5)
        break

    ans_17 = input(ru.res0)
    print('')
    if ans_17 == 1:
        print('')
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
        print('')
    else:
        print(ru.st5)
    print('')

    print(r.chc_4)
    time.sleep(5)
    print('')
    print(r.event_6, '\n', r.dcn_5)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch30, '\n', r.wpn_ch30)
    print(r.dff_enemy, '\n', r.hlt_ch10, '\n', r.ptn_ch30)
    time.sleep(5)
    print('')
    print(r.dcn_6)
    time.sleep(5)
    print('')
    print(r.dff_my, '\n', r.hlt_ch15)
    print(r.dff_ppl, '\n', r.hlt_ch_pl20, '\n', r.sht_ch_pl10)
    time.sleep(5)
    print('')
    sl_3 = input(r.sl)
    if sl_3 == '1':
        if health_n >= 30 and weapon_n >= 30:
            health_n -= 30
            weapon_n -= 30
            health_d -= 10
            potion -= 30
        else:
            print(r.rsr)
    elif sl_3 == '2':
        if health_n >= 15:
            health_n -= 15
            v_money += 20
            v_shelter += 10
        else:
            print(r.rsr)
    print('')
    print(r.dn)
    print('')
    if health_d <= 0 or health_n <= 0 or v_health <= 0:
        break
    stt_3 = input(r.stt)
    print('')
    if stt_3 == '1':
        print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        print('')
    else:
        print(r.pl_fur)
        print('')

    ch5 = input(ar.chc1)
    if ch5 != '1':
        print(ar.mtv1)
        print('')
    print(ar.chc2)
    time.sleep(10)
    print('')
    print(ar.chc3)
    print(ar.chc4, '\n', ar.chc5, '\n', ar.chc6)
    print(ar.chc7, '\n', ar.chc8, '\n', ar.chc9)
    time.sleep(10)
    print('')
    print(ar.chc10)
    print(ar.chc4, '\n', ar.chc11, '\n', ar.chc12)
    time.sleep(10)
    ch6 = input(ar.ch1)
    if ch6 == '1':
        if health_d >= 20 and potion >= 15:
            health_d -= 20
            potion -= 15
            v_health -= 27
            v_shelter -= 12
        else:
            print(ar.rfs1)
    elif ch6 == '2':
        health_d += 30
        potion += 20
    print(ar.mtv2)
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <=0 or v_health <= 0:
        break
    ch7 = input(ar.ch2)
    if ch7 == '1':
        print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
        print('')
    else:
        print(ar.ans2)
        print('')

    print(ru.st10)
    print(ru.st7)
    time.sleep(1)
    rand_event1_d = random.randint(1, 2)
    if rand_event1_d == 1:
        print(ru.possible_6)
        v_money += 20
        time.sleep(1)
        print('')
    else:
        print(ru.possible_7)
        if v_health >= 30:
            v_health -= 30
        else:
            v_health = 0
        time.sleep(1)
        print(ru.possible_3)
        print('')
        ans_12 = input(ru.des_7)
        if ans_12 == 1:
            if v_money >= 30:
                v_money -= 30
                v_health += 20
            else:
                print(ru.outcome_2)
        else:
            print(ru.outcome_8)
            print('')

    if v_health == 0:
        print(ru.outcome_5)
        break

    ans_13 = input(ru.res0)
    print('')
    if ans_13 == 1:
        print(ru.res1, '\n', ru.res2, v_health, '\n', ru.res3, v_money, '\n', ru.res4, v_shelter)
    else:
        print(ru.st5)

    print(r.chc_5)
    print('')
    print(r.be_rd_3)
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print(r.event_7)
        health_n += 15
        print('')
        pr_7 = input(r.stt)
        if pr_7 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.mt_1)
    else:
        print(r.event_8)
        if weapon_n >= 20:
            weapon_n -= 20
        else:
            weapon_n = 0
        if health_n >= 40:
            health_n -= 40
        else:
            health_n = 0
        print('')
        print(r.mt_3)
        time.sleep(5)
        print('')
        pr_8 = input(r.pch_3)
        if pr_8 == '1':
            if money_n >= 30:
                money_n -= 30
                health_n += 20
            else:
                print(r.cns_lw)
        else:
            print(r.pl_fur)
        if health_n <= 0:
            break
        pr_9 = input(r.stt)
        if pr_9 == '1':
            print(r.sm, '\n', r.hlt, health_n, '\n', r.cns, money_n, '\n', r.wpn, weapon_n)
        else:
            print(r.pl_fur)

    fb9 = input(ar.randc1)
    if fb9 != '1':
        print(ar.mtv3)
    print('')
    rand_event1_d = random.randint(1,2)
    time.sleep(5)
    if rand_event1_d == 1:
        print(ar.randc2)
        health_d += 20
        potion += 18
        fb10 = input(ar.ch2)
        if fb10 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
    else:
        print(ar.randc3)
        if health_d >= 30:
            health_d -= 30
        else:
            health_d = 0
        fb11 = input(ar.ch2)
        if fb11 == '1':
            print(ar.check5, '\n', ar.check6, health_d, '\n', ar.check7, money_d, '\n', ar.check8, potion)
            print('')
        else:
            print(ar.ans2)
            print('')
        time.sleep(5)
        fb12 = input(ar.randc4)
        if fb12 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 20
                print(ar.fb3)
                print('')
            else:
                print(ar.rfs2)
        elif fb12 == '2':
            if money_d >= 25:
                money_d -= 25
                potion += 17
                print(ar.fb3)
                print('')
            else:
                print(ar.rfs2)
        else:
            print(ar.fb4)
            print('')
        if health_d <= 0:
            break
time.sleep(5)


if  health_n > 0 and health_d > 0:
    print(ru.ft_1)
    print('')
    print(ru.ft_2)
    print(ru.ft_3)
    print('')
    print(ru.ft_4)
    print(ru.ft_5)
    print(ru.ft_6)
    print(ru.ft_7)
    points_n = health_n * 0.4 + weapon_n * 0.6
    points_d = health_d * 0.4 + potion * 0.6
    if points_n > points_d:
        print(ru.ft_8)
        print('')
        print(ru.ft_9)
    elif points_n < points_d:
        print(ru.ft_8)
        print('')
        print(ru.ft_10)
    else:
        print(ru.ft_11)
        print(ru.ft_12)
        rand_event1_d = random.randint(1, 2)
        if rand_event1_d == 1:
            print(ru.ft_8)
            print('')
            print(ru.ft_10)
        else:
            print(ru.ft_8)
            print('')
            print(ru.ft_9)

if health_d <= 0:
    print(ar.war1)

if v_health > 0 and health_d > 0:
    print(ar.war2)
    print('')
    print(ar.war3)
    print('')
    print(ar.war4)
    time.sleep(10)
    points_v = v_health * 0.4 + v_shelter * 0.6
    points_d = health_d * 0.4 + potion * 0.6
    if points_v > points_d:
        print(ar.war5)
        time.sleep(5)
        print('')
        print(ar.war6)
    elif points_v < points_d:
        print(ar.war5)
        time.sleep(5)
        print('')
        print(ar.war7)
    else:
        print(ar.war8)
        rand_event2_d = random.randint(1, 2)
        if rand_event2_d == 1:
            print(ar.war5)
            time.sleep(5)
            print('')
            print(ar.war6)
        else:
            print(ar.war5)
            time.sleep(5)
            print('')
            print(ar.war7)
time.sleep(5)
print(ar.war9)
