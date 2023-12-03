import numpy as np

def translacao(ponto, delta):
    """
    Função para realizar uma translação em um ponto tridimensional.

    Args:
    ponto (tuple): Um ponto no formato (X, Y, Z).
    delta (tuple): As quantidades de translação em cada eixo (DeltaX, DeltaY, DeltaZ).

    Returns:
    tuple: O novo ponto após a translação.
    """
    return tuple(np.add(ponto, delta))

def rotacao_z(ponto, theta):
    """
    Função para realizar uma rotação em torno do eixo Z em um ponto tridimensional.

    Args:
    ponto (tuple): Um ponto no formato (X, Y, Z).
    theta (float): O ângulo de rotação em radianos.

    Returns:
    tuple: O novo ponto após a rotação.
    """
    x, y, z = ponto
    novo_x = x * np.cos(theta) - y * np.sin(theta)
    novo_y = x * np.sin(theta) + y * np.cos(theta)
    return (novo_x, novo_y, z)

def escala(ponto, fator):
    """
    Função para realizar uma escala em um ponto tridimensional.

    Args:
    ponto (tuple): Um ponto no formato (X, Y, Z).
    fator (float): O fator de escala.

    Returns:
    tuple: O novo ponto após a escala.
    """
    return tuple(np.multiply(ponto, fator))

# Exemplo de uso:
ponto_original = (1, 2, 3)
delta_translacao = (2, 3, 1)
angulo_rotacao = np.pi / 4  # 45 graus em radianos
fator_escala = 2

ponto_transladado = translacao(ponto_original, delta_translacao)
ponto_rotacionado = rotacao_z(ponto_transladado, angulo_rotacao)
ponto_escalado = escala(ponto_rotacionado, fator_escala)

print("Ponto Original:", ponto_original)
print("Ponto Transladado:", ponto_transladado)
print("Ponto Rotacionado:", ponto_rotacionado)
print("Ponto Escalado:", ponto_escalado)
