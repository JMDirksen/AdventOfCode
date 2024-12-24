from enum import Enum


def main():
    inputfile = "input.txt"  # example.txt / input.txt
    with open(inputfile) as f:
        input = f.read()
    print(part1(input))


def part1(input):
    inputs = {}
    gates = []

    # Setup inputs & gates
    for line in input.splitlines():
        if ":" in line:
            name, value = line.split(": ")
            inputs[name] = bool(int(value))
        if ">" in line:
            wireA, type, wireB, _, wireC = line.split(" ")
            gates.append(Gate(GateType[type], wireA, wireB, wireC))

    # Set inputs to gates
    for gate in gates:
        if gate.wireA in inputs:
            gate.set_inputA(inputs[gate.wireA])
        if gate.wireB in inputs:
            gate.set_inputB(inputs[gate.wireB])

    # Iterage gate changes
    change = True
    while change:
        change = False
        for gate in gates:
            if not gate.active:
                if gate.inputA is None:
                    for gate2 in gates:
                        if gate2.active and gate2.wireC == gate.wireA:
                            gate.set_inputA(gate2.output)
                            change = True
                if gate.inputB is None:
                    for gate2 in gates:
                        if gate2.active and gate2.wireC == gate.wireB:
                            gate.set_inputB(gate2.output)
                            change = True

    # Get zxx values
    zValues = []
    for x in range(100):
        nr = str(x)
        if len(nr) == 1:
            nr = "0" + nr
        wire = f"z{nr}"

        if wire in inputs:
            zValues.append(inputs[wire])
        else:
            for gate in gates:
                if gate.active and gate.wireC == wire:
                    zValues.append(gate.get_output())

    # Binary to decimal
    decimal = 0
    b = 1
    for v in zValues:
        if v: decimal += b
        b *= 2

    return decimal


class GateType(Enum):
    AND = 1
    OR = 2
    XOR = 3


class Gate:
    def __init__(self, type: GateType, wireA: str, wireB: str, wireC: str):
        self.type = type
        self.wireA = wireA
        self.wireB = wireB
        self.wireC = wireC
        self.active = False
        self.inputA = None
        self.inputB = None
        self.output = None

    def set_inputA(self, value):
        self.inputA = bool(value)
        self.on_change()

    def set_inputB(self, value):
        self.inputB = bool(value)
        self.on_change()

    def on_change(self):
        if self.inputA is not None and self.inputB is not None:
            self.calc()
            self.active = True

    def calc(self):
        match self.type:
            case GateType.AND:
                self.output = self.inputA and self.inputB

            case GateType.OR:
                self.output = self.inputA or self.inputB

            case GateType.XOR:
                self.output = self.inputA ^ self.inputB

    def get_output(self):
        return self.output

main()
