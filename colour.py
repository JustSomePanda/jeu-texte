# Copiez ces 2 lignes pour l'utiliser dans votre programme.
import os
os.system('color')

print('Défaut')
print(f'0: \033[0mremet tout au défaut.')

print('\nSoulignement')
print(f'4: \033[4mSouligné  \033[24m')

print('\nCouleurs')
# Voir les colonnes « FG Code », « BG Code » et « Windows 10 Console Powershell 6 »:
#     https://i.stack.imgur.com/9UVnC.png
print(f'49: \033[49mremet la couleur de l\'arrière plan au défaut')
print(f'39: \033[39mremet la couleur du texte au défaut')
print(f'27: \033[27marrête l\'invertissement de couleurs')
print(f'7: \033[7mInvertit  \033[27m (échange la couleur du texte et de l\'arrière plan)')

print('\nCouleurs de base')
for i in range(30, 38):
    print(f'{i}: \033[{i}mCouleur  \033[39m', end=' ')
print()
for i in range(90, 98):
    print(f'{i}: \033[{i}mCouleur  \033[39m', end=' ')
print()
for i in range(40, 48):
    print(f'{i}: \033[{i}mCouleur  \033[49m', end=' ')
print()
for i in range(100, 107):
    print(f'{i}: \033[{i}mCouleur  \033[49m', end=' ')
print()

print('\n256 Couleurs (format: 38;5;...)')
for i in range(0, 256):
    print(f'\033[38;5;{i}m{i:3}\033[39m', end=' ')
    if i % 16 == 15:
        print()

print('\n256 Couleurs (format: 48;5;...)')
for i in range(0, 256):
    print(f'\033[48;5;{i}m{i:3}\033[49m', end=' ')
    if i % 16 == 15:
        print()

print('\n16 777 216 couleurs (format: 38;2;rouge;vert;bleu)')
print(f'38;2;0;0;0: \033[38;2;0;0;0mCouleur  \033[39m')
print(f'38;2;191;63;255: \033[38;2;191;63;255mCouleur  \033[39m')
print(f'38;2;255;255;255: \033[38;2;255;255;255mCouleur  \033[39m')

print('\n16 777 216 couleurs (format: 48;2;rouge;vert;bleu)')
print(f'48;2;0;0;0: \033[48;2;0;0;0mCouleur  \033[49m')
print(f'48;2;191;63;255: \033[48;2;191;63;255mCouleur  \033[49m')
print(f'48;2;255;255;255: \033[48;2;255;255;255mCouleur  \033[49m')

print('\nCombinaison (avec ; entre les items)')
print(f'38;4;255;164;197;48;2;155;106;0;4: \033[38;4;255;164;197;48;2;155;106;0;1;4mCombinaison  \033[0m')
print('    38;4;255;164;197 jaune')
print('    48;2;155;106;0 brun')
print('    4 souligné')
