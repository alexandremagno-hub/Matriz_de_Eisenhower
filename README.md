# ⏱️ Matriz de Eisenhower

Gerenciador de tarefas feito com [Streamlit](https://streamlit.io). Ele organiza as tarefas automaticamente nos quatro quadrantes da Matriz de Eisenhower, de acordo com a **urgência** e a **importância** de cada uma:

| | Importância alta (≥ 3) | Importância baixa (< 3) |
|---|---|---|
| **Urgência alta (≥ 3)** | 🔴 Fazer agora | 🟡 Delegar |
| **Urgência baixa (< 3)** | 🟢 Planejar | ⚪ Eliminar |

## Pré-requisitos

- **Python 3.10 ou mais recente** instalado. Para conferir, rode `python3 --version` no Linux/macOS ou `python --version` no Windows.

## Passo a passo

### 1. Baixe o projeto

```bash
git clone <url-do-repositorio>
cd Matriz_de_Eisenhower
```

Se você recebeu o projeto em uma pasta ou arquivo `.zip`, extraia e abra o terminal dentro da pasta.

### 2. Crie o ambiente virtual (só na primeira vez)

**Linux / macOS**
```bash
python3 -m venv .venv
```

**Windows**
```powershell
python -m venv .venv
```

### 3. Ative o ambiente virtual

**Linux / macOS**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Prompt de Comando)**
```cmd
.venv\Scripts\activate.bat
```

Com o ambiente ativo, o nome `(.venv)` aparece no começo da linha do terminal.

### 4. Instale as dependências (só na primeira vez)

```bash
pip install -r requirements.txt
```

### 5. Abra a aplicação

```bash
streamlit run Eisenhower.py
```

O navegador abre sozinho em **http://localhost:8501**. Se não abrir, copie esse endereço e cole no navegador.

Para **parar** a aplicação, volte ao terminal e aperte `Ctrl + C`.

## Da próxima vez

Basta repetir os passos 3 e 5:

```bash
cd Matriz_de_Eisenhower
source .venv/bin/activate      # Windows: .venv\Scripts\activate
streamlit run Eisenhower.py
```

## Como usar

1. Na barra lateral, digite a **descrição da tarefa**.
2. Escolha o **prazo final**.
3. Ajuste a **urgência** e a **importância**, de 1 (baixa) a 5 (alta).
4. Clique em **Adicionar**. A tarefa aparece no quadrante correspondente.
5. Clique em **Baixar tarefa em CSV** para salvar a lista.

> ⚠️ As tarefas ficam guardadas apenas enquanto a página está aberta. Se você recarregar a página ou fechar a aplicação, elas se perdem. Baixe o CSV antes de sair se quiser guardar a lista.

## Problemas comuns

| Problema | Solução |
|---|---|
| `streamlit: command not found` ou `'streamlit' não é reconhecido` | O ambiente virtual não está ativo. Repita o passo 3. |
| `ModuleNotFoundError: No module named 'streamlit'` | Rode o passo 4 com o ambiente ativo. |
| No Windows, o PowerShell bloqueia o `Activate.ps1` | Rode `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente de novo, ou use o Prompt de Comando. |
| A porta 8501 já está em uso | Rode `streamlit run Eisenhower.py --server.port 8502` e acesse http://localhost:8502. |
