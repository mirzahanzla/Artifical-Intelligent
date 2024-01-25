from unicodedata import name


class RuleBasedInferenceEngine:
    def _init_(self):
        self.conditions = {
            "car_cranks_normally": False,
            "smell_of_gasoline": False,
            "nothing_happens": False
        }

    def ask_question(self, question):
        user_input = input(question + " (yes/no/na): ").lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            return None

    def execute_rule(self, rule, action):
        if all(self.conditions[condition] == rule[condition] for condition in rule):
            print("Recommended Action:", action)
            return True
        return False

    def start_inference(self):
        # Rule 1
        self.conditions["car_cranks_normally"] = self.ask_question("Does the car crank normally?")
        self.conditions["smell_of_gasoline"] = self.ask_question("Is the smell of gasoline present while trying to start the car?")
        self.execute_rule({"car_cranks_normally": True, "smell_of_gasoline": True}, "Wait 10 minutes, restart flooded car")

        # Rule 2
        self.conditions["smell_of_gasoline"] = self.ask_question("Is the smell of gasoline present while trying to start the car?")
        self.execute_rule({"car_cranks_normally": True, "smell_of_gasoline": False}, "Refuel the car")

        # Rule 3
        self.conditions["nothing_happens"] = self.ask_question("Does nothing happen when trying to start the car?")
        self.execute_rule({"nothing_happens": True}, "Recharge or replace the battery")

engine = RuleBasedInferenceEngine()
engine.start_inference()
# if _name_ == _"main"_:
#     engine = RuleBasedInferenceEngine()
#     engine.start_inference()