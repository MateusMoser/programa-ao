def notas(*n,mostrar=False):
    tot = sum(n)
    dic = {'quantidade':len(n),'menor':min(n),'maior':max(n),'media':tot/len(n),'sit':'nao informado'}
    if dic['media'] > 7:
        dic['sit']= 'bom'
    elif dic ['media'] > 5:
        dic['sit']='ruim'
    else:
        dic['sit'] = 'horrivel'
    if mostrar == False:
        del dic['sit']
    return dic


resp = notas(6,3,9,mostrar=False)
print(resp)


