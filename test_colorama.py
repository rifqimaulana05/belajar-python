from colorama import Fore, Back, Style, init

init(autoreset=True)

print(Fore.RED + "Ini teks merah!")
print(Fore.GREEN + "Ini teks hijau!")
print(Fore.BLUE + "Ini teks biru!")
print(Fore.YELLOW + "Ini teks kuning!")
print(Fore.RED + "Ini teks biru!")

print(Back.YELLOW + Fore.BLACK + "Ini teks dengan latar kuning!")
print(Style.BRIGHT + Fore.MAGENTA + "Ini teks tebal dan ungu cerah!")

print(Back.BLACK + "Latar Hitam")
print(Back.RED + "Latar Merah")
print(Back.GREEN + "Latar Hijau")
print(Back.YELLOW + "Latar Kuning")
print(Back.BLUE + "Latar Biru")
print(Back.MAGENTA + "Latar Ungu")
print(Back.CYAN + "Latar Cyan")
print(Back.WHITE + "Latar Putih")

