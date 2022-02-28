# DESAFIO 045
import emoji
import random
print(
    '                  \033[1;36;40m>>>>>>\033\033[7;0;40m JOKENPÔ \033[1;36;40m<<<<<<\033[m')
print('\033[1;30;40m-\033\033[1;35;40m+\033[m'*30)
print(emoji.emojize('\033[1;36;40m Escolha: \033[m \033[1;31;40m0. Pedra :fist:\033[m    \033[1;30;40m1. Papel :raised_hand_with_fingers_splayed:\033[m     \033[1;37;40m2. Tesoura :v:\033[m', use_aliases=True))

# 0 pedra        1 papel         2 tesoura
opcoes = ['Pedra', 'Papel', 'Tesoura']
emojiOp = [':fist:', ':raised_hand_with_fingers_splayed:', ':v:']
comp = random.randint(0, 2)

op = int(input('\033[1;32;40m>\033[m '))

print(emoji.emojize('\033[1;32;40mVocê:{}\033[m\n     :vs:\n\033[1;31;40mComp:{}\033[m' .format(
    emojiOp[op], emojiOp[comp]), use_aliases=True))
if op == 0 and comp == 2 or op == 2 and comp == 1 or op == 1 and comp == 0:
    print(emoji.emojize(
        '\n\033[1;32;40mVocê venceu :tada::partying_face::white_check_mark:\033[m', use_aliases=True))
elif op == comp:
    print(emoji.emojize(
        '\n\033[1;30;40mEmpate :warning:\033[m', use_aliases=True))
else:
    print(emoji.emojize(
        '\n\033[1;31;40mVocê perdeu :robot::x:\033[m', use_aliases=True))