# Solução interna para um problema que enchia o disco C do servidor e não enviava os exames para a aplicação laudoweb (visualização de exames)

O servidor onde fica a central de recebimento de exames enche-se de arquivos de imagens feitos no raio X e enviados para a aplicação LaudoWeb para visualização dos exames e análise pelos médicos. Esse trabalho era sempre feito manualmente, entrando pasta por pasta, mês por mês, dia por dia, e verificando o que podia ser excluído ou não (os exames do dia atual não podiam ser excluídos). Às vezes, eram puxados exames antigos com a data de hoje para revisualização.

Antes que eu abria o servidor todos os dias para excluir imagens, hoje eu somente abro para verificação.

**- Observações:**
- A pasta pode estar em outro servidor na rede (além do servidor local)
- Python 3.12 deve estar instalado no servidor
- Deve-se fazer um agendamento de tarefa executando essa tarefa conforme o tempo da sua necessidade, eu deixo pra executar todos os dias a cada 1h.
- O código só irá excluir os arquivos se determinado espaço livre em disco for atingido.

## Funcionalidades

Este código ele entra pasta de acordo com a hierarquia (ANO > MÊS > DIA), verifica se há alguma data diferente da atual e exclui os ANOS não condizentes, em seguida, faz o mesmo para o sub-diretório de MÊS e logo após faz para o subsub-diretório de DIA. Deixando apenas os exames que constam a data de hoje. 

**1. Clone o repositório:**

```bash
git clone https://https://igorcarmona-git/telelaudos_deleteImages_automation.git
cd telelaudos_deleteImages_automation
```

**2. Instale as dependências:** (Recomendado via scriptlogon (netlogon))
- Utiliza as bibliotecas padrões do Python com sua instalação (Python 3.12)

**3. Como executar:**
- Agendar no Agendador de Tarefas do windows com privilégios de administrador.
- Executar conforme sua necessidade, recomendo todos os dias a cada 1h.

## Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests para melhorar o projeto.

**Para mais informações, entrar em contato via redes sociais.**
