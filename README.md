# Instalação e execução do exemplo
- Crie um ambiente virtual (virtual environment) usando a sua versão padrão do Python
```
python3 -m venv venv
```
- Ative o ambiente virtual
```
venv\scripts\activate
```
- Instale os requisitos do projeto
```
pip install -r requirements.txt
```
- Execute o teste de exemplo. Garanta que o Chrome esteja inslado na sua máquina.
```
python -m pytest
```

# Referências
- [Selenium WebDriver Documentation](https://www.selenium.dev/documentation/webdriver/)


Regras importantes:
trabalho individual
trabalhos copiados não serão considerados
entregas após a data limite não serão considerados. Lembre-se que o professor precisa de tempo para corrigir os trabalhos com calma. Não deixe para a última hora!
Dica: se você não usa Linux, adiante-se para que o professor possa te ajudar na medida do possível, pois o professor só sabe Linux :)
Objetivo:
Faça o que se pede e organize o código no padrão de projeto page objects, screenplay ou gherkin. Aceito Keyword-Driven também.

Dica importante: caso tenha mais familiaridade com outro framework, por exemplo, Robotframework, Cypress, Playwrite... você pode usar ele para fazer a automação. Não se esqueça de mandar as instruções para execução do teste.

 

Entregáveis:
Vídeo contínuo exibindo a execução com sucesso do seu script
 Código fonte (em Python)
Instruções num arquivo README.md para execução do script pelo professor
 

Trabalho: Automação da aplicação Web College Manager (https://tdd-detroid.onrender.com/).
Com a aplicação acessível via browser, explore-a um pouco para se familiarizar com ela
Baixe este script base (https://pucminas.instructure.com/courses/195083/modules/items/4785351) e tente executá-lo usando pytest
Algumas partes do script vão falhar. Corrija-as antes de refatorar o código para um padrão de projeto.
O script
cria um aluno (student)
cria 3 cursos (courses);
inscreve o aluno no curso de id 1
adiciona 3 matérias (disciplines) no curso de id 1
inscreve o aluno nas matérias de id 1,2,3
Neste vídeo (https://drive.google.com/file/d/1tzXHQJe7U2v_vp5JSAjTpRKVIeKlcDk_/view?usp=sharing) é possível ter uma idéia de como a sua execução ficará ao final do trabalho
