from televisores.tv import TV
class Control:
     def enlazar(self, televisor):
        self._tv = televisor
        self._tv.setControl(self)
        
     def getTv(self):
        return self._tv
    
     def setTv(self, televisor):
        self.enlazar (televisor) 


     def canalUp(self):
        if self._tv:
            self._tv.canalUp()

     def canalDown(self):
        if self._tv:
            self._tv.canalDown()

     def turnOn(self):
        if self._tv:
            self._tv.turnOn()
    
     def turnOff(self):
        if self._tv:
            self._tv.turnOff()

     def volumenUp(self):
        if self._tv:
            self._tv.volumenUp()
    
     def volumenDown(self):
        if self._tv:
            self._tv.volumenDown()
    
     def setCanal(self, canal):
        if self._tv:
            self._tv.setCanal(canal)
    
     def setVolumen(self, volumen):
        if self._tv and self._tv.getEstado():
            self._tv.setVolumen(volumen)
            
