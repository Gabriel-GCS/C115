from mininet.topo import Topo

class MyTopo( Topo ):
    "3 host 2 switch 2 host custom topology"

    def _init_( self ):
        "Create custom topo."

        # Initialize topology
        Topo._init_( self )

        # Add hosts and switches
        firstSwitch = self.addSwitch( 's1')
        rightSwitch = self.addSwitch( 's2')
        rightSwitch2 = self.addSwitch( 's3')
        leftSwitch = self.addSwitch( 's4')
        leftSwitch2 = self.addSwitch( 's5')
        hosth1 = self.addHost( 'h1' )
        hosth2 = self.addHost( 'h2' )
        hosth3 = self.addHost( 'h3' )
        hosth4 = self.addHost( 'h4' )
        hosth5 = self.addHost( 'h5' )
        hosth6 = self.addHost( 'h6' )
        hosth7 = self.addHost( 'h7' )
        hosth8 = self.addHost( 'h8' )
        hosth9 = self.addHost( 'h9' )
        hosth10 = self.addHost( 'h10' )

        # Add links
        self.addLink(rightSwitch, firstSwitch )
        self.addLink(right2Switch, firstSwitch )
        self.addLink(leftSwitch, firstSwitch )
        self.addLink(left2Switch, firstSwitch )
        self.addLink(hosth9, rightSwitch )
        self.addLink(hosth8, rightSwitch )
        self.addLink(hosth1, rightSwitch )
        self.addLink(hosth10, right2Switch )
        self.addLink(hosth2, right2Switch )
        self.addLink(hosth3, right2Switch )
        self.addLink(hosth7, leftSwitch )
        self.addLink(hosth6, left2Switch )
        self.addLink(hosth4, left2Switch )
        self.addLink(hosth5, left2Switch )

topos = { 'mytopo': ( lambda: MyTopo() ) }