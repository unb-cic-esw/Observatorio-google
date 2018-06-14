# Observatório Google

## Ferramentas

- Selenium com GeckoDriver
  - Download do GeckoDriver (Linux64)
      ```bash
        $ wget https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
        $ tar -xvzf geckodriver-v0.20.1-linux64.tar.gz
        $ rm geckodriver-v0.20.1-linux64.tar.gz
      ```

## Instalação

```bash
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

## Execução

- Testes
```bash
$ py.test
```

- Arquivo que coleta os resultados das pesquisas no google dos termos do arquivo "actors/actors.json" com os perfis do arquivo _profiles.json_, um profile com _"login" : ""_ não realiza o login.
```bash
$ export PATH=$PATH:diretório/onde/o/geckodriver/foi/extraido
$ export POST_URL=url que receberá os dados
$ python roda_pesquisas.py
```
