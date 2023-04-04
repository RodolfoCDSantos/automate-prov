# Automatizar processo importar e configurar provisionamento nos ramais.

## Tarefas

- [ ] Criar tabela de cliente 
- [ ] Importar imagem
- [ ] Identificar serial e MAC da imagem
- [ ] Registrar dados.
- [ ] Importar lista de imagens (O numero do ramal deve ser informado)
- [ ] Importar .zip com o nome da conta no titulo e imagens renomeadas com o numero do ramal.
- [ ] Listar images e seus dados para validar.
- [ ] Identificar se teve sucesso ou não.
- [ ] Fazer chamada no servidor para criar provi.
- [ ] Retornar resultado (exibir o ZTP on ou off).

---

## Requisitos:
### Linux
- unzip
- python3
- zbar
- python-poetry

### Backend
- python = "^3.10"
- pyzbar = "^0.1.9"
- opencv-python = "^4.7.0.72"
- typer = "^0.7.0"
- rich = "^13.3.3"

### Frontend
- streamlit = "^1.20.0"
- fastapi = "^0.95.0"
- uvicorn = "^0.21.1"

## Clonando projeto.

```
git clone 'sasdsd'
```

## Instalando depencias do linux.

Archlinux
```bash
sudo pacman -S unzip python3 zbar python-poetry
```

Ubuntu
```bash
sudo apt-get install unzip python3 zbar python-poetry
```

Fedora
```bash
sudo dnf install unzip python3 zbar python-poetry
```

## Instalando depencias do backend.

Poetry
```bash
poetry add pyproject.toml
```

---

## Obter Serial e Mac a partir de um banco de imagens em zip.
### CLI:

```bash
    poetry run python3 ./automate_prov/backend/server/scan_image.py --help
```

Você deve informar um nome e o caminho para o arquivo Zip, exemplo:

```bash
poetry run python3 ./automate_prov/backend/server/scan_image.py "teste1" ./ramais.zip
```

Você ter um retorno como esse.

```bash
Archive:  ./ramais.zip
  inflating: ./automate_prov/ramais/teste1/1001.jpeg
  inflating: ./automate_prov/ramais/teste1/1002.jpeg
  inflating: ./automate_prov/ramais/teste1/1003.jpeg

┏━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━┓
┃ Ramal ┃ Serial            ┃ MAC           ┃
┡━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━┩
│ 1002  │ 2123218122121067  │ 805EC04B642C  │
│ 1001  │ 2119418061408326  │ 805EC01E38F9  │
│ 1003  │ 4123217062104519  │ 001565E5A0F5  │
└───────┴───────────────────┴───────────────┘
```

O arquivo csv é salvo na pasta automate_prov/ramais/$name

