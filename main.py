import random
import time
import local_karolina as ru
import local_Uly.ru as r

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

fb1 = input('Вы готовы узнать узнать как магический шар распределил вас на команды? Введите "1", чтобы продолжить ')
if fb1 != '1':
    print('Удивительное приключение ждёт вас! Не время сдаваться!')
    print('')
time.sleep(5)
print('Право обладать силой ангелов принадлежит команде', a)
print('Право властвовать отродьями ада принадлежит команде', d)
print('Право управлять судьбой местных жителей принадлежит команде', c)
print('')
print('Примите наши поздравления!')
print('')
time.sleep(5)
fb2 = input('Введите "1", чтобы начать эту легендарную битву! ')
if fb2 == '1':
    print('Отлично! Начинаем!')
    print('')
else:
    print('Удивительное приключение ждёт вас! Не время сдаваться!')
    print('')
time.sleep(5)

while health_d > 0 and v_health > 0 and health_n > 0:
    print(ru.st1)
    print('')
    print(ru.st2)
    print('')
    time.sleep(1)
    print(ru.res0, '\n', ru.res1, v_health, '\n', ru.res2, v_money, '\n', ru.res3, v_shelter)
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
        print(ru.res0, '\n', ru.res1, v_health, '\n', ru.res2, v_money, '\n', ru.res3, v_shelter)
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

    print('Демоны! У вас есть', money_d, 'монет,', health_d, 'здоровья и', potion, 'зелья!')
    print('')
    time.sleep(5)
    print('Демоны! Вам предстоит сделать судьбоносный выбор... Аид в ярости из-за проделок нефилимов. Покажите кто тут господин!')
    time.sleep(10)
    print('')
    print('Радуйтесь больше смерти! У него уже есть заготовленный коварный план - ночное нападение на нефилимов!')
    print('Как меняются ваши ваши параметры:', '\n', '"Здоровье" -14', '\n', '"Зелье" -11')
    print('Как меняются параметры нефилимов:', '\n', '"Здоровье" -25', '\n', '"Оружие" -10')
    time.sleep(10)
    print('')
    print('Но вы можете выбрать план похитрее... Нападите на тех, кого они защищают - местных жителей. Вот этого-то они точно не ожидают!')
    print('Как меняются ваши параметры:', '\n', '"Здоровье" -12', '\n', '"Зелье" -13')
    print('Как меняются параметры мирных жителей:',  '\n', '"Убежище" -25')
    time.sleep(10)
    print('')
    ch1 = input('Если вы выбираете 1 вариант, то введите "1". Если вы выбираете 2 вариант, то введите "2": ')
    if ch1 == '1':
        if health_d >= 14 and potion >= 11:
            health_d -= 14
            potion -= 11
            health_n -= 15
            weapon_n -= 10
        else:
            print('Упс... Походу у вас недостаточно ресурсов')
    elif ch1 == '2':
        if health_d >= 12 and potion >= 13:
            health_d -= 12
            potion -= 13
            v_shelter -= 25
        else:
            print('Упс... Походу у вас недостаточно ресурсов')
    print('Будем надеяться этот выбор приведёт вас к победе!')
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <=0 or v_health <= 0:
        break
    ch2 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch2 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
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
        print(ru.res0, '\n', ru.res1, v_health, '\n', ru.res2, v_money, '\n', ru.res3, v_shelter)
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

    fb3 = input('Демоны, приготовьтесь к первому случайному событию! Введите "1", чтобы продолжить ')
    if fb3 != '1':
        print('Не время вешать нос! Фантастическая битва ждёт вас!')
    print('')
    time.sleep(5)
    rand_event1_d = random.randint(1,2)
    if rand_event1_d == 1:
        print('Да вы сегодня везунчик! Шабаш! Вы увеличили "Здоровье" на 30 и "Зелье" на 20!')
        health_d += 30
        potion += 20
        fb4 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb4 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжаем битву!')
            print('')
    else:
        print('Сегодня явно не ваш день! Зельевар заболел! Вы потеряли 20 "здоровья" и 30 "зелья"...')
        if health_d >= 20:
            health_d -= 20
        else:
            health_d = 0
        if potion >= 30:
            potion -= 30
        else:
            potion = 0
        fb4 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb4 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжам битву!')
            print('')
        time.sleep(5)
        fb5 = input('Вы хотите потратить 30 монет, чтобы увеличить "здоровье" на 20? Если да, введите "1" ')
        if fb5 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 20
                print('Да я смотрю вы настроены на победу!')
                print('')
            else:
                print('Упс.. Походу у вас не хватает монет')
        else:
            print('Да я смотрю вы уверены в своих силах! Так держать, боец!')
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
        print(ru.res0, '\n', ru.res1, v_health, '\n', ru.res2, v_money, '\n', ru.res3, v_shelter)
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

    cp = input('Вам предстоит сделать второй важный выбор, мои злодеи! Введите "1", чтобы продолжить ')
    if cp != '1':
        print('Удивительное приключение ждёт вас! Не время сдаваться!')
        print('')
    print('Демоны! У вас есть', money_d, 'монет,', health_d, 'здоровья и', potion, 'зелья!')
    print('')
    time.sleep(5)
    print('Демоны! Ваш повелитель нуждается в вас! От вашего решения будет зависеть будущее всего подземного царства!')
    print('Нефилимы и мирные жители вышли за пределы дозволенного: они устоили тайный заговор. К счастью, наши хитрые разведчики не дремлют!')
    time.sleep(10)
    print('')
    print('Нефилимы хотят переправить своё оружие этим бездарным созданиям! Не позвольте же им это сделать! Устройте им подлянку на месте встречи!')
    print('Как меняются ваши ваши параметры:', '\n', '"Здоровье" -5', '\n', '"Зелье" -25', '\n', '"Монеты" +20')
    print('Как меняются параметры нефилимов:', '\n', '"Оружие" -30')
    print('Как меняются параметры мирных жителей:', '\n', '"Здоровье" -20', '\n', '"Убежище" -15')
    time.sleep(10)
    print('')
    print('Но какой же большой соблазн проучить этих нефилимов! Может добавить им огонька к оружейке?')
    print('Как меняются ваши параметры:', '\n', '"Здоровье" -10', '\n', '"Зелье" -20')
    print('Как меняются параметры нефилимов:',  '\n', '"Оружие" -25', '\n', '"Здоровье" -5')
    time.sleep(10)
    print('')
    ch3 = input('Если вы выбираете 1 вариант, то введите "1". Если вы выбираете 2 вариант, то введите "2": ')
    if ch3 == '1':
        if health_d >= 5 and potion >= 25:
            health_d -= 5
            potion -= 25
            money_d += 20
            weapon_n -= 30
            v_health -= 20
            v_shelter -= 15
        else:
            print('Упс... Походу у вас недостаточно ресурсов')
    elif ch3 == '2':
        if health_d >= 10 and potion >= 20:
            health_d -= 10
            potion -= 20
            weapon_n -= 25
            health_n -= 5
        else:
            print('Упс... Походу у вас недостаточно ресурсов')
    print('Будем надеяться этот выбор приведёт вас к победе!')
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <= 0 or v_health <= 0:
        break
    ch4 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch4 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
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
    ans_6 = input('Введите "1", если хотите потратить 30 "монет" чтобы добавить +15 "убежища": ')
    print('')
    if ans_6 == 1:
        if v_money >= 30:
            v_money -= 30
            v_shelter += 15
        else:
            print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
            ans_7 = input('Введите "1", если хотите потратить 20 "монет" чтобы добавить +10 "здоровья": ')
            print('')
            if ans_7 == 1:
                if v_money >= 20:
                    v_money -= 20
                    v_health += 10
                else:
                    print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
            else:
                ans_80 = input('Введите "1", если хотите потратить 20 "монеты" чтобы добавить +10 "здоровья": ')
                print('')
                if ans_80 == 1:
                    if v_money >= 20:
                        v_money -= 20
                        v_health += 10
                    else:
                        print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
                else:
                    print('Похоже, вы уверены в своих силах! Так держать!')
                    print('')

    if v_health == 0:
        break
        print('Местные жители проиграли!')

    ans_5 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_5 == 1:
        print('')
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
        print('')
    else:
        print('Отличная работа!')
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

    fb6 = input('Демоны, приготовьтесь ко второму случайному событию! Введите "1", чтобы продолжить ')
    if fb6 != '1':
        print('Не время вешать нос! Фантастическая битва ждёт вас!')
    print('')
    time.sleep(5)
    rand_event1_d = random.randint(1,2)
    if rand_event1_d == 1:
        print('Да провалиться вам сквозь землю! Удача на вашей стороне! Сегодня полнолуние! Вы увеличили "здоровье" на 30 и "зелье" на 10!')
        health_d += 30
        potion += 10
        fb7 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb7 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжаем битву!')
            print('')
    else:
        print('Жизнь не бывает всегда так благосклонна! Сегодня солнцестояние! Ваше "здоровье" уменьшилось на 30!')
        if health_d >= 30:
            health_d -= 30
        else:
            health_d = 0
        fb7 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb7 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжам битву!')
            print('')
        time.sleep(5)
        fb8 = input('Введите "1", чтобы потрать 30 "монет" на +30 "здоровья" или введите "2", чтобы за 25 "монет" купить +30 "зелья" ')
        if fb8 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 30
                print('Да я смотрю вы настроены на победу!')
                print('')
            else:
                print('Упс.. Походу у вас не хватает монет')
        elif fb8 == '2':
            if money_d >= 25:
                money_d -= 25
                potion += 30
                print('Да я смотрю вы настроены на победу!')
                print('')
            else:
                print('Упс.. Походу у вас не хватает монет')
        else:
            print('Да я смотрю вы уверены в своих силах! Так держать, боец!')
            print('')
        if health_d <= 0:
            break

    print('Мирные жители, пришло время продолжить игру.')
    print('')
    time.sleep(3)
    print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
    time.sleep(2)
    print('')
    print('Вы уже давно не вступали в бой я демонами...Пора бы уже дать отдохнуть Ангелам, да и ваши параметры успели')
    print('неплохо восстоновится. Нельзя давать врагу время на отдых! Хотите собрать отряд? ')
    time.sleep(5)
    print('')
    print('Изменения ваших параметров: здоровье -20')
    print('Изменение параметров Демонов: здоровье -20    зелья -10')
    time.sleep(3)
    print('')
    print('Вот только стоит ли оно того? Могут ли простые смертные заметно ослабить демонов? Не лучше ли помочь')
    print('восстоновится Ангелам, чтобы они уже сошлись с нечистью в равной схватке?')
    print('')
    time.sleep(9)
    print('Изменения ваших параметров: деньги -20')
    print('Изменение параметров Ангелов: деньги +20  здоровье +10')
    time.sleep(3)
    print('')
    print('Каким путём вы последуете в этот раз?')
    time.sleep(1)
    ans_14 = int(input('Введите "1",если хотите помочь ангелам; '
                       'Введите "2",если хотите отказать в помощи: '))
    if ans_14 == 1:
        if v_health >= 20:
            if health_n >= 20:
                v_health -= 20
                health_d -= 20
            else:
                v_health -= 20
                health_n = 0
        else:
            print(
                'Похоже, у вас недостаточно ресурсов для этого выбора... И всё же, вы должны помочь Ангелам, даже если лишь матриально!')
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
    print('Выбор сделан! ')
    print('')
    time.sleep(2)

    if v_health == 0:
        print('Местные жители проиграли!')
        break

    ans_17 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_17 == 1:
        print('')
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
        print('')
    else:
        print('Отличная работа!')
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

    ch5 = input('Демоны! Вам в третий раз предстоит сделать сложный выбор! Введите "1", чтобы продолжить ')
    if ch5 != '1':
        print('Удивительное приключение ждёт вас! Не время сдаваться!')
        print('')
    print('Демоны! Аид посылает вас на последнюю бивтву! '
          'Выполните уже наконец свою главную миссию и станьте властителями этого мира!')
    time.sleep(10)
    print('')
    print('Покажите этим мирным жителям наконец как надо биться! Зададим им жару!')
    print('Как меняются ваши ваши параметры:', '\n', '"Здоровье" -20', '\n', '"Зелье" -15')
    print('Как меняются параметры мирных жителей:', '\n', '"Здоровье" -27', '\n', '"Убежище" -12')
    time.sleep(10)
    print('')
    print('Битва битвой, но о себе заботиться тоже надо! Хотите остаться в своём логове и восстановить силы?')
    print('Как меняются ваши параметры:', '\n', '"Здоровье" +30', '\n', '"Зелье" +20')
    time.sleep(10)
    ch6 = input('Если вы выбираете 1 вариант, то введите "1". Если вы выбираете 2 вариант, то введите "2" ')
    if ch6 == '1':
        if health_d >= 20 and potion >= 15:
            health_d -= 20
            potion -= 15
            v_health -= 27
            v_shelter -= 12
        else:
            print('Упс... Походу у вас недостаточно ресурсов')
    elif ch6 == '2':
        health_d += 30
        potion += 20
    print('Будем надеяться этот выбор приведёт вас к победе!')
    print('')
    time.sleep(5)
    if health_n <= 0 or health_d <=0 or v_health <= 0:
        break
    ch7 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch7 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
        print('')

    input('Мирные жители, пора испытать удачу!')
    print('Время не ждёт! Скрестите пальцы!')
    time.sleep(1)
    rand_event1_d = random.randint(1, 2)
    if rand_event1_d == 1:
        print('Эх, не зря говорят, что земля - кормилица! Благодоря большому урожаю, вы получили +20 "монет".')
        v_money += 20
        time.sleep(1)
        print('')
    else:
        print('Могло быть и хуже, но некуда. В вашем поселении эпидемия дизентерии, "здоровье" уменьшилось на 30')
        if v_health >= 30:
            v_health -= 30
        else:
            v_health = 0
        time.sleep(1)
        print('Кажется, у вас появилась проблема...')
        print('')
        ans_12 = input('Введите "1", если хотите потратить 30 "монет" чтобы добавить +20 "здоровья"')
        if ans_12 == 1:
            if v_money >= 30:
                v_money -= 30
                v_health += 20
            else:
                print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
        else:
            print('Похоже, выы уверены в своих силах! Так держать!')
            print('')

    if v_health == 0:
        print('Местные жители проиграли!')
        break

    ans_13 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_13 == 1:
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    else:
        print('Продолжим!')

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

    fb9 = input('Демоны, приготовьтесь к финальному третьему случайному событию! Введите "1", чтобы продолжить ')
    if fb9 != '1':
        print('Не время вешать нос! Фантастическая битва ждёт вас!')
    print('')
    rand_event1_d = random.randint(1,2)
    time.sleep(5)
    if rand_event1_d == 1:
        print('Демоническая удача! Вы получили жертвоприношение! Вы увеличили "здоровье" на 20 и "зелье" на 18!')
        health_d += 20
        potion += 18
        fb10 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb10 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжаем битву!')
            print('')
    else:
        print('Походу судьба не хочет быть к вам блогосклонной... Обстрел серебрянными пулями! "Здоровье" уменьшилось на 30!')
        if health_d >= 30:
            health_d -= 30
        else:
            health_d = 0
        fb11 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if fb11 == '1':
            print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
            print('')
        else:
            print('Продолжам битву!')
            print('')
        time.sleep(5)
        fb12 = input('Введите "1", чтобы потрать 30 "монет" на +20 "здоровья" или введите "2", чтобы за 25 "монет" купить +17 "зелья" ')
        if fb12 == '1':
            if money_d >= 30:
                money_d -= 30
                health_d += 20
                print('Да я смотрю вы настроены на победу!')
                print('')
            else:
                print('Упс.. Походу у вас не хватает монет')
        elif fb12 == '2':
            if money_d >= 25:
                money_d -= 25
                potion += 17
                print('Да я смотрю вы настроены на победу!')
                print('')
            else:
                print('Упс.. Походу у вас не хватает монет')
        else:
            print('Да я смотрю вы уверены в своих силах! Так держать, боец!')
            print('')
        if health_d <= 0:
            break


