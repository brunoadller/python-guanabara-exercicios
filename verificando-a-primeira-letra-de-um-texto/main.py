texto = str(input("Em que cidade você nasceu: ")).lower()
new_texto = texto.split()


def is_text():
    if new_texto[0] != 'santo':
        return False
    else:
        return True
    
    
print(is_text())