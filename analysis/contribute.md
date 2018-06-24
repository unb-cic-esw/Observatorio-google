# Contribuições
Para adicionar a este módulo pode ser escolhido o arquivo
*data_frame_op.py* ou *text_analyzer.py*.

## Contribuições aos Data Frames
Primeiramente, para se ter uma melhor consciência da interface utilizada 
confira o arquivo *test_data_frames.py* na pasta *tests* deste módulo.  
Caso seja desejada uma adição a este módulo, comece aumentando os dados
atribuidos ao *data frame*. Os *Json's* disponíveis no banco de dados do 
projeto contém informações que não foram utilizadas mas o podem. Por 
exemplo o dado que corresponde se um link é anúncio ou não, que é de 
grande relevância para o processamento.

## Contribuições ao processamento textual
Primeiramente, para se ter uma melhor consciência da interface utilizada 
confira o arquivo *test_analyzer.py*.  
Seria de grande importância ao módulo uma adição de outro algoritmo que 
não *tf-idf*. De preferência, um que esteja adaptado a textos menores, uma 
vez que mesmo que os *preview's* sejam a seção que mais contém palavras, 
elas ainda são muito escassas para uma relevância alta do *tf-idf*.