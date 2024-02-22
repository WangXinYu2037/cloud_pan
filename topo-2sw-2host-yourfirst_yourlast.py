from mininet.topo import Topo

class MyTopo(Topo):
    
    def build(self):
        # add hosts
        N1 = self.addHost("N1")
        N2 = self.addHost("N2")
        N3 = self.addHost("N3")
        N4 = self.addHost("N4")
        N5 = self.addHost("N5")
        N6 = self.addHost("N6")

        # add switches
        S1 = self.addSwitch("S1")
        S2 = self.addSwitch("S2")

        # add links
        self.addLink(N1, S1)
        self.addLink(N2, S1)
        self.addLink(N6, S1)

        self.addLink(N3, S2)
        self.addLink(N4, S2)
        self.addLink(N5, S2)

        self.addLink(S1, S2)

topos = {"mytopo":(lambda : MyTopo())}