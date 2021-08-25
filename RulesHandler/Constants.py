import operator

# operations
eq = 'eq'
operators = {eq: operator.eq}

# log headers
message_header = 'message'
type_header = 'type'
severity_header = 'severity'
id_header = 'id'

# rule headers
field_header = 'field'
operation_header = 'operation'
value_header = 'value'

# list for the headers of each rule and each log
rule_headers = [field_header, operation_header, value_header]
log_headers = [message_header, type_header, severity_header, id_header]




