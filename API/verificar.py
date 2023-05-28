import jwt

def verify_token(token, key):
    try:
        # Decodifica o token e verifica sua validade
        tok = get_token(token, key)

        print("Token válido.")
        print(tok)
        # Você pode imprimir mais informações aqui, se necessário
        
        return True
    except:
        print("Token invalido e/ou expirou.")
        return False
    
def get_token(token, key):
    return jwt.decode(token,key,algorithms=["HS256"], verify=False)

# Token de exemplo
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg1MjMxNDI3LCJpYXQiOjE2ODUyMzEzMDcsImp0aSI6IjYzZTgyZDIwNDYyZjQwMjBiYTI5ZjlhYjM5ZjQ4YTM1IiwidXNlcl9pZCI6MX0.nGIrnObYsQeaYhtRJIYd9RvnTOQ1pIPsWIauJ5wNgKE"
key = '&bo&pzkta3q)k6kjj3a)lj6mlfun-+n112wp@i!gb_z4c(6q0d'

# Verifica o token
verify_token(token,key)