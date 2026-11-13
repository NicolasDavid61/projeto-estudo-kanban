import random

def gerar_token():
    """Gera token numérico de 6 dígitos para recuperação de senha."""
    return f"{random.randint(0, 999999):06d}"
