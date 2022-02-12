# SGU


## Sobre o projeto

<p> Sistema de gerenciamento de usuários (SGU), tem o objetivo primário de se conectar a um Active Directory (AD). O projeto está em formato de API básica, sem as métricas avançadas de segurança, pois o foco desse projeto é apenas demonstrar uma conexão básica.</p>

## Tecnologias

<p>O sistema foi desenvolvido em python com a framework Django. Além disso, utilizei a biblioteca "Django Auth Ldap", onde a mesma faz uso da biblioteca "ldap3", porém, ja modificada especificamente para fazer as métricas de autenticação com o AD. Por fim, utilizei a framework "Django rest framework", para configurar com facilidade uma API.</p>

## Funcionamento

<p>Através de uma requisição tipo POST, é passado no corpo da requisição o usuário e senha. </p>
--COLOCAR IMAGEM AKI

<p>Após o sistema receber essa requisição, ele consultará o AD para verificar se esse usuário existe. Caso o usuário existe e a senha esteja correta , ele cadastra no próprio banco de dados do Django, ele retorna os dados em formato JSON. Caso o usuário ja exista, ele não cadastra no banco de dados e retorna os dados em JSON. Mas caso não existe ou a senha esteja incorreta, ele apenas retorna um Not Found 404.</p>

--COLOCAR IMAGEM AKI
--COLOCAR IMAGEM AKI




