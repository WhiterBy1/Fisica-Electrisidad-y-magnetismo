from dataclasses import dataclass

@dataclass
class ConstantesFisicas:
    """Clase para almacenar constantes físicas fundamentales"""
    # Constantes En Ecuaciones
    G: float = 6.674e-11    # Constante de gravitación universal (N⋅m²/kg²)
    g: float = 9.81         # Aceleración gravitatoria en la Tierra (m/s²)
    c: float = 2.998e8      # Velocidad de la luz (m/s)
    k: float = 8.988e9      # Constante de Coulomb (N⋅m²/C²)
    epsilon_0: float = 8.854e-12  # Permitividad del vacío (F/m)
    h: float = 6.626e-34    # Constante de Planck (J⋅s)
    # Atomos
    MASA_PROTON: float = 1.6726e-27  # kg
    MASA_NEUTRON: float= 1.6750e-27  # kg
    MASA_ELECTRON: float = 9.1094e-31  # kg
    CARGA_ELECTRON: float = 1.602e-19  # C  (proton = +e, electrón = -e)