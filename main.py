from Ecuations.ecuations import CalculadoraLeyes
from models.basics import particle


if __name__ == "__main__":
    calc = CalculadoraLeyes()
    
    print("=== Ejemplos de cálculos con leyes físicas ===\n")
    
    # 1. Fuerza gravitacional entre la Tierra y la Luna
    masa_tierra = 5.972e24  # kg
    masa_luna = 7.34767309e22  # kg
    distancia = 384400000  # m
    
    fuerza = calc.gravedad_universal(m1=masa_tierra, m2=masa_luna, r=distancia)
    print(f"Fuerza gravitacional Tierra-Luna: {fuerza:.2e} N")
    
    # 2. Campo gravitatorio en la superficie de Marte
    masa_marte = 6.39e23  # kg
    radio_marte = 3.389e6  # m
    
    g_marte = calc.campo_gravitatorio(M=masa_marte, r=radio_marte)
    print(f"Aceleración gravitatoria en Marte: {g_marte:.2f} m/s²")
    
    # 4. Fuerza electrostática entre dos cargas
    fuerza_e = calc.fuerza_electrica(q1=1e-6, q2=1e-6, r=0.1)
    print(f"Fuerza electrostática: {fuerza_e:.2e} N")
    
particle_1 = particle("q1", charge=1e-6)
particle_2 = particle("q2", charge=1e-2)

fuerza_e_particulas = calc.fuerza_electrica(q1=particle_1.charge, q2=particle_2.charge, r=0.1)
print(f"Fuerza electrostática de particulas: {fuerza_e_particulas:.2e} N")