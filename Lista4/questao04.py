'''
Seja o statement sobre diversidade: “The Python Software Foundation and the global Python community  welcome  and  encourage  participation  by  everyone.  Our  community  is  based  on mutual respect, tolerance, and encouragement, and we are working to help each other live up to  these  principles.  We  want  our  community  to  be  more  diverse:  whoever  you  are,  and whatever  your  background,  we  welcome  you.”. Gere  uma  lista  de  palavras  deste  texto  com split(), a seguir crie uma lista com as palavras que começam ou terminam comuma das letras “python”.Imprima a lista resultante.Não se esqueça deremover antes os caracteres especiais e cuidado com maiúsculas e minúsculas.
'''
import re
str = 'The Python Software Foundation and the global Python community  welcome  and  encourage  participation  by  everyone.  Our  community  is  based  on mutual respect, tolerance, and encouragement, and we are working to help each other live up to  these  principles.  We  want  our  community  to  be  more  diverse:  whoever  you  are,  and whatever  your  background,  we  welcome  you.'
strFilter = re.sub(r'[^\w]', " ", str)
arrStr = strFilter.lower().split()
arrFilter = []
for i in (arrStr):
    for j in ('python'):
        if i.startswith(j) or i.endswith(j):
            arrFilter.append(i)
print(arrFilter)
