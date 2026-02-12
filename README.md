# Natural-Language-Processing-Suite

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-4.0%2B-blue?logo=r&logoColor=white)
![Top Language](https://img.shields.io/github/languages/top/galafis/Natural-Language-Processing-Suite)


![Natural Language Processing](assets/nlp_hero_image.jpg)


## English

### Overview
This **Natural Language Processing (NLP) Suite** is a multi-language project demonstrating text processing, data analysis, and interactive visualization. It combines Python, JavaScript, and R into a full-stack application with a Flask backend, a responsive web frontend, and R-based statistical analysis.

### Author
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Technologies Used
This project uses the following technologies:

-   **Backend**: Python (Flask)
-   **Frontend**: HTML5, CSS3, JavaScript (ES6+)
-   **Analytics**: R (ggplot2, dplyr, statistical modeling)
-   **Data Processing**: pandas, numpy
-   **Styling**: CSS Grid, Flexbox, responsive design
-   **Modern Web Features**: Async/await, Web APIs, ES6 classes
-   **Visualization**: Charts via R (ggplot2) and frontend interactivity

### Features

#### Core Functionality
-   **Text Processing**: API endpoint for text transformation and analysis.
-   **Analytics**: Data analysis and visualization via the web interface.
-   **Interactive Web Interface**: Responsive design for user interaction.
-   **Statistical Analysis**: R-based analytics and reporting tools.

#### Web Interface
-   **Modern UI/UX**: Semantic HTML5, accessible design, and professional styling.
-   **Responsive Design**: Optimized for various devices using CSS Grid and Flexbox.
-   **Dynamic Interactivity**: JavaScript ES6+ powers interactive elements and real-time updates.

#### Analytics & Reporting
-   **R Integration**: R script for statistical modeling and data visualization.
-   **Data Processing**: Tools for data loading, transformation, and analysis.
-   **Visualizations**: Generate charts using ggplot2 and correlation plots.

### Installation

To set up the Natural-Language-Processing-Suite locally, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/galafis/Natural-Language-Processing-Suite.git
cd Natural-Language-Processing-Suite

# 2. Python setup
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..

# 3. R setup (install required packages)
Rscript -e "install.packages(c('ggplot2', 'dplyr', 'corrplot'), repos='http://cran.us.r-project.org')"

# 4. Create data directory and sample data (if not present)
mkdir -p data
echo "text,category\nhello world,greeting\nNLP is great,technology" > data/data.csv
```

### Usage

#### Running the Application

1.  **Start the Python Backend**
    ```bash
    cd backend
    python app.py
    ```
    The application will run on `http://localhost:5000`.

2.  **Access the Web Interface**
    Navigate to `http://localhost:5000` in your web browser.
    The web interface is responsive across devices.

3.  **Run R Analytics**
    You can execute the R analytics script independently:
    ```r
    # Load R analytics script
    source('analytics/analytics.R')
    
    # Create analyzer instance
    analyzer <- DataAnalyzer$new()
    
    # Load and analyze data from data.csv
    analyzer$load_data('data/data.csv')
    analyzer$analyze()
    analyzer$generate_report()
    ```

#### Testing the API

Run tests to verify functionality:
```bash
cd backend
python test_app.py
```

### File Structure

```
Natural-Language-Processing-Suite/
├── backend/            # Python backend (Flask) files
│   ├── app.py          # Main Python application
│   ├── config.py       # Application configuration
│   ├── test_app.py     # Unit tests
│   └── requirements.txt  # Python dependencies
├── frontend/           # Web interface files
│   ├── index.html      # Main HTML file
│   ├── styles.css      # Modern CSS3 styling
│   └── app.js          # JavaScript functionality
├── analytics/          # R statistical analysis files
│   └── analytics.R     # R statistical analysis script
├── data/               # Data files and samples
│   └── data.csv        # Sample data file
├── assets/             # Assets and images
│   └── nlp_hero_image.jpg  # Project hero image
└── README.md           # Project documentation
```

### API Endpoints

The Python backend exposes the following API endpoints:

| Method | Endpoint          | Description                                  | Example Usage                                    |
| :----- | :---------------- | :------------------------------------------- | :----------------------------------------------- |
| `GET`  | `/`               | Serves the main web interface.               | `curl http://localhost:5000/`                    |
| `POST` | `/api/process`    | Processes text data using NLP algorithms.    | `curl -X POST http://localhost:5000/api/process -H "Content-Type: application/json" -d '{"text": "Sample text"}'` |
| `GET`  | `/api/analytics`  | Retrieves analytics results.                 | `curl http://localhost:5000/api/analytics`       |
| `POST` | `/api/upload`     | Uploads files for processing.                | `curl -X POST http://localhost:5000/api/upload -F "file=@document.txt"` |
| `GET`  | `/api/status`     | Checks the system status.                    | `curl http://localhost:5000/api/status`          |

**Example API Response:**

```json
{
  "original_text": "Sample text",
  "processed_text": "Processed: SAMPLE TEXT",
  "length": 11,
  "timestamp": "2024-10-09T20:00:00"
}
```

### Configuration

Configuration settings can be found and modified in `backend/config.py`:

```python
# Example configuration (backend/config.py)
APP_CONFIG = {
    'debug': True,
    'host': '0.0.0.0',
    'port': 5000,
    'max_content_length': 16 * 1024 * 1024  # 16MB in bytes
}

ANALYTICS_CONFIG = {
    'enable_r_integration': True,
    'auto_visualization': True,
    'export_formats': ['json', 'csv']
}
```

### Troubleshooting

#### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure the virtual environment is activated and dependencies are installed:
```bash
cd backend
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Issue: Port 5000 already in use
**Solution:** Change the port in `backend/config.py` or specify a different port when running the application.

#### Issue: Tests fail
**Solution:** Verify all dependencies are installed:
```bash
cd backend
python test_app.py -v
```

#### Issue: R not installed
**Solution:** R analytics is optional. You can use Python-only features if R is not available.

### License
This project is licensed under the MIT License.

### Contributions
Contributions are welcome! Please feel free to open an issue or submit a pull request.

### Contact
For any inquiries or support, please reach out via the email or LinkedIn provided above.

---

## Português

### Visão Geral
Esta **Natural Language Processing (NLP) Suite** é um projeto multi-linguagem que demonstra processamento de texto, análise de dados e visualização interativa. Ele combina Python, JavaScript e R em uma aplicação full-stack com backend Flask, frontend web responsivo e análise estatística baseada em R.

### Autor
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Tecnologias Utilizadas
Este projeto utiliza as seguintes tecnologias:

-   **Backend**: Python (Flask)
-   **Frontend**: HTML5, CSS3, JavaScript (ES6+)
-   **Análises**: R (ggplot2, dplyr, modelagem estatística)
-   **Processamento de Dados**: pandas, numpy
-   **Estilização**: CSS Grid, Flexbox, design responsivo
-   **Recursos Web Modernos**: Async/await, Web APIs, classes ES6
-   **Visualização**: Gráficos via R (ggplot2) e interatividade no frontend

### Funcionalidades

#### Funcionalidade Principal
-   **Processamento de Texto**: Endpoint de API para transformação e análise de texto.
-   **Análises**: Análise e visualização de dados via interface web.
-   **Interface Web Interativa**: Design responsivo para interação do usuário.
-   **Análise Estatística**: Ferramentas de análise e relatórios baseadas em R.

#### Interface Web
-   **UI/UX Moderna**: HTML5 semântico, design acessível e estilização profissional.
-   **Design Responsivo**: Otimizado para vários dispositivos usando CSS Grid e Flexbox.
-   **Interatividade Dinâmica**: JavaScript ES6+ impulsiona elementos interativos e atualizações em tempo real.

#### Análises e Relatórios
-   **Integração R**: Script R para modelagem estatística e visualização de dados.
-   **Processamento de Dados**: Ferramentas para carregamento, transformação e análise de dados.
-   **Visualizações**: Geração de gráficos usando ggplot2 e plots de correlação.

### Instalação

Para configurar a Natural-Language-Processing-Suite localmente, siga estes passos:

```bash
# 1. Clonar o repositório
git clone https://github.com/galafis/Natural-Language-Processing-Suite.git
cd Natural-Language-Processing-Suite

# 2. Configuração Python
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
cd ..

# 3. Configuração R (instalar pacotes necessários)
Rscript -e "install.packages(c('ggplot2', 'dplyr', 'corrplot'), repos='http://cran.us.r-project.org')"

# 4. Criar diretório de dados e dados de exemplo (se não existirem)
mkdir -p data
echo "text,category\nhello world,greeting\nNLP is great,technology" > data/data.csv
```

### Uso

#### Executando a Aplicação

1.  **Iniciar o Backend Python**
    ```bash
    cd backend
    python app.py
    ```
    A aplicação será executada em `http://localhost:5000`.

2.  **Acessar a Interface Web**
    Navegue para `http://localhost:5000` no seu navegador web.
    A interface web é responsiva em todos os dispositivos.

3.  **Executar Análises R**
    Você pode executar o script de análises R independentemente:
    ```r
    # Carregar script de análises R
    source('analytics/analytics.R')
    
    # Criar instância do analisador
    analyzer <- DataAnalyzer$new()
    
    # Carregar e analisar dados de data.csv
    analyzer$load_data('data/data.csv')
    analyzer$analyze()
    analyzer$generate_report()
    ```

#### Testando a API

Execute testes para verificar a funcionalidade:
```bash
cd backend
python test_app.py
```

### Estrutura de Arquivos

```
Natural-Language-Processing-Suite/
├── backend/            # Arquivos do backend Python (Flask)
│   ├── app.py          # Aplicação Python principal
│   ├── config.py       # Configurações da aplicação
│   ├── test_app.py     # Testes unitários
│   └── requirements.txt  # Dependências Python
├── frontend/           # Arquivos da interface web
│   ├── index.html      # Arquivo HTML principal
│   ├── styles.css      # Estilização CSS3 moderna
│   └── app.js          # Funcionalidade JavaScript
├── analytics/          # Arquivos de análise estatística R
│   └── analytics.R     # Script de análise estatística R
├── data/               # Arquivos de dados e exemplos
│   └── data.csv        # Arquivo de dados de exemplo
├── assets/             # Recursos e imagens
│   └── nlp_hero_image.jpg  # Imagem hero do projeto
└── README.md           # Documentação do projeto
```

### Endpoints da API

O backend Python expõe os seguintes endpoints da API:

| Método | Endpoint          | Descrição                                    | Exemplo de Uso                                       |
| :----- | :---------------- | :------------------------------------------- | :--------------------------------------------------- |
| `GET`  | `/`               | Serve a interface web principal.             | `curl http://localhost:5000/`                        |
| `POST` | `/api/process`    | Processa dados de texto usando algoritmos NLP. | `curl -X POST http://localhost:5000/api/process -H "Content-Type: application/json" -d '{"text": "Olá mundo"}'` |
| `GET`  | `/api/analytics`  | Recupera resultados de análises.             | `curl http://localhost:5000/api/analytics`           |
| `POST` | `/api/upload`     | Carrega arquivos para processamento.         | `curl -X POST http://localhost:5000/api/upload -F "file=@documento.txt"` |
| `GET`  | `/api/status`     | Verifica o status do sistema.                | `curl http://localhost:5000/api/status`              |

**Exemplo de Resposta da API (POST /api/process):**

```json
{
  "original_text": "Olá mundo",
  "processed_text": "Processed: OLÁ MUNDO"
}
```

**Exemplo de Resposta da API (GET /api/status):**

```json
{
  "status": "running",
  "version": "1.0.0",
  "timestamp": "2025-10-14T21:15:00.000000"
}
```

### Configuração

As configurações podem ser encontradas e modificadas em `backend/config.py`:

```python
# Exemplo de configuração (backend/config.py)
APP_CONFIG = {
    'debug': True,
    'host': '0.0.0.0',
    'port': 5000,
    'max_content_length': 16 * 1024 * 1024  # 16MB em bytes
}

ANALYTICS_CONFIG = {
    'enable_r_integration': True,
    'auto_visualization': True,
    'export_formats': ['json', 'csv']
}
```

### Solução de Problemas

#### Problema: Erro "ModuleNotFoundError: No module named 'flask'"
**Solução:** Certifique-se de que o ambiente virtual está ativado e as dependências estão instaladas:
```bash
cd backend
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
```

#### Problema: Porta 5000 já em uso
**Solução:** Altere a porta em `backend/config.py` ou especifique uma porta diferente ao executar a aplicação.

#### Problema: Testes falham
**Solução:** Verifique se todas as dependências estão instaladas:
```bash
cd backend
python test_app.py -v
```

#### Problema: R não instalado
**Solução:** A análise R é opcional. Você pode usar apenas os recursos Python se o R não estiver disponível.

### Licença
Este projeto está licenciado sob a Licença MIT.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Contato
Para quaisquer dúvidas ou suporte, entre em contato através do e-mail ou LinkedIn fornecidos acima.

