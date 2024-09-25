# Casos de Uso

## Caso de Uso 1: Registro de Usuário e Escolha de Plano

**Ator Principal:** Novo Usuário

**Atores Secundários:** Sistema de Pagamento (se o Plano Avançado for selecionado)

### Pré-condições:
- O usuário deve acessar a página de registro.
- O e-mail fornecido deve ser válido e não já registrado.

### Fluxo Principal:
1. O usuário acessa a página de registro.
2. O sistema apresenta as opções de registro via e-mail/senha ou redes sociais.
3. O usuário preenche os campos ou autentica via rede social.
4. O sistema valida as informações fornecidas.
5. O sistema exibe uma tela para o usuário escolher entre o Plano Básico (gratuito) ou Plano Avançado (pago).
6. O usuário seleciona o plano desejado.
7. Se o Plano Avançado for selecionado, o sistema solicita as informações de pagamento.
8. O sistema cria a conta do usuário e redireciona para a página inicial.

### Fluxos Alternativos:
- Se o e-mail já estiver registrado, o sistema informa que o e-mail não pode ser utilizado.
- Se o pagamento para o Plano Avançado falhar, o sistema informa o erro e solicita uma nova tentativa de pagamento ou a escolha do Plano Básico.

### Pós-condições:
- O usuário é registrado com sucesso.
- O plano escolhido (Básico ou Avançado) é configurado corretamente para o usuário.

### Pontos para Modelagem:
**Usuário:**
- **Atributos:** nome, e-mail, plano (básico ou avançado).
- **Métodos:** `registrar()`, `escolherPlano()`, `autenticarRedeSocial()`.

**Plano:**
- **Atributos:** tipo (básico, avançado), preço, benefícios.
- **Métodos:** `validarPlano()`, `processarPagamento()`.

**Sistema de Pagamento:**
- **Atributos:** status do pagamento, detalhes do cartão de crédito.
- **Métodos:** `validarPagamento()`, `confirmarPagamento()`.

---

## Caso de Uso 2: Login do Usuário

**Ator Principal:** Usuário Registrado

**Atores Secundários:** Nenhum

### Pré-condições:
- O usuário deve estar registrado.
- As credenciais devem ser válidas.

### Fluxo Principal:
1. O usuário acessa a página de login.
2. O sistema apresenta as opções de login por e-mail/senha ou redes sociais.
3. O usuário insere suas credenciais.
4. O sistema valida as credenciais.
5. O sistema verifica o plano do usuário (Básico ou Avançado) e redireciona para o painel principal, onde o acesso é limitado ou completo conforme o plano.

### Fluxos Alternativos:
- Se as credenciais forem inválidas, o sistema exibe uma mensagem de erro e solicita a correção dos dados ou recuperação da senha.

### Pós-condições:
- O usuário faz login com sucesso e tem acesso ao conteúdo conforme o plano escolhido.

### Pontos para Modelagem:
**Usuário:**
- **Atributos:** e-mail, senha, plano (básico ou avançado).
- **Métodos:** `login()`, `validarCredenciais()`.

---

## Caso de Uso 3: Consumo de Conteúdo

**Ator Principal:** Usuário Registrado

**Atores Secundários:** Nenhum

### Pré-condições:
- O usuário deve estar autenticado.
- O conteúdo deve estar disponível conforme o plano do usuário.

### Fluxo Principal:
1. O usuário acessa a biblioteca de conteúdo.
2. O sistema exibe os vídeos e quizzes disponíveis de acordo com o plano (Básico ou Avançado).
   - **Plano Básico:** Acesso a uma seleção limitada de vídeos e quizzes básicos.
   - **Plano Avançado:** Acesso a todos os vídeos, quizzes avançados e exercícios interativos.
3. O usuário interage com o conteúdo selecionado.
4. O sistema registra o progresso do usuário.

### Fluxos Alternativos:
- Se o conteúdo não estiver disponível, o sistema informa o usuário que o material não está acessível no momento.

### Pós-condições:
- O usuário consome o conteúdo, com o progresso sendo registrado no sistema.

### Pontos para Modelagem:
**Usuário:**
- **Atributos:** nome, plano (básico ou avançado), progresso no conteúdo.
- **Métodos:** `assistirConteudo()`, `interagirQuiz()`.

**Conteúdo:**
- **Atributos:** título, tipo (vídeo, quiz), acesso (básico, avançado).
- **Métodos:** `exibirConteudo()`, `registrarProgresso()`.

---

## Caso de Uso 4: Participação em Fóruns

**Ator Principal:** Usuário Registrado

**Atores Secundários:** Nenhum

### Pré-condições:
- O usuário deve estar autenticado.
- O fórum deve estar ativo e permitir novas postagens.

### Fluxo Principal:
1. O usuário acessa a seção de fóruns.
2. O sistema exibe os fóruns disponíveis, diferenciando entre fóruns gerais e exclusivos (somente para usuários do Plano Avançado).
3. Todos os usuários podem visualizar e interagir nos fóruns gerais.
4. Usuários do Plano Avançado podem criar tópicos e participar dos fóruns exclusivos.
5. O usuário posta uma pergunta ou comentário ou interage em um fórum.
6. O sistema publica o post ou a resposta do usuário.

### Fluxos Alternativos:
- Se o fórum estiver fechado ou não permitir novas postagens, o sistema exibe uma mensagem informando que o fórum está inativo.

### Pós-condições:
- O usuário interage com sucesso nos fóruns conforme seu plano.

### Pontos para Modelagem:
**Usuário:**
- **Atributos:** nome, plano (básico ou avançado), permissões no fórum.
- **Métodos:** `criarPost()`, `responder()`.

**Fórum:**
- **Atributos:** título, status (ativo, inativo), tipo (geral, exclusivo).
- **Métodos:** `exibirPost()`, `criarTopico()`.

---

## Caso de Uso 5: Gerenciamento de Perfil e Assinatura

**Ator Principal:** Usuário Registrado

**Atores Secundários:** Sistema de Pagamento (se houver alteração no plano para Avançado)

### Pré-condições:
- O usuário deve estar autenticado.
- O sistema deve validar as novas informações e o pagamento, se aplicável.

### Fluxo Principal:
1. O usuário acessa a página de perfil.
2. O sistema exibe as informações atuais do perfil.
3. O usuário pode:
   - Editar informações pessoais (nome, e-mail, etc.).
   - Alterar o plano de assinatura (do Plano Básico para o Avançado ou vice-versa).
   - Gerenciar as informações de pagamento, caso tenha o Plano Avançado.
4. O sistema valida as novas informações e atualiza o perfil do usuário.

### Fluxos Alternativos:
- Se houver falha na validação de dados ou no pagamento, o sistema solicita a correção das informações ou uma nova tentativa de pagamento.

### Pós-condições:
- O perfil do usuário é atualizado com sucesso, incluindo mudanças no plano e nas informações de pagamento.

### Pontos para Modelagem:
**Usuário:**
- **Atributos:** nome, e-mail, plano, informações de pagamento.
- **Métodos:** `editarPerfil()`, `alterarPlano()`, `gerenciarPagamento()`.

**Sistema de Pagamento:**
- **Atributos:** status do pagamento, informações de cobrança.
- **Métodos:** `validarPagamento()`, `confirmarPagamento()`.
