# 💿 Sistema de Gerenciamento de Usuário (SGU)


## 📚 Sobre o projeto

<p> Sistema de gerenciamento de usuários (SGU), tem o objetivo primário de se conectar a um Active Directory (AD). A motivação do projeto é justamente para ambientes que possuem algum tipo de AD e possuem outros sistemas web's internos. Afim de evitar um número alto de diferentes login's e senhas, nessa ocasião, é interessante utilizar as mesmas informações do AD para a autenticação.
O projeto está em formato de API básica, sem as métricas avançadas de segurança, pois o foco desse projeto é apenas demonstrar uma conexão básica entre um sistema em Django e o AD.</p>

<hr/>

## 💻 Tecnologias

<p>O sistema foi desenvolvido em python com a framework Django. Além disso, utilizei a biblioteca "Django Auth Ldap", onde a mesma faz uso da biblioteca "ldap3", porém, ja modificada especificamente para fazer as métricas de autenticação com o AD. Por fim, utilizei a framework "Django rest framework", para configurar com facilidade uma API.</p>

<hr />

## ⚡ Funcionamento

<p>Através de uma requisição tipo POST, é passado no corpo da requisição o usuário e senha. </p>

<p>Após o sistema receber essa requisição, ele consultará o AD para verificar se esse usuário existe. Caso o usuário existe e a senha esteja correta , ele cadastra no próprio banco de dados do Django, ele retorna os dados em formato JSON. Caso o usuário ja exista, ele não cadastra no banco de dados e retorna os dados em JSON. Mas caso não existe ou a senha esteja incorreta, ele apenas retorna um Not Found 404.</p>

<p>A cada requisição de autenticação, o sistema verifica se houve alguma modificação do setor do usuário. Caso o setor tenha sido mudado no AD, o sistema alterará no banco de dados do Django. Para a alteração de setor automática funcionar, é necessário que o nome do setor no banco de dados do Django seja exatamente igual ao grupo no AD </p>

<hr/>

## 🎨 Algumas imagens

<img src="https://raw.githubusercontent.com/patrickvrodrigues/SGU/main/prints/1.PNG" />
<img src="https://raw.githubusercontent.com/patrickvrodrigues/SGU/main/prints/2.PNG" />
<img src="https://raw.githubusercontent.com/patrickvrodrigues/SGU/main/prints/3.PNG" />
<img src="https://raw.githubusercontent.com/patrickvrodrigues/SGU/main/prints/4.PNG" />

<hr/>

## 🔗 Links úteis

<a href="https://techexpert.tips/pt-br/django-pt-br-2/django-autenticacao-ldap-no-diretorio-ativo/">https://techexpert.tips/pt-br/django-pt-br-2/django-autenticacao-ldap-no-diretorio-ativo/<a/>

<a href="https://ldap3.readthedocs.io/en/latest/">https://ldap3.readthedocs.io/en/latest/<a/>

<a href="https://django-auth-ldap.readthedocs.io/en/latest/">https://django-auth-ldap.readthedocs.io/en/latest/<a/>

<a href="https://www.django-rest-framework.org/">https://www.django-rest-framework.org/<a/>
