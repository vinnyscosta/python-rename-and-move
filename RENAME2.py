
import os
import shutil

diretorio = 'D:\\python-rename\\files'
destino = 'D:\\python-rename\\renamed'

for root, dirs, files in os.walk(diretorio, topdown=False):
    for name in files:
        caminho = os.path.join(root, name)
        #print(caminho)
        source_dir = caminho.split('\\',)[-2]
        pasta_renamed = destino+"\\"+source_dir+"-renamed"
        #print(pasta_renamed)
        file_name = caminho.split('\\',)[-1]
        file_renamed = "pattern_"+source_dir+"_"+file_name
        #print(file_renamed)
        if os.path.isdir(pasta_renamed):
            print("O diretório existe!")
        else:
            try:
                os.mkdir(pasta_renamed) 
            except:
                print("diretorio NÃO criado")
            else:
                print("diretorio criado")
        shutil.copy(caminho, pasta_renamed+"\\"+file_renamed)
        print('renamed:', file_renamed)
        #print(caminho.split('\\',)[-2])
        #print(caminho.split('\\',)[-1])
        #for name in dirs:
        #    print(os.path.join(root, name))
