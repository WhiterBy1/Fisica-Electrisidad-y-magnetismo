from typing import Dict
from constantes import ConstantesFisicas
from sympy import symbols, solve, Eq, pi

class Ecuation:
    def __init__(self):
        self.constantes = ConstantesFisicas()
        # Símbolos para variables comunes
        self.m1, self.m2, self.r = symbols('m1 m2 r')
        self.F, self.g, self.M = symbols('F g M')
        #Electrica
        self.q1, self.q2 = symbols('q1 q2')
        #Movimiento
        self.v, self.v0, self.a, self.t, self.d = symbols('v v0 a t d')
        
    def _resolver_ecuacion(self, ecuacion:Eq, valores_conocidos: Dict):
        """Método auxiliar para resolver ecuaciones"""
        # Convertir valores conocidos a formato SymPy
        valores = {
            getattr(self, var): valor 
            for var, valor in valores_conocidos.items()
        }
        
        # Sustituir valores conocidos
        ecuacion_con_valores = ecuacion.subs(valores)
        
        # Resolver
        solucion = solve(ecuacion_con_valores)
        
        # Convertir resultado a formato amigable
        if isinstance(solucion, list):
            # Tomar solo valores reales positivos si hay múltiples soluciones
            solucion = [s for s in solucion if s.is_real and s > 0]
            if solucion:
                return float(solucion[0])
        elif isinstance(solucion, dict):
            return {str(var): float(val) for var, val in solucion.items()}
        
        return solucion
    
class CalculadoraLeyes(Ecuation):    
    def gravedad_universal(self, **kwargs):
        """
        Ley de Gravitación Universal: F = G * (m1 * m2) / r²
        
        Parámetros:
        - m1: masa del primer cuerpo (kg)
        - m2: masa del segundo cuerpo (kg)
        - r: distancia entre centros de masa (m)
        - F: fuerza gravitacional (N)
        """
        ecuacion = Eq(self.F, self.constantes.G *((self.m1 * self.m2)/self.r**2))
        return self._resolver_ecuacion(ecuacion, kwargs)
    
    def campo_gravitatorio(self, **kwargs):
        """
        Campo gravitatorio: g = G * M / r²
        
        Parámetros:
        - g: aceleración gravitatoria (m/s²)
        - M: masa del cuerpo que genera el campo (kg)
        - r: distancia al centro del cuerpo (m)
        """
        ecuacion = Eq(self.g, self.constantes.G * self.M / (self.r**2))
        return self._resolver_ecuacion(ecuacion, kwargs)
    
    def fuerza_electrica(self, **kwargs):
        """
        Ley de Coulomb: F = k * q1 * q2 / r²
        
        Parámetros:
        - k: constante de Coulomb (8.9875517923 × 10^9 N·m²/C²)
        - q1: carga del primer cuerpo (C)
        - q2: carga del segundo cuerpo (C)
        - r: distancia entre centros de carga (m)
        - F: fuerza eléctrica (N)
        """
        ecuacion = Eq(self.F, self.constantes.c * ((self.q1* self.q2)/self.r**2))
        return self._resolver_ecuacion(ecuacion, kwargs)

class CalculadoraCinematica(Ecuation):
    def __init__(self):
        # Definir ecuaciones del movimiento
        self.ecuaciones = {
            'mru': [
                Eq(self.v, self.d/self.t),           # v = d/t
            ],
            'mrua': [
                Eq(self.v, self.v0 + self.a*self.t),                    # v = v0 + at
                Eq(self.d, self.v0*self.t + (self.a*self.t**2)/2),     # d = v0*t + (1/2)at²
                Eq(self.v**2, self.v0**2 + 2*self.a*self.d)            # v² = v0² + 2ad
            ]
        }