if  health_n > 0 and health_d > 0:
    print('Ох-ох-ох! Похоже, теперь вы остались вдвоём... Нефилимы против Демонов. Эта битва будет легендарной!')
    print('')
    print('Победитель будет определен исходя из набранных за игру очков. Для этого мы проверим "здоровье" обеих команд')
    print('а также их "зелья" и "оружие", причём здоровье повлияет на победу на 40%,а второй параметр - на целых 60!')
    print('')
    print('«Адский день! Легко оглохнуть от дикого, неумолкного рева армий. Острые клинки, свистящие в небесах, '
          'визжали, шикали и, как град, осыпаются на землю смертоносным дождём; вспышки заклинаний, посланых в самый '
          'центр поля битвы, поражают молниеносно, не давая и шанса осмыслить происходящее... Однако сегодня с этого '
          'боя выйдет лишь один победитель...')
    points_n = health_n * 0.4 + weapon_n * 0.6
    points_d = health_d * 0.4 + potion * 0.6
    if points_n > points_d:
        print('Победу одержали...')
        print('')
        print('Нефилимы!')
    elif points_n < points_d:
        print('Победу одержали...')
        print('')
        print('Демоны!')
    else:
        print('Похоже, силы противников оказались равны... А значит, воины могут полагаться лишь на удачу. '
              'Пусть всё решиться волей случая!')
        rand_event1_d = random.randint(1, 2)
        if rand_event1_d == 1:
            print('Победу одержали...')
            print('')
            print('Демоны!')
        else:
            print('Победу одержали...')
            print('')
            print('Нефилимы!')