class vehicule:
	compteur = 0
	
	def __init__(self):
		self.moteur="thermique"
		self.capacite_reservoir=None
		self.consommation=None
		self.prix=None
		compteur += 1
	
		
class voiture(vehicule):
	def __init__(self):
		self.moteur="thermique"
		self.capacite_reservoir=40
		self.consommation=7
		self.prix=20000
		self.nb_airbags=2
		self.gps=True
		
		
	def autonomie(self):
		"""autonomie en km"""
		autonomie=self.capacite_reservoir/self.consommation*100
		return autonomie
	
	def decote_voiture(self,distance):
		"""prend en argument la distance parcourue en km par le véhicule et renvoie sa valeur actualisée"""
		return self.prix-0.15*distance
	
		
		"""super(voiture, self).__init__()"""

class bus(vehicule):
	def __init__(self):
		self.moteur="thermique"
		self.capacite_reservoir=300
		self.consommation=20
		self.prix=100000
		self.nb_roues=8
		self.articule=True
		
	def decote_bus(self,distance):
		"""prend en argument la distance parcourue en km par le véhicule et renvoie sa valeur actualisée"""
		return self.prix-0.08*distance
		
	def getConsommation(self):
		return self.consommation
		
renault=voiture()
autonomie_renault=renault.autonomie()
print("autonomie de la Renault :",autonomie_renault)

mercedes=bus()
decote=mercedes.decote_bus(25000)
print("nouveau prix du bus :",decote)

	
	

	
