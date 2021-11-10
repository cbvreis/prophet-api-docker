## 🔖 Sobre
Objetivo deste projeto era passar por todas as etapas de desenvolvimento de modelos de machine Learning. Foi desenvolvido desde a virtualização até o deploy do modelo via API.

</br>

<p align="center"> 
  <img src="https://miro.medium.com/max/964/0*tVCene42rgUTNv9Q.png" alt="Página inicial" width="100%">
</p>

</br>

## 🚀 Bibliotecas utilizadas

- [Prophet](https://facebook.github.io/prophet/)

</br>


## 🗂 Estrutura do projeto

```
prophet-api-docker
│   README.md
│   main.py    
│   Dockerfile  
│   requirements.txt    
│   saida.xlsx    
│
└───data
│   │   petr4.csv
│   
└───models
|    │   Prophet.py
|    │   model.pkl
│
│
└───notebooks
|    │   data-petr4.ipynb



 
```


## 🗂 Como baixar e iniciar o projeto

### Docker
Para construir a imagem deveremos instalar o docker e digitar o comando abaixo:
```bash
#docker build -f .\Dockerfile -t <tag_name> .
docker build -f .\Dockerfile -t ubuntu:my_version .
```

Agora, iremos rodar gerar o container  a partir da imagem acima através do comando:
```bash
docker run -it -v C:\docker_tutorial:/home/user -p 8888:8888 ubuntu:my_version bash
```
Substituir o caminho pelo Path utilizado.


### Jupyter notebook 
Após realizar os comandos acima, já estamos dentro do container. Agora pasta digitar:

```bash
jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root
```
Um novo notebook do jupyter poderá ser acessado através da URL pelo navegador:
(https://localhost:8888/)

### API
Para rodar a api, rodar comando abaixo:

```bash
python main.py
```

<br>

Desenvolvido por [Cássio Reis](https://www.linkedin.com/in/cassioreisdevelop/) 🤓


