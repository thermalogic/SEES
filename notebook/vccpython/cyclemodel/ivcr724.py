cycle = {}
cycle["name"] = "The Ideal VCR Example 7.2-4"
cycle["nodes"] = [{
    "name": "Evaporator to Compressor",
            "id": 1,
            "p": None,
            "t": -10.0,
            "x": 1,
            "mdot": 0.08
},
    {
    "name": "Compressor to Condenser",
            "id": 2,
            "p": None,
            "t": None,
            "x": None,
            "mdot": None
},
    {
    "name": "Condenser to Expansion Valve ",
            "id": 3,
            "p": 0.9,
            "t": None,
            "x": 0,
            "mfdot": None
},
    {
    "name": "Expansion Valve to Evaporator",
            "id": 4,
            "p": None,
            "t": None,
            "x": None,
            "mdot": None
}
]

cycle["comps"] = [
    {
        "name": "Compressor",
        "devtype": "COMPRESSOR",
        "iNode": 1,
        "oNode": 2
    },
    {
        "name": "Condenser",
        "devtype": "CONDENSER",
        "iNode": 2,
        "oNode": 3
    },
    {
        "name": "Expansion Valve ",
        "devtype": "EXPANSIONVALVE",
        "iNode": 3,
        "oNode": 4
    },
    {
        "name": "Evaporator",
        "devtype": "EVAPORATOR",
        "iNode": 4,
        "oNode": 1
    }
]
