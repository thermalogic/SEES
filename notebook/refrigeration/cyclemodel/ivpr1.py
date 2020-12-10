cycle = {}
cycle["name"] = "Ideal_VPR"
cycle["nodes"] = [{
    "name": "Evaporator to Compressor",
            "id": 1,
            "t": 0.0,
            "x": 1,
            "mdot": 0.08
 },
    {
    "name": "Compressor to  Condenser",
            "id": 2,
            "t": None,
            "x": None,
            "mdot": None
},
    {
    "name": "Condenser to Expansion Valve ",
            "id": 3,
            "t": 26.0,
            "x": 0,
            "mfdot": None
},
    {
    "name": "Expansion Valve to Evaporator",
            "id": 4,
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
