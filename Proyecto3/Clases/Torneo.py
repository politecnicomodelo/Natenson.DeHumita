class Torneo(object):
    Equipos=[]

    Partidos=[]

    def agregarEquipos(self, n):
        for variable in self.Equipos:
            if variable.Nombre==n.Nombre:
                return False
        self.Equipos.append(n)
        return True
