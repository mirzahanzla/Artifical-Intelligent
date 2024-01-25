class InferenceEngine:
    def __init__(self):
        self.rules = {}

    def add_rule(self, conditions, action):
        self.rules[tuple(conditions)] = action

    def infer(self, conditions):
        for rule_conditions, action in self.rules.items():
            if all(conditions.get(cond, 0) >= value for cond, value in rule_conditions):
                return action
        return None


# Example usage:
if __name__ == "__main__":
    car_rules_engine = InferenceEngine()

    # Adding rules
    car_rules_engine.add_rule([("hot", 1)], "turn thermostat down")
    car_rules_engine.add_rule([("not hot", 0), ("window open", 1)], "close the window")
    car_rules_engine.add_rule([("thermostat down", 1), ("cold", 1)], "open the window")

    # Asking questions and dynamically inferring the result
    user_conditions = {}
    break_flag = False

    questions = [{"hot": "Are you hot? "},
                 {"window open": "Is the window open?  "},
                 {"thermostat down": "Is the thermostat down? "},
                 {"cold": "Are you cold? "}
                 ]

    for question_dict in questions:
        if break_flag:
            break
        for key, value in question_dict.items():
            user_conditions[key] = int(input(f"{value} (0: no, 1: yes): "))
            result = car_rules_engine.infer(user_conditions)
            if result:
                print(f"Action to be taken: {result}")
                break_flag = True
                break
            # print(f"Key: {key}, Value: {value}"