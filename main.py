from RulesHandler.RulesService import RulesService

rules_path = "./Data/rules.json"
logs_path = "./Data/logs.txt"
output_path = "./Data/output.txt"

if __name__ == '__main__':
    rs = RulesService()
    rs.config_rules(rules_path)
    rs.apply_rules(logs_path, output_path)
