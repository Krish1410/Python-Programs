
# colors={
#     "BLACK" : "\033[0;30m",
#     "RED" : "\033[0;31m",
#     "GREEN" : "\033[0;32m",
#     "BROWN" : "\033[0;33m",
#     "BLUE" : "\033[0;34m",
#     "PURPLE" : "\033[0;35m",
#     "CYAN" : "\033[0;36m",
#     "LIGHT_GRAY" : "\033[0;37m",
#     "DARK_GRAY" : "\033[1;30m",
#     "LIGHT_RED" : "\033[1;31m",
#     "LIGHT_GREEN" : "\033[1;32m",
#     "YELLOW" : "\033[1;33m",
#     "LIGHT_BLUE" : "\033[1;34m",
#     "LIGHT_PURPLE" : "\033[1;35m",
#     "LIGHT_CYAN" : "\033[1;36m",
#     "LIGHT_WHITE" : "\033[1;37m",
#     "BOLD" : "\033[1m",
#     "FAINT" : "\033[2m",
#     "ITALIC" : "\033[3m",
#     "UNDERLINE" : "\033[4m",
#     "BLINK" : "\033[5m",
#     "NEGATIVE" : "\033[7m",
#     "CROSSED" : "\033[9m",
#     "END" : "\033[0m"
# }
# print("\nFore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.")
# print("\nBack: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.")
# print("\nStyle: DIM, NORMAL, BRIGHT, RESET_ALL")
# import colorama
# from colorama import  Fore, Back, Style
# print(Fore.CYAN)
# print("Text will continue to be cyan")
# print("until it is reset or changed")
# print(Style.RESET_ALL)
# # Colorize a single line and then reset
# print(Fore.RED + 'You can colorize a single line.' + Style.RESET_ALL)

# # Colorize a single word in the output
# print('Or a single ' + Back.GREEN + 'words' + Style.RESET_ALL + ' can be highlighted')

# # Combine foreground and background color
# print(Fore.BLUE + Back.WHITE)
# print('Foreground, background, and styles can be combined')
# print("==========            ")

# print(Style.RESET_ALL)
# print('If unsure, reset everything back to normal.')
import colorama
from colorama import Fore, Back

colorama.init(autoreset=True)

# Automatically adds a Style.RESET_ALL after each print statement
print(f'{Fore.RED}Red foreground text')
print(f'{Back.RED}Red background text')
print("Some plain text")
