# simple inquiry example
import bluetooth

class Scanner:
    def __init__(self, duration=5) -> None:
        self._result = None
        self.duration = duration

    def scan(self):
        nearby_devices = bluetooth.discover_devices(duration=self.duration, lookup_names=True)
        self._result = dict(nearby_devices)
        return nearby_devices
    
    def __str__(self):
        if self._result is None or len(self._result.keys())==0:
            output = "not found yet."
        else:
            output = "\n".join([f'{name} => {mac}' for mac,name in self._result.items()])
        return output

    @property
    def result(self):
        return self._result
            
if __name__=="__main__":
    scanner = Scanner()
    scanner.scan()
    print(scanner.result)