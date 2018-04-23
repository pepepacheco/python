class Persona:
    def __init__(self, id, firstName, lastName, email, gender, date):
        self.id        = id
        self.firstName = firstName
        self.lastName  = lastName
        self.email     = email
        self.gender    = gender
        self.date      = date

    def toString (self):
        return "persona: " + self.lastName + ", " + self.firstName

#persona = Persona(1, "manuel", "molino", "man@fjjf.es", "v", "fecha")
#print (persona.toString())
