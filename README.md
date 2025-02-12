# Bot-de-Monitoramento-de-Pre-os-com-Selenium
Este bot automatiza a verificação de preços de produtos no Mercado Livre utilizando Selenium. Quando o preço de um produto atinge ou cai abaixo de um valor alvo, um e-mail de alerta é enviado automaticamente para o usuário.

Tecnologias Utilizadas

Python 3

Selenium

smtplib (para envio de e-mails)

WebDriver do Chrome

Como Instalar e Rodar

1. Clonar o Repositório

git clone https://github.com/seu-usuario/nome-do-repositorio.git
cd nome-do-repositorio

2. Criar um Ambiente Virtual (Opcional, mas Recomendado)

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows

3. Instalar Dependências

pip install -r requirements.txt

4. Configurar Credenciais

Crie um arquivo .env ou config.json com suas credenciais de e-mail para envio de alertas:

{
  "email": "seu-email@gmail.com",
  "senha": "sua-senha"
}

Importante: Nunca exponha credenciais diretamente no código-fonte.

5. Baixar e Configurar o ChromeDriver

Baixe o ChromeDriver compatível com sua versão do Google Chrome em ChromeDriver. Salve o executável e defina o caminho no script.

6. Executar o Bot

mercadoLivreBot.py

Exemplo de Uso

O bot acessa o Mercado Livre, pesquisa um produto (por padrão, "notebook"), obtém o preço do primeiro resultado e, se estiver abaixo do preço alvo, envia um e-mail de notificação.

Melhorias Futuras

Adicionar suporte a múltiplos produtos

Melhorar a robustez da busca de elementos

Implementar um banco de dados para histórico de preços

Criar uma interface gráfica para facilitar o us
