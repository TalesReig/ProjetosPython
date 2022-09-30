import re;
import unidecode;

with open('teste.txt',"r", encoding="utf_8") as arquivoTeste:
    comentarios = arquivoTeste.read().lower();
    comentarios = unidecode.unidecode(comentarios)

def comentariosPositivos(comentarios):
    totpositivos = 0;

    x = re.findall(r"melhor filme",comentarios)
    totpositivos = totpositivos+x.__len__();

    # x = re.findall(r"muito bom",comentarios)
    # totpositivos = totpositivos+x.__len__();;

    # x = re.findall(r"curti muito",comentarios)
    # totpositivos = totpositivos+x.__len__();;

    # x = re.findall(r"muito interessante",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r"ótimos atores",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r"ótima trilhasonona",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r"obra prima ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r" vale a pena ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r" sensacional ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r" impecável ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r" perfeito ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    # x = re.findall(r" história prende ",comentarios)
    # totpositivos = totpositivos+x.__len__();

    return totpositivos;

def comentariosNegativos(comentarios):
    totNegativos = 0;

    x = re.findall(r"pior(s)? (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r"pessim(o|a)(s)? (filme|trilha sonora|atuac|atuaç|roteiro|trama|direc|direç|fotografia|musica|arte|cg)",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" não percam tempo ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" muito ruim ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" dormi ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" filme chato ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" sem graça ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" muito fraco ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" não recomendo ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" chato ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" maçante ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" cansativo ",comentarios)
    totNegativos = totNegativos + x.__len__();

    x = re.findall(r" sem sentido ",comentarios)
    totNegativos = totNegativos + x.__len__();

    return totNegativos;

def filtrarComentarios(comentarios):    

    totPositivos = comentariosPositivos(comentarios);

    totNegativos = comentariosNegativos(comentarios);

    cacularEstrelas();

# def cacularEstrelas(int positivos, int negativos):
#     pontos = 50;

#     valorDeCadaCriticaOuElogio = 50/positivos;

#     pontos = positivos*valorDeCadaCriticaOuElogio + negativos*valorDeCadaCriticaOuElogio;

#     estrelas = pontos/100;

#     return("O filme foi classificado como",pontos*estrelas,"estrelas");

filtrarComentarios(comentarios);