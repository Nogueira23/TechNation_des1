def modulo(d):
    if d > 0:
        d = d
    else:
        d = -d
    return d


def custoPalindromo(string):
    lista = list(string)
    lista_c = lista[::-1]
    string_c = ''.join(lista_c)
    custo = 0
    alpha_e = ["#", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m"]
    alpha_d = ["#", "z", "y", "x", "w", "v", "u", "t", "s", "r", "q", "p", "o", "n"]
    #quando a palavra já é palíndromo
    if string_c == string or string_c == '':
        custo += 0
        return custo
    #transformar a palavra em palíndromo
    else:
        for i in range(len(lista_c)):
            if lista_c[i] != lista_c[-i-1]:
                if lista_c[i] in alpha_e:
                    pos1 = int(alpha_e.index(lista_c[i]))
                    if lista_c[-i-1] in alpha_e:
                        pos2 = int(alpha_e.index(lista_c[-i-1]))
                        lista_c[i] = alpha_e[pos2]
                        d = pos1 - pos2
                        d = modulo(d)
                        custo += d
                    else:
                        pos2 = int(alpha_d.index(lista_c[-i-1]))
                        lista_c[i] = alpha_d[pos2]
                        if 1 <= pos1 <= 6:
                            if 1 <= pos2 <= 6:
                                d = pos1 + pos2 
                                d = modulo(d) - 1
                                custo += d
                            else:
                                d = pos1 + pos2 
                                d = modulo(d) - 1
                                custo += d
                        else:
                            if 1 <= pos2 <= 6:
                                d = pos1 + pos2 
                                d = modulo(d) - 1
                                custo += d
                            else:
                                d = (pos2 - pos1)
                                d = modulo(d) + 1
                                custo += d
                    string_c = ''.join(lista_c)
                    lista_c_ = lista_c[::-1]
                    string_c_ = ''.join(lista_c_)
                    if string_c_ == string_c:
                        return custo
                elif lista_c[i] in alpha_d:
                    pos1 = int(alpha_d.index(lista_c[i]))
                    if lista[i] in alpha_d:
                        pos2 = int(alpha_d.index(lista[i]))
                        lista_c[i] = alpha_d[pos2]
                        d = pos1 - pos2
                        d = modulo(d)
                        custo += d
                    else:
                        pos2 = int(alpha_e.index(lista[i]))
                        lista_c[i] = alpha_e[pos2]
                        if 1 <= pos1 <= 6:
                            if 1 <= pos2 <= 6:
                                d = pos1 + pos2
                                d = modulo(d) - 1
                                custo += d
                            else:
                                d = pos1 + pos2 
                                d = modulo(d) - 1
                                custo += d
                        else:
                            if 1 <= pos2 <= 6:
                                d = (len(alpha_e) - pos1) + (len(alpha_d) - pos2)
                                d = modulo(d) - 1
                                custo += d
                            else:
                                d = (len(alpha_e) - pos1) + (len(alpha_d) - pos2)
                                d = modulo(d) - 1
                                custo += d
                    string_c = ''.join(lista_c)
                    lista_c_ = lista_c[::-1]
                    string_c_ = ''.join(lista_c_)
                    if string_c_ == string_c:
                        return custo


string = input("Digite uma palavra: ")
print(custoPalindromo(string))