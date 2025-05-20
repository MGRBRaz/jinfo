# JGR Broker - Sistema de Acompanhamento de Processos

Este é o sistema de acompanhamento de processos de importação e exportação da JGR Broker.

## Conteúdo do Pacote

Este pacote contém todos os arquivos necessários para fazer o deploy do sistema no Streamlit Cloud:

- `app.py` - Arquivo principal do aplicativo
- `data.py` - Gerenciamento de dados
- `utils.py` - Funções utilitárias
- `components/` - Pasta com os componentes da interface
- `assets/` - Pasta com recursos (CSS, imagens, etc.)
- Arquivos de geração de HTML e exportação
- Arquivos de estilo e interatividade
- Arquivos de configuração

## Como fazer o Deploy

1. Crie um repositório no GitHub
2. Faça upload de todos estes arquivos mantendo a estrutura de pastas
3. Acesse [share.streamlit.io](https://share.streamlit.io)
4. Faça login com sua conta do GitHub
5. Clique em "New app"
6. Selecione seu repositório
7. Mantenha app.py como arquivo principal
8. Clique em "Deploy!"

Para instruções detalhadas, consulte o arquivo `guia_facil_deploy_streamlit.md` incluído neste pacote.

## Observações Importantes

- O sistema usa arquivos JSON para armazenar dados, o que é adequado para testes mas não para produção
- Para uso em produção, recomenda-se migrar para um banco de dados
- As exportações HTML são salvas temporariamente no Streamlit Cloud

## Suporte

Em caso de dúvidas, entre em contato com o desenvolvedor.