# Projeto

![logo](https://user-images.githubusercontent.com/65972745/209705812-b707ba23-4464-4720-bf95-496bf981f2a1.png)

DCO - Detectar e contar objetos

## Descrição

Este projeto faz parte de um teste para determinar conhecimento em IA usando visão computacional

### FrameWorks

Python 3.10.6,  Numpy, opencv 4.5.4 or opencv-python-headless 4.6.0.66, visual Code, ubuntu 22 

### Objetivo
Com as imagens selecionadas exibir as seguintes informações:  
   * 1. O número de marcações na primeira linha
   * 2. O número de marcações na primeira coluna
   * 3. O número de marcações na imagem

![card](https://user-images.githubusercontent.com/65972745/209705872-fda0ff08-89ad-47ea-82e7-1fcb2c4c3e5e.png)

### Instalação

* Import vc2
* Import numpy as np

### Executando o programa

* Primeiro passo => Selecionar a imagem
"img = cv2.imread("card01.bmp",(0))"

* Para rodar o programa
"Python3 img_analiz.py

## Resultados

* O processamento do código vai retorna a quantidade de objetos dentro de uma imagem por binarização, 
* Duas área da imagem foram slecionadas atraves de ROI, onde o código vai proceder da mesma ambiguidade e fazer 
    o processamento exibindo a quantidade de objetos em cada seleção. 
## Autor

Juliano Aragão

https://github.com/Juliano-Aragao

## Versionamento 

* 0.1

## Licensa 

Este projeto está licenciado sob a licença do autor - consulte o arquivo LICENSE.md para obter detalhes

## Acknowledgments

Inspiration, code snippets, etc.
* [Livro] Introdução a Visão Computacional - Felipe Bareli
* [Documentação_OpenCv]https://docs.opencv.org/4.x/d9/d8b/tutorial_py_contours_hierarchy.html
* [I_Love_Python]https://www.youtube.com/watch?v=uVct6QT-mJU
