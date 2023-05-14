import random
import time

v_health = 200
v_money = 100
v_shelter = 500

health_n = 200
money_n = 100
weapon_n = 500

money_d = 200
health_d = 100
potion = 500

l = [1, 2, 3]
random.shuffle(l)
a = int(l[0])
d = int(l[1])
c = int(l[2])

print('Добро пожаловать в игру "Fantastic survival"! Пожалуй, начнем погружение в наш мир.')
time.sleep(5)
print('')
print('Есть три клана, за которые вы можете играть. Первый клан - Мирные жители, каковыми и являемся мы с вами. '
      'Второй клан - Демоны, которые '
      'представляют собой вампиров, оборотней и ведьм.')
time.sleep(10)
print('')
print('И последние - это Нефилимы потомки ангелов. Выглядят они как обычные люди, однако в их крови течет ангельская кровь,'
      'что позволяет им иметь нечеловеческую силу и защищать людей.')
time.sleep(10)
print('')
print('Перейдем к концепции игры. В мире идет противостояние, люди страшатся выходить ночами - '
      'за каждым темным углом их поджидают Демоны.')
time.sleep(10)
print('')
print('Однако, Нефилимы были сотворены ангельскими силами, чтобы защищать мир и поддерживать его в балансе. Интересно?')
time.sleep(10)
print('')
print('Вам предстоит пройти несколько уровней: каждый неверный шаг может привести к краху! '
      'Поэтому обдуманно совершайте выбор.')
time.sleep(10)
print('')
print('У каждой из трех команд есть обязательные ресурсы: здоровье и монеты. '
      'При чем, есть и третий - у каждой команды он разный!')
