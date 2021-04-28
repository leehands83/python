
class SuperMario:
        def __init__(self):
            self.pos = 10
        def forward(self):
            self.pos = self.pos + 20


mario = SuperMario()
mario2 = SuperMario()
mario.forward()
print(mario.pos)
mario.__init__()
mario.forward()
mario2.forward()
mario2.forward()

print('mario:',mario.pos)
print(mario2.pos)
