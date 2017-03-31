from Clases.Equipos import Equipos
from Clases.Jugadores import Jugadores
from Clases.Torneo import Torneo

CarlitosTevez=Jugadores()
CarlitosTevez.setNombre("Carlos Tevez")
CarlitosTevez.setNacimiento(1984,2,5)
CarlitosTevez.setNumero(32)

ElFlacoSchiavi=Jugadores()
ElFlacoSchiavi.setNombre("Rolando Schiavi")
ElFlacoSchiavi.setNacimiento(1973,1,18)
ElFlacoSchiavi.setNumero(4)

LioMessi=Jugadores()
LioMessi.setNombre("Lionel Messi")
LioMessi.setNacimiento(1987,6,24)
LioMessi.setNumero(10)

IndioSolari=Jugadores()
IndioSolari.setNombre("Carlos Alberto Solari")
IndioSolari.setNacimiento(1949,1,16)
IndioSolari.setNumero(24)

SilvioSoldan=Jugadores()
SilvioSoldan.setNombre("William Silvio Soldan")
SilvioSoldan.setNacimiento(1935,3,26)
SilvioSoldan.setNumero(2)

OscarCordoba=Jugadores()
OscarCordoba.setNombre("Oscar Cordoba")
OscarCordoba.setNacimiento(1970,2,3)
OscarCordoba.setNumero(1)

LuisMajul=Jugadores()
LuisMajul.setNombre("Luis Miguel Majul")
LuisMajul.setNacimiento(1961,5,19)
LuisMajul.setNumero(11)

NelsonCastro=Jugadores()
NelsonCastro.setNombre("Nelson Alberto Castro")
NelsonCastro.setNacimiento(1955,4,5)
NelsonCastro.setNumero(16)

MarceloBonelli=Jugadores()
MarceloBonelli.setNombre("Marcelo Boneli")
MarceloBonelli.setNacimiento(1955,10,8)
MarceloBonelli.setNumero(19)

ChoripanCC=Equipos()
ChoripanCC.setNombre("Choripan Curling Club")
ChoripanCC.setBarrio("Villa Bosch")
ChoripanCC.agregarJugador(CarlitosTevez)
ChoripanCC.agregarJugador(LioMessi)
ChoripanCC.agregarJugador(NelsonCastro)
ChoripanCC.agregarJugador(IndioSolari)
ChoripanCC.setCapitan(IndioSolari)
ChoripanCC.setDisponibilidad(0,2,True)
ChoripanCC.setDisponibilidad(1,0,True)
ChoripanCC.setDisponibilidad(2,1,True)
ChoripanCC.setDisponibilidad(3,2,True)
ChoripanCC.setDisponibilidad(4,0,True)


TrapitoCC=Equipos()
TrapitoCC.setNombre("Trapito Curling Club")
TrapitoCC.setBarrio("Coghlan")
TrapitoCC.agregarJugador(ElFlacoSchiavi)
TrapitoCC.agregarJugador(MarceloBonelli)
TrapitoCC.agregarJugador(LuisMajul)
TrapitoCC.agregarJugador(OscarCordoba)
TrapitoCC.agregarJugador(SilvioSoldan)
TrapitoCC.setCapitan(SilvioSoldan)
TrapitoCC.setDisponibilidad(0,1,True)
TrapitoCC.setDisponibilidad(1,2,True)
TrapitoCC.setDisponibilidad(2,2,True)
TrapitoCC.setDisponibilidad(3,1,True)
TrapitoCC.setDisponibilidad(4,0,True)

ChampionsLeague=Torneo()
ChampionsLeague.agregarEquipos(TrapitoCC)
ChampionsLeague.agregarEquipos(ChoripanCC)