time.sleep(10)
print('')
print('У Мирных жителей - убежище, у Нефилимов - оружие, а у Демонов - зелье.')
time.sleep(10)
print('')
print('Ваша команда, за которую Вы будете играть, будет распределена на рандоме.')
time.sleep(10)
print('')
print('Сохраняйте ваше здоровье, чтобы игра не завершилась для вас. Удачи!')
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
    input('Мирные жители, вы готовы начать игру? ')
    print('')
    print('Вот это настрой! Для начала, ')
    print('')
    time.sleep(1)
    print('Параметры "Мирных жителей":', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    time.sleep(3)
    print('')
    print('Ещё не сбежали? Что же... Тогда, да пребудет с вами сила. Не забывайте, что каждая неудавшаяся попытка — '
          'это еще один шаг вперед.')
    time.sleep(3)
    print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
    time.sleep(2)
    print('')
    print('Эх, опять эта нечисть наводит шуму... Мало им того, что вы вынужденны постоянно скрываться, ')
    print('боясь и шагу ступить в лес, так они ещё и устраивают свои шабаши чуть ли не через день.... ')
    print('Распугали всю живность, а она, конечно, повыбегала из леса прямиком к вашим курятникам. Эх....')
    print('')
    time.sleep(9)
    print('Нет больше сил это терпеть! Старейшины предлагают отправить к поселению нечисти храбрых охотников.')
    print('Пусть проберутся внутрь во время следующего шабаша и украдут зелья из запасов - ')
    print('их с руками оторвут торговцы-кочевники.')
    print('')
    time.sleep(9)
    print('Вот только украденные зелья очень даже могут сыграть с вами злую шутку... Не помните, что лы, ')
    print('как пару лет назад одна разбитая склянка на неделю свалила с десяток парней? ')
    print('Готовы ли вы рискнуть их здоровьем только чтобы насолить шумным соседям и немного подзаработать? ')
    print('')
    time.sleep(5)
    print('Изменения ваших параметров:   здоровье -10, деньги +20')
    print('Изменение параметров Демонов: зелье -20')
    print('')
    time.sleep(3)
    print('Не забывайте, вы можете отказаться от задумки старейшин, и потратить освободившееся время на постройку укреплений.')
    print('')
    time.sleep(3)
    print('Изменения ваших параметров: убежище +20')
    print('')
    time.sleep(2)
    print('Каким путём вы последуете в этот раз?')

    ans_1 = int(input('Введите "1",если хотите последовать решению старейшин; '
                      'Введите "2",если хотите продолжить со вторым вариантом: '))
    if ans_1 == 1:
        if v_health >= 10 and potion >= 20:
            v_health -= 10
            v_money += 20
            potion -= 20
        else:
            v_shelter += 20
            print('Кажется, у вас не хватает ресурсов для этого выбора... Придётся пойти по второму пути')
    elif ans_1 == 2:
        v_shelter += 20
    print('')
    print('Выбор сделан! ')
    print('')
    time.sleep(2)
    ans_10 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_10 == 1:
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
        print('')
    else:
        print('Продолжим!')
        print('')

    print('Параметры "Нефилимов": ', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
    time.sleep(5)
    print('')
    print('Судьба судьбой, но выбор всегда за Вами, дорогие Нефилимы. Есть два пути развития событий.')
    time.sleep(5)
    print('')
    print('1) Вы прокрались в логово Демонов и разграбили зельеварню. Как же так? '
          'Больше Демоны не смогут пополнять здоровье зельем!')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -20', '\n', '"Монеты": +15')
    print('Как меняются параметры противника:', '\n', '"Здоровье": -30', '\n', '"Зелье": -30')
    time.sleep(5)
    print('')
    print('2) Или же... Вы поспешили спасать заплутавших мирных жителей, которые оказались в плену у Демонов.')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -30', '\n', '"Оружие": -20')
    print('Как меняются параметры Мирных жителей:', '\n', '"Здоровье": +30', '\n', '"Убежище": +10')
    time.sleep(5)
    print('')
    sl_1 = input('Если хотите выбрать 1-й исход, то введите "1". Если хотите выбрать 2-й исход, то введите "2": ')
    if sl_1 == '1':
        if health_n >= 20:
            health_n -= 20
            money_n += 15
            health_d -= 30
            potion -= 30
        else:
            print('Кажется, у вас недостаточно ресурсов!')
    elif sl_1 == '2':
        if health_n >= 30 and weapon_n >= 20:
            health_n -= 30
            weapon_n -= 20
            v_health += 30
            v_shelter += 10
        else:
            print('Кажется у вас недостаточно ресурсов!')
    print('')
    print('Выбор сделан!')
    time.sleep(5)
    print('')
    stt_1 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if stt_1 == '1':
        print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        print('')
    else:
        print('Играем дальше!')
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
    ch2 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch2 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
        print('')


    input('Мирные жители, вы готовы испытать удачу вновь?: ')
    print('')
    print('Время не ждёт! Скрестите пальцы на удачу')
    time.sleep(2)

    rand_event1_v = random.randint(1, 2)
    if rand_event1_v == 1:
        print('Якорь мне в бухту! Вы нашли потерянное сокровище пиратов! Вы получили +20 "монет".')
        v_money += 20
    else:
        print('Ох, нет... Спящий вулкан проснулся! Вулканический пепел накрыл часть вашего поселения, -40 "убежища"')
        if v_shelter >= 40:
            v_shelter -= 40
        else:
            v_shelter == 0
        time.sleep(1)
        print('Кажется, у вас появилась проблема...')
        time.sleep(1)
        ans_3 = input('Введите "1", если хотите потратить 30 "монеты" чтобы добавить +20 "убежища": ')
        if ans_3 == 1:
            if v_money >= 30:
                v_money -= 30
                v_shelter += 20
            else:
                print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
        else:
            print('Похоже, выы уверены в своих силах! Так держать!')

    if v_health == 0:
        print('Местные жители проиграли!')

    ans_4 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_4 == 1:
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
        print('')
    else:
        print('Продолжим!')
        print('')

    print('Вы готовы к испытанию?')
    print('')
    print('Приготовьтесь, что же выпало вам на этот раз?')
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print(
            'Сегодня ваш день! Вы заговорили ангельскими силами ваши клинки и это автоматически увеличило урон от оружия. Вы получили +50 "оружия".')
        weapon_n += 50
        print('')
        pr_1 = input('Нажмите "1", чтобы узнать свои текущие параметры: ')
        if pr_1 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Играем дальше!')
    else:
        print(
            'Во время ночного патруля на вас напали дикие животные. Многие в ваших рядах пострадали от такой неожиданности. '
            '"здоровье" и "оружие" уменьшились на 20')
        if health_n >= 20:
            health_n -= 20
        else:
            health_n = 0
        if weapon_n >= 20:
            weapon_n -= 20
        else:
            weapon_n = 0
        print('')
        print('Ваши ресурсы в убытке...')
        time.sleep(5)
        print('')
        pr_2 = input('Введите "1", если хотите потратить 30 "монет" чтобы добавить +10 "оружия": ')
        if pr_2 == '1':
            if money_n >= 30:
                money_n -= 30
                weapon_n += 10
            else:
                print('Кажется, у вас не хватает монет!')
        else:
            print('Играем дальше!')
        pr_3 = input('Введите "1" чтобы узнать свои текущие параметры: ')
        if pr_3 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Играем дальше!')
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

    input('Мирные жители, вы готовы начать игру? ')
    print('')
    time.sleep(3)
    print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
    time.sleep(2)
    print('')
    print('Кажется, Ангелы в опасности! Посол рассказал вас о планах демонов напасть на их лагерь на рассвете! ')
    print('Нужно срочно начать собирать отряд, чтобы успеть выдвинутся до темноты. ')
    time.sleep(5)
    print('')
    print('Изменения ваших параметров:зд оровье - 20')
    print('Изменение параметров Ангелов: здоровье - 20')
    time.sleep(3)
    print('')
    print('Да, вы возьмете часть удара на себя, но необходимо поддержать друзей в борьбе против одного противника! Или... нет?')
    print('Кажется, ваши показатели здоровья тоже не очень велеки. Вам бы спокойно залечить раны, чтобы быть готовыми дать ')
    print('достоинный отпор в следующий раз. В конце концов, Ангелы и сами смогут защитить поселение, разве что с большими ')
    print('потерями. Может, отправите посла с отказом?')
    time.sleep(9)
    print('')
    print('Изменения ваших параметров: здоровье + 10')
    print('Изменение параметров Ангелов: здоровье - 30')
    time.sleep(3)
    print('')
    print('Каким путём вы последуете в этот раз?')
    time.sleep(1)
    ans_1 = int(input('Введите "1",если хотите помочь ангелам; '
                      'Введите "2",если хотите отказать в помощи: '))
    if ans_1 == 1:
        if v_health >= 20:
            if health_n >= 20:
                v_health -= 20
                health_n -= 20
            else:
                v_health -= 20
                health_n = 0
        else:
            print('Похоже, у вас недостаточно ресурсов для этого выбора... В этот раз Ангелам придётся сражатся одним')

    elif ans_1 == 2:
        v_health += 10
        if health_n >= 30:
            health_n -= 30
        else:
            health_n = 0
    print('')
    print('Выбор сделан! ')
    print('')
    time.sleep(2)

    if health_n == 0:
        print('Ангелы проиграли!')
    elif v_health == 0:
        print('Местные жители проиграли!')

    print('Вам вновь предстоит сделать сложный выбор, Нефилимы!')
    time.sleep(5)
    print('')
    print('Аид, предводитель Демонов, отдал приказ немедленно нападать на деревню мирных жителей...'
          , '\n', '1) Вы организовали отряд Нефилимов, чтобы предотвратить жестокое нападение.')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -20', '\n', '"Оружие": -20')
    print('Как меняются параметры противника:', '\n', '"Здоровье": -40', '\n', '"Зелье": -10')
    time.sleep(5)
    print('')
    print('2) Вы решили помочь Мирным Жителям укрепить их убежища, чтобы Демоны не смогли разгромить их постройки.')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -10', '\n', '"Монеты": -30')
    print('Как меняются параметры Мирных жителей:', '\n', '"Монеты": +20', '\n', '"Убежище": +30')
    time.sleep(5)
    print('')
    sl_2 = input('Если хотите выбрать 1-й исход, то введите "1". Если хотите выбрать 2-й исход, то введите "2": ')
    if sl_2 == '1':
        if health_n >= 20 and weapon_n >= 20:
            health_n -= 20
            weapon_n -= 20
            health_d -= 40
            potion -= 10
        else:
            print('Кажется, у вас недостаточно ресурсов!')
    elif sl_2 == '2':
        if health_n >= 10 and money_n >= 30:
            health_n -= 10
            money_n -= 30
            v_money += 20
            v_shelter += 30
        else:
            print('Кажется, у вас недостаточно ресурсов!')
    print('')
    print('Выбор сделан!')
    time.sleep(5)
    print('')
    stt_2 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if stt_2 == '1':
        print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        print('')
    else:
        print('Играем дальше!')
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
    ch4 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch4 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
        print('')


    input('Мирные жители, ваш час настал. Готовы продолжить игру?: ')
    print('Время не ждёт! Скрестите пальцы.')
    time.sleep(3)
    rand_event1_d = random.randint(1, 2)
    if rand_event1_d == 1:
        print('Отличый улов! Кажется, этой рыбы хватит не только на пропитание, но и на продажу. ВЫ получили +20 "монет".')
        v_money += 20
    else:
        print('Какая неудача... Это стихия! Цунами! Око смерча! Ваше "убежище" уменьшилось на 30, "здоровье" на 20')
        if v_shelter >= 30:
            v_shelter -= 30
            if v_health >= 20:
                v_health -= 20
            else:
                v_health == 0
        else:
            v_shelter == 0
        print('Кажется, у вас появилась проблема...')
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
            ans_8 = input('Введите "1", если хотите потратить 20 "монеты" чтобы добавить +10 "здоровья": ')
            print('')
            if ans_8 == 1:
                if v_money >= 20:
                    v_money -= 20
                    v_health += 10
                else:
                    print('Кажется, у вас недостаточно монет... Что же, попробуете в следующий раз')
            else:
                print('Похоже, выы уверены в своих силах! Так держать!')
                print('')

    if v_health == 0:
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

    print('Нефилимы, зло все ближе и ближе! Нужно стоять на страже порядка. Вы готовы?')
    print('')
    print('Что же послали вам Высшие Силы на этот раз? Приготовьтесь...')
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print('Вы удостоились чести пройти ритуал нанесения рун! Руны придают вам силы во время сражений. '
              'Вы получили +20 "здоровья"!')
        health_n += 20
        print('')
        pr_4 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if pr_4 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Ваши дела идут в гору!')
    else:
        print(
            'Опять эти орки! Устроили пожар в вашей оружейной. Вы потеряли много оружия... "Оружие" уменьшилось на 50')
        if weapon_n >= 50:
            weapon_n -= 50
        else:
            weapon_n = 0
        print('')
        print('Не переживайте, за каждой черной полосой следует белая.')
        time.sleep(5)
        print('')
        pr_5 = input('Введите "1", если хотите потратить 30 "Монет", чтобы приобрести +30 "Оружия": ')
        if pr_5 == '1':
            if money_n >= 30:
                money_n -= 30
                weapon_n += 30
            else:
                print('Кажется, у вас не хватает монет!')
        else:
            print('Играем дальше!')
        pr_6 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
        if pr_6 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Играем дальше!')
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


    input('Мирные жители, вы готовы продолжить игру? ')
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
            print('Похоже, у вас недостаточно ресурсов для этого выбора... И всё же, вы должны помочь Ангелам, даже если лишь матриально!')
            if v_money >= 20:
                v_money -= 20
                money_n += 20
                health_n += 10
            else:
                money_n += v_money
                v_money == 0
                health_n += 10

    elif ans_14 == 2:
        if v_money >= 20:
            v_money -= 20
            money_n += 20
            health_n += 10
        else:
            money_n += v_money
            v_money == 0
            health_n += 10
    print('')
    print('Выбор сделан! ')
    print('')
    time.sleep(2)

    if v_health == 0:
        print('Местные жители проиграли!')

    ans_17 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_17 == 1:
        print('')
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
        print('')
    else:
        print('Отличная работа!')
    print('')

    print('Приготовьтесь! Вам предстоит сделать сложный выбор... Какой из двух путей лучший? Решать только вам.')
    time.sleep(5)
    print('')
    print(
        'Нефилимы, во время ночного патруля вы случайно рассекретили место шабаша ведьм. Какая наглость! Они устроили ритуал прямо посреди леса.',
        '\n',
        '1) Нападать во время ритуала очень рискованно... Ведь они находятся на пике своих сил, потери могут быть слишком большие для вас.')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -30', '\n', '"Оружие": -30')
    print('Как меняются параметры противника:', '\n', '"Здоровье": -10', '\n', '"Зелье": -30')
    time.sleep(5)
    print('')
    print(
        '2) Кажется, поселение Мирных жителей находится недалеко от проведения шабаша... Надо предупредить поселян не выходить ночью из убежища! '
        'Иначе может случиться что-то непоправимое.')
    time.sleep(5)
    print('')
    print('Как меняются ваши параметры:', '\n', '"Здоровье": -15')
    print('Как меняются параметры Мирных жителей:', '\n', '"Здоровье": +20', '\n', '"Убежище": +10')
    time.sleep(5)
    print('')
    sl_3 = input('Если хотите выбрать 1-й исход, то введите "1". Если хотите выбрать 2-й исход, то введите "2": ')
    if sl_3 == '1':
        if health_n >= 30 and weapon_n >= 30:
            health_n -= 30
            weapon_n -= 30
            health_d -= 10
            potion -= 30
        else:
            print('Кажется, у вас недостаточно ресурсов!')
    elif sl_3 == '2':
        if health_n >= 15:
            health_n -= 15
            v_money += 20
            v_shelter += 10
        else:
            print('Кажется, у вас недостаточно ресурсов!')
    print('')
    print('Выбор сделан!')
    print('')
    stt_3 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if stt_3 == '1':
        print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        print('')
    else:
        print('Играем дальше!')
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
    ch7 = input('Введите "1", чтобы узнать свои текущие параметры: ')
    if ch7 == '1':
        print('Итого:', '\n', 'Здоровье:', health_d, '\n', 'Монеты:', money_d, '\n', 'Зелье:', potion)
        print('')
    else:
        print('Продолжаем битву!')
        print('')


    input('Мирные жители, вы готовы попытать удачу? ')
    print('Время не ждёт! Скрестите пальцы!')
    time.sleep(1)
    rand_event1_d = random.randint(1, 2)
    if rand_event1_d == 1:
        print('Якорь мне в бухту! Вы нашли потерянное сокровище пиратов! Вы получили +20 "монет".')
        v_money += 20
        time.sleep(1)
        print('')
    else:
        print('Могло быть и хуже, но некуда. В вашем поселении эпидемия дизентерии, "здоровье" уменьшилось на 30')
        if v_health >= 30:
            v_health -= 30
        else:
            v_health == 0
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

    ans_13 = input('Нажмите "1" чтобы узнать свои текущие параметры: ')
    print('')
    if ans_13 == 1:
        print('Итого:', '\n', 'Здоровье:', v_health, '\n', 'Монеты:', v_money, '\n', 'Убежище:', v_shelter)
    else:
        print('Продолжим!')

    print('Превосходно играем, Нефилимы! Ангелы не зря поделились с вами своим даром. Продолжаем?')
    print('')
    print('Интересно, какое испытание на этот раз?')
    print('')
    rndm_event_1 = random.randint(1, 2)
    if rndm_event_1 == 1:
        print(
            'Как мы знаем, молитвы исцеляют наши души и приносят гармонию в жизнь. Утренние молитвы пошли Вам на пользу! Вы получили +15 "Здоровья".')
        health_n += 15
        print('')
        pr_7 = input('Введите "1", чтобы узнать свои текущие параметры: ')
        if pr_7 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Ваши дела идут в гору!')
    else:
        print(
            'Караул! Орки не дремлют... На этот раз они подстроили нападение на ваш отряд! Ваше "Здоровье" уменьшилось на 40, к сожалению, "Оружие" сократилось на 20')
        if weapon_n >= 20:
            weapon_n -= 20
        else:
            weapon_n = 0
        if health_n >= 40:
            health_n -= 40
        else:
            health_n = 0
        print('')
        print('Не падаем духом, впереди нас ждет величайшая битва!')
        time.sleep(5)
        print('')
        pr_8 = input('Введите "1", если хотите потратить 30 "монет", чтобы приобрести +20 "здоровья": ')
        if pr_8 == '1':
            if money_n >= 30:
                money_n -= 30
                health_n += 20
            else:
                print('Кажется, у вас не хватает монет!')
        else:
            print('Играем дальше!')
        pr_9 = input('Введите "1" чтобы узнать свои текущие параметры: ')
        if pr_9 == '1':
            print('Итого:', '\n', 'Здоровье:', health_n, '\n', 'Монеты:', money_n, '\n', 'Оружие:', weapon_n)
        else:
            print('Играем дальше!')

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

