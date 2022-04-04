ies = []
ies.append({ "ie_value" : "Cause", "presence" : "Mandatory", "reference" : "7.7.1"})
ies.append({ "ie_value" : "Reordering required", "presence" : "Conditional", "reference" : "7.7.6"})
ies.append({ "ie_value" : "Recovery", "presence" : "Optional", "reference" : "7.7.11"})
ies.append({ "ie_value" : "Tunnel Endpoint Identifier Data I", "presence" : "Conditional", "reference" : "7.7.13"})
ies.append({ "ie_value" : "Tunnel Endpoint Identifier Control Plane", "presence" : "Conditional", "reference" : "7.7.14"})
ies.append({ "ie_value" : "NSAPI", "presence" : "Optional", "reference" : "7.7.17"})
ies.append({ "ie_value" : "Charging ID", "presence" : "Conditional", "reference" : "7.7.26"})
ies.append({ "ie_value" : "End User Address", "presence" : "Conditional", "reference" : "7.7.27"})
ies.append({ "ie_value" : "Protocol Configuration Options", "presence" : "Optional", "reference" : "7.7.31"})
ies.append({ "ie_value" : "GGSN Address for Control Plane", "presence" : "Conditional", "reference" : "7.7.32"})
ies.append({ "ie_value" : "GGSN Address for user traffic", "presence" : "Conditional", "reference" : "7.7.32"})
ies.append({ "ie_value" : "Alternative GGSN Address for Control Plane", "presence" : "Conditional", "reference" : "7.7.32"})
ies.append({ "ie_value" : "Alternative GGSN Address for user traffic", "presence" : "Conditional", "reference" : "7.7.32"})
ies.append({ "ie_value" : "Quality of Service Profile", "presence" : "Conditional", "reference" : "7.7.34"})
ies.append({ "ie_value" : "Charging Gateway Address", "presence" : "Optional", "reference" : "7.7.44"})
ies.append({ "ie_value" : "Alternative Charging Gateway Address", "presence" : "Optional", "reference" : "7.7.44"})
ies.append({ "ie_value" : "Common Flags", "presence" : "Optional", "reference" : "7.7.48"})
ies.append({ "ie_value" : "APN Restriction", "presence" : "Optional", "reference" : "7.7.49"})
ies.append({ "ie_value" : "MS Info Change Reporting Action", "presence" : "Optional", "reference" : "7.7.80"})
ies.append({ "ie_value" : "Bearer Control Mode", "presence" : "Optional", "reference" : "7.7.83"})
ies.append({ "ie_value" : "Evolved Allocation/Retention Priority I", "presence" : "Optional", "reference" : "7.7.91"})
ies.append({ "ie_value" : "Extended Common Flag", "presence" : "Optional", "reference" : "7.7.93"})
ies.append({ "ie_value" : "CSG Information Reporting Action", "presence" : "Optional", "reference" : "7.7.95"})
ies.append({ "ie_value" : "APN-AMBR", "presence" : "Optional", "reference" : "7.7.98"})
ies.append({ "ie_value" : "GGSN Back-Off Time", "presence" : "Optional", "reference" : "7.7.102"})
ies.append({ "ie_value" : "Extended Common Flags II", "presence" : "Optional", "reference" : "7.7.118"})
msg_list[key]["ies"] = ies
