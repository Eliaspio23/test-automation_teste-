# Test Automation Suite

Projeto de automação de testes cobrindo API REST (Petstore) e interface Web (SauceDemo), com pipeline de CI integrada via GitHub Actions.

---

## 🗂 Estrutura do Projeto

```
test-automation/
├── .github/
│   └── workflows/
│       ├── api-tests.yml        # Pipeline para testes de API
│       └── web-tests.yml        # Pipeline para testes Web
├── api-tests/
│   ├── conftest.py              # Fixtures globais (session, base_url)
│   ├── requirements.txt
│   └── tests/
│       ├── test_pet.py          # Endpoints /pet
│       ├── test_store.py        # Endpoints /store
│       └── test_user.py         # Endpoints /user
├── web-tests/
│   ├── conftest.py              # Fixture do WebDriver (Chrome headless)
│   ├── pytest.ini
│   ├── requirements.txt
│   ├── pages/                   # Page Objects
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── products_page.py
│   │   ├── cart_page.py
│   │   └── checkout_page.py
│   └── tests/
│       └── test_e2e_purchase.py # Fluxo E2E completo
└── README.md
```

---

## 🔧 Tecnologias Utilizadas

| Camada | Tecnologia |
|--------|-----------|
| Linguagem | Python 3.11 |
| Runner de testes | pytest |
| Automação Web | Selenium 4 + WebDriver Manager |
| Testes de API | requests |
| Relatórios | pytest-html |
| CI/CD | GitHub Actions |

---

## ⚙️ Pré-requisitos

- Python 3.11+
- Google Chrome instalado (para testes locais)
- pip

---

## 🚀 Instalação e Execução Local

### Testes de API

```bash
cd api-tests
pip install -r requirements.txt
pytest tests/ -v
```

### Testes Web

```bash
cd web-tests
pip install -r requirements.txt
pytest -v
```

### Gerando relatório HTML

```bash
# API
pytest api-tests/tests/ --html=reports/api-report.html --self-contained-html -v

# Web
cd web-tests && pytest --html=../reports/web-report.html --self-contained-html -v
```

---

## 🧪 Cenários Cobertos

### API — Petstore (`https://petstore.swagger.io/v2`)

| Arquivo | Cenário |
|---------|---------|
| `test_pet.py` | Criar pet, buscar por ID, buscar por status, atualizar, deletar, validar 404 após deleção |
| `test_store.py` | Consultar inventário, criar pedido, buscar pedido, deletar, validar 404 após deleção |
| `test_user.py` | Criar usuário, login, buscar usuário, atualizar, logout, deletar, validar 404 após deleção |

### Web — SauceDemo (`https://www.saucedemo.com`)

| Cenário | Descrição |
|---------|-----------|
| Login válido | Autentica com `standard_user` e valida redirecionamento para produtos |
| Login inválido | Valida mensagem de erro com credenciais incorretas |
| Adicionar ao carrinho | Adiciona 2 produtos e verifica badge do carrinho |
| Fluxo E2E completo | Login → carrinho → checkout → confirmação de pedido |

---

## 🔄 Pipeline CI/CD

As pipelines são disparadas automaticamente a cada `push` ou `pull_request` nos diretórios correspondentes.

- **`api-tests.yml`**: instala dependências Python, executa pytest e publica relatório HTML como artefato.
- **`web-tests.yml`**: instala Chrome via `browser-actions/setup-chrome`, executa pytest em modo headless e publica relatório HTML.

---

## 🏗 Design Patterns

- **Page Object Model (POM)**: cada página da interface web possui sua própria classe, isolando seletores e ações.
- **BasePage**: classe base com métodos reutilizáveis de espera explícita (`WebDriverWait`), herdada por todas as páginas.
- **Fixtures com escopos**: `scope="session"` no driver e na session HTTP evita recriação desnecessária entre testes.

---

## 📸 Screenshots

> Adicione prints das execuções locais e da pipeline na pasta `docs/screenshots/`.

Sugestão de capturas:
- Terminal com resultado do `pytest` (API e Web)
- Aba "Actions" do GitHub com pipeline verde
- Relatório HTML gerado pelo pytest-html

---

## 🔑 Credenciais de Teste (SauceDemo)

| Usuário | Senha |
|---------|-------|
| `standard_user` | `secret_sauce` |
