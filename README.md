# Natural-Language-Processing-Suite

![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![R](https://img.shields.io/badge/R-4.0%2B-blue?logo=r&logoColor=white)
![Top Language](https://img.shields.io/github/languages/top/galafis/Natural-Language-Processing-Suite)


![Natural Language Processing](assets/nlp_hero_image.jpg)


## English

### Overview
This **Natural Language Processing (NLP) Suite** is an advanced, comprehensive platform designed for robust text analysis, data processing, and interactive visualization. It leverages a modern technology stack, integrating multiple programming languages to deliver professional-grade solutions for various NLP tasks. From real-time analytics to scalable architecture, this suite provides a powerful toolkit for developers and data scientists.

### Author
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Technologies Used
This project integrates a diverse set of technologies to ensure high performance, scalability, and a rich user experience:

-   **Backend**: Python (Flask, FastAPI), SQLite
-   **Frontend**: HTML5, CSS3, JavaScript (ES6+)
-   **Analytics**: R (ggplot2, dplyr, statistical modeling)
-   **Data Processing**: pandas, numpy, scikit-learn
-   **Styling**: CSS Grid, Flexbox, responsive design
-   **Modern Web Features**: Async/await, Web APIs, ES6 classes
-   **Visualization**: Interactive charts, real-time dashboards

### Features

#### Core Functionality
-   **Advanced NLP Processing**: High-performance algorithms for various NLP tasks.
-   **Real-time Analytics**: Live data analysis and visualization capabilities.
-   **Interactive Web Interface**: Modern, responsive design for intuitive user interaction.
-   **Comprehensive Statistical Analysis**: R-based analytics and reporting tools.
-   **Scalable Architecture**: Designed for enterprise-level performance and future expansion.

#### Web Interface
-   **Modern UI/UX**: Semantic HTML5, accessible design, and professional styling.
-   **Responsive Design**: Optimized for various devices using CSS Grid and Flexbox.
-   **Dynamic Interactivity**: JavaScript ES6+ powers interactive elements and real-time updates.

#### Analytics & Reporting
-   **R Integration**: Seamless integration with R for advanced statistical modeling and data visualization.
-   **Automated Data Processing**: Tools for efficient data cleaning, transformation, and preparation.
-   **Rich Visualizations**: Generate interactive charts and comprehensive dashboards.
-   **Export Options**: Support for various report and data export formats (JSON, CSV, PDF).

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
Rscript -e "install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'), repos=\'http://cran.us.r-project.org\')"

# 4. Create data directory and sample data (if not present)
mkdir -p data
echo "text,category\nhello world,greeting\nNLP is great,technology" > data/data.csv
```

### Usage

#### Running the Application

1.  **Start the Python Backend (Flask/FastAPI)**
    ```bash
    cd backend
    python app.py
    ```
    The application will run on `http://localhost:5000`.

2.  **Access the Web Interface**
    Navigate to `http://localhost:5000` in your web browser.
    The interactive dashboard provides real-time functionality and is responsive across devices.

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
├── backend/            # Python backend (Flask/FastAPI) files
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
  "status": "success",
  "processed_text": "Sample processed text",
  "sentiment": "positive",
  "confidence": 0.92,
  "timestamp": "2024-10-09T20:00:00Z"
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
    'max_file_size': '16MB'
}

ANALYTICS_CONFIG = {
    'enable_r_integration': True,
    'auto_visualization': True,
    'export_formats': ['json', 'csv', 'pdf']
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

### Performance Features
-   **Multi-threading**: Utilizes parallel processing for enhanced performance.
-   **Caching**: Implements intelligent caching mechanisms for faster response times.
-   **Memory Optimization**: Efficient memory usage and management for resource-intensive tasks.
-   **Scalability**: Supports horizontal scaling for enterprise-level deployments.

### License
This project is licensed under the MIT License.

### Contributions
Contributions are welcome! Please feel free to open an issue or submit a pull request.

### Contact
For any inquiries or support, please reach out via the email or LinkedIn provided above.

---

## Português

### Visão Geral
Esta **Natural Language Processing (NLP) Suite** é uma plataforma avançada e abrangente, projetada para análise robusta de texto, processamento de dados e visualização interativa. Ela utiliza uma stack de tecnologia moderna, integrando múltiplas linguagens de programação para entregar soluções de nível profissional para diversas tarefas de NLP. Desde análises em tempo real até arquitetura escalável, esta suite oferece um poderoso conjunto de ferramentas para desenvolvedores e cientistas de dados.

### Autor
**Gabriel Demetrios Lafis**
- Email: gabrieldemetrios@gmail.com
- LinkedIn: [Gabriel Demetrios Lafis](https://www.linkedin.com/in/gabriel-demetrios-lafis-62197711b)
- GitHub: [galafis](https://github.com/galafis)

### Tecnologias Utilizadas
Este projeto integra um conjunto diversificado de tecnologias para garantir alto desempenho, escalabilidade e uma rica experiência do usuário:

-   **Backend**: Python (Flask, FastAPI), SQLite
-   **Frontend**: HTML5, CSS3, JavaScript (ES6+)
-   **Análises**: R (ggplot2, dplyr, modelagem estatística)
-   **Processamento de Dados**: pandas, numpy, scikit-learn
-   **Estilização**: CSS Grid, Flexbox, design responsivo
-   **Recursos Web Modernos**: Async/await, Web APIs, classes ES6
-   **Visualização**: Gráficos interativos, dashboards em tempo real

### Funcionalidades

#### Funcionalidade Principal
-   **Processamento NLP Avançado**: Algoritmos de alta performance para diversas tarefas de NLP.
-   **Análises em Tempo Real**: Capacidades de análise e visualização de dados ao vivo.
-   **Interface Web Interativa**: Design moderno e responsivo para interação intuitiva do usuário.
-   **Análise Estatística Abrangente**: Ferramentas de análise e relatórios baseadas em R.
-   **Arquitetura Escalável**: Projetada para desempenho de nível empresarial e expansão futura.

#### Interface Web
-   **UI/UX Moderna**: HTML5 semântico, design acessível e estilização profissional.
-   **Design Responsivo**: Otimizado para vários dispositivos usando CSS Grid e Flexbox.
-   **Interatividade Dinâmica**: JavaScript ES6+ impulsiona elementos interativos e atualizações em tempo real.

#### Análises e Relatórios
-   **Integração R**: Integração perfeita com R para modelagem estatística avançada e visualização de dados.
-   **Processamento Automatizado de Dados**: Ferramentas para limpeza, transformação e preparação eficiente de dados.
-   **Visualizações Ricas**: Geração de gráficos interativos e dashboards abrangentes.
-   **Opções de Exportação**: Suporte para vários formatos de exportação de relatórios e dados (JSON, CSV, PDF).

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
Rscript -e "install.packages(c(\'ggplot2\', \'dplyr\', \'corrplot\', \'plotly\'), repos=\'http://cran.us.r-project.org\')"

# 4. Criar diretório de dados e dados de exemplo (se não existirem)
mkdir -p data
echo "text,category\nhello world,greeting\nNLP is great,technology" > data/data.csv
```

### Uso

#### Executando a Aplicação

1.  **Iniciar o Backend Python (Flask/FastAPI)**
    ```bash
    cd backend
    python app.py
    ```
    A aplicação será executada em `http://localhost:5000`.

2.  **Acessar a Interface Web**
    Navegue para `http://localhost:5000` no seu navegador web.
    O dashboard interativo oferece funcionalidade em tempo real e é responsivo em todos os dispositivos.

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
├── backend/            # Arquivos do backend Python (Flask/FastAPI)
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
    'max_file_size': '16MB'
}

ANALYTICS_CONFIG = {
    'enable_r_integration': True,
    'auto_visualization': True,
    'export_formats': ['json', 'csv', 'pdf']
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

### Recursos de Performance
-   **Multi-threading**: Utiliza processamento paralelo para melhor desempenho.
-   **Cache**: Implementa mecanismos de cache inteligentes para tempos de resposta mais rápidos.
-   **Otimização de Memória**: Uso eficiente de memória e gerenciamento para tarefas intensivas em recursos.
-   **Escalabilidade**: Suporta escalonamento horizontal para implantações de nível empresarial.

### Licença
Este projeto está licenciado sob a Licença MIT.

### Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

### Contato
Para quaisquer dúvidas ou suporte, entre em contato através do e-mail ou LinkedIn fornecidos acima.

