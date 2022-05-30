class Node(object):
    def __init__(self, condition="", value="123", number=100):
        self.kids = []
        self.condition = condition
        self.value = value
        self.number = number

    def add_node(self, new_node):
        self.kids.append(new_node)

    def run(self, dict):
        if len(self.kids) == 0:
            return self.value
        else:
            for i in self.kids:
                if i.condition == dict[self.number]:
                    return i.run(dict)


def main(a):
    nodemain = Node(number=1)
    node1 = Node(condition=2005, number=2)
    node2 = Node(condition=1998, number=0)
    node3 = Node(condition=1999, number=2)

    node11 = Node(condition=1997, number=3)
    node12 = Node(condition=1959, value=2)
    node21 = Node(condition='D', value=3)
    node22 = Node(condition='AGDA', number=2)
    node23 = Node(condition='MQL4', number=2)
    node31 = Node(condition=1997,value=8)
    node32 = Node(condition=1959, number=0)

    node111 = Node(condition=1983, value=0)
    node112 = Node(condition=2013, value=1)
    node221 = Node(condition=1997, value=4)
    node222 = Node(condition=1959, value=5)
    node231 = Node(condition=1997, value=6)
    node232 = Node(condition=1959, value=7)
    node321 = Node(condition='D', value=9)
    node322 = Node(condition='AGDA', value=10)
    node323 = Node(condition='MQL4', value=11)


    nodemain.add_node(node1)
    nodemain.add_node(node2)
    nodemain.add_node(node3)

    node1.add_node(node11)
    node11.add_node(node111)
    node11.add_node(node112)
    node1.add_node(node12)

    node2.add_node(node21)
    node2.add_node(node22)
    node2.add_node(node23)
    node22.add_node(node221)
    node22.add_node(node222)
    node23.add_node(node231)
    node23.add_node(node232)

    node3.add_node(node31)
    node3.add_node(node32)
    node32.add_node(node321)
    node32.add_node(node322)
    node32.add_node(node323)

    return nodemain.run(a)