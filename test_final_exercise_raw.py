"""
Disciplina: Automação de testes
Aluno: Luis Roberto Lange
Data: 25/11/2024

Código verificado com:
_ pycodestyle (antigo pep8)
    Ok

_ pylint
    ************* Module test_final_exercise_raw
    test_final_exercise_raw.py:23:8: W0201: Attribute 'driver' defined outside __init__ (attribute-defined-outside-init)
    test_final_exercise_raw.py:24:8: W0201: Attribute 'vars' defined outside __init__ (attribute-defined-outside-init)

    ------------------------------------------------------------------
    Your code has been rated at 9.72/10 (previous run: 9.72/10, +0.00)
"""
import re
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDemo():
    """Definições da classe de teste"""

    def setup_method(self, _method):
        """
        Inicializa o WebDriver
        """
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, _method):
        """
        Encerra o WebDriver
        """
        if self.driver:
            self.driver.quit()

    def preenche_campos(self, id_campo, texto):
        """
        Limpa o campo de entrada e preenche com o valor informado
        """
        campo = self.driver.find_element(By.ID, id_campo)
        campo.clear()  # Limpa o campo de entrada
        campo.send_keys(texto)  # Preenche com o novo valor

    def clica_botao(self, xpath_botao):
        """
        Clica no botão informado
        """
        self.driver.find_element(By.XPATH, xpath_botao).click()

    def valida_texto_retorno(self, seletor, *expected_texts):
        """
        Valida o(s) texto(s) do retorno e retorna o id (se existir)
        """
        texto_retornado = self.driver.find_element(
            By.XPATH, seletor
        ).text

        # Valida se o texto esperado está presente
        for text in expected_texts:
            assert text in texto_retornado, (
                f"Expected '{text}' in '{texto_retornado}'"
            )

        # Expressão regular para capturar o número após "id:"
        match = re.search(r"id:\s*(\d+)", texto_retornado)
        if match:
            course_id = int(match.group(1))  # Converte o ID para inteiro
            return course_id  # Retorna o ID encontrado
        return None

    def test_demo(self):
        """
        ======================================================================
        Início do teste
        ======================================================================
        """
        duracao_sleep = 3
        self.driver.get("https://tdd-detroid.onrender.com/")

        self.driver.maximize_window()

        # Aguarda carregar o python da página
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".smooth")
        while len(elements) > 0:
            elements = self.driver.find_elements(By.CSS_SELECTOR, ".smooth")
            sleep(duracao_sleep)

        # Cadastra o estudante
        estudante = "Luis"
        self.preenche_campos("student-nome", estudante)
        self.clica_botao("//button[contains(@id,'student-btn')]")
        id_estudante = self.valida_texto_retorno(
            "//div[@id='local-terminal']",
            "Added student",
            f"Name: {estudante}"
        )
        print(f"O id do estudante é: {id_estudante}")
        sleep(duracao_sleep)  # Pausa de 2 segundos após o cadastro

        # Cadastra os cursos e armazena em vetores
        cursos = [
            "Pós em testes de software",
            "Graduação em TI",
            "MBA em Qualidade de Software"
        ]
        ids_cursos = []

        for curso in cursos:
            self.preenche_campos("course-nome", curso)
            self.clica_botao(
                "//button[@class='py-button']"
                "[contains(.,'Add course')]"
            )
            id_curso = self.valida_texto_retorno(
                "//div[@id='local-terminal']",
                "Added course",
                f"Nome: {curso}"
            )
            ids_cursos.append(id_curso)
            sleep(duracao_sleep)  # Pausa de 2 segundos entre cada cadastro
            # print(f"O id do curso '{curso}' é: {id_curso}")

        print("Cursos cadastrados:")
        for curso, id_curso in zip(cursos, ids_cursos):
            print(f"Curso: {curso}, ID: {id_curso}")

        self.preenche_campos("student-id", id_estudante)
        self.preenche_campos("course-id", "1")
        self.clica_botao(
            "//button[contains(text(),'Subscribe student in course')]"
        )
        sleep(duracao_sleep)
        self.valida_texto_retorno(
            "//div[@id='local-terminal']",
            f"Student id {id_estudante} subscribed to course id 1"
        )

        # Cadastra os cursos e armazena em vetores
        disciplinas = [
            "Automação de Testes",
            "Testes Mobile",
            "ISTQB"
        ]

        ids_disciplinas = []

        for disciplina in disciplinas:
            self.preenche_campos("discipline-nome", disciplina)
            self.preenche_campos("course-discipline-id", "1")

            self.clica_botao(
                "//button[@class='py-button']"
                "[contains(.,'Add discipline')]"
            )
            ids_disciplina = self.valida_texto_retorno(
                "//div[@id='local-terminal']",
                "Added discipline",
                f"Name: {disciplina}"
            )
            ids_disciplinas.append(ids_disciplina)
            sleep(duracao_sleep)  # Pausa de 2 segundos entre cada cadastro

        for num_atual in ids_disciplinas:
            self.preenche_campos("subscribe-student-id", id_estudante)
            self.preenche_campos("subscribe-discipline-id", num_atual)
            self.clica_botao(
                "//button[@class='py-button']"
                "[contains(.,'Subscribe discipline')]"
            )
            if num_atual != 3:
                self.valida_texto_retorno(
                    "//div[@id='local-terminal']/pre[2]",
                    "Student id ",
                    f"Name {estudante}",
                    "subscribed to discipline ",
                    f"id {id_estudante}"
                )
            else:
                self.valida_texto_retorno(
                    "//div[@id='local-terminal']",
                    "Student id ",
                    f"Name {estudante}",
                    "subscribed to discipline ",
                    f"id {id_estudante}"
                )

            sleep(duracao_sleep)  # Pausa de 2 segundos entre cada cadastro
