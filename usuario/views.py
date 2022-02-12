from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from .serializers import UserSerializer, UsuarioSerializer, SetorSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_auth_ldap.backend import LDAPBackend, _LDAPUser
from .models import Usuario, Setor


#Método de Verificação ser o usuário e senha conferem com o do AD
def authenticate(request,username, password):
    # teste_password()
    UserModel = get_user_model()
    #verifica o usuario no AD e retorna o usuário no BD do Django
    
    userGet = LDAPBackend().authenticate(request,username,password)
    
    #Somente para teste fora do AD
    #userGet = UserModel.objects.get(username=username)
    if userGet == None:
        return False
    if userGet.check_password(password) != None:
        if userGet.ldap_user.group_names:
            print(dir(userGet))
            print("Tem grupo")
            print(userGet.ldap_user.group_names)
        else:
            print("Não tem grupo")
        user = userGet
        user.set_password(None)
        user.save()
        return userGet
    else:
        print("false")
        user = UserModel.objects.all()
        return False

def mapping_setor(aut):
    usuario = aut.usuario
    setor = Setor.objects.filter(setor__in = aut.ldap_user.group_names)
    if usuario.setor != setor.first():
        usuario.setor = setor.first()
        usuario.save()

@api_view(['POST'])
def autenticar(request):
    UserModel = get_user_model()
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'POST':
        username = request.data["username"]
        password = request.data["password"]

        aut = authenticate(request,username, password)
        if aut:
            users = UserModel.objects.get(username=username)
    #Verifica se o usuário ja está vinculado ao setor do AD.
            if not Usuario.objects.filter(usuario = users):
                newUser = Usuario()
                setor = Setor.objects.filter(setor = userGet.ldap_user.group_names)
                print(setor)
                # setor = Setor.objects.get(setor=userGroup)
                # newUser.setor = setor
                newUser.usuario = users
                newUser.save()
            setor = Setor.objects.filter(setor__in = aut.ldap_user.group_names)
            mapping_setor(aut)
            print(aut)
            print(setor)
            usuario = Usuario.objects.get(usuario = users)
            serializer = UsuarioSerializer(usuario, many=False)
            return Response(serializer.data)
        else:
            raise NotFound(detail="Error 404, username or password incorrect", code=404)




@api_view(['GET'])
def user(request,id):
    UserModel = get_user_model()
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        usuario = Usuario.objects.get(pk = id)
        serializer = UsuarioSerializer(usuario, many=False)
        return Response(serializer.data)


class UsersViewSet(viewsets.ModelViewSet):
    UserModel = get_user_model()
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

