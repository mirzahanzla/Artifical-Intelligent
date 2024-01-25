class InterferenceEngine:
    def _init_(self):
        pass

    def make_decision(self, temperature, window_state):
        decision_matrix = {
            ("hot", "window not open"): "Turn thermostat down",
            ("not hot", "window  open"): "Close the window",
            ("cold", "thermostat is down"): "Open the window",
            
        }
        key = (temperature, window_state)
        return decision_matrix.get(key, " Unable to make decision.")

car_engine = InterferenceEngine()

#Usage cases
# Case 1
temp_ex1 = "hot"
window_ex1 = "window not open"
action_ex1 = car_engine.make_decision(temp_ex1, window_ex1)
print("Case 1: ")
print(f"Temperature: {temp_ex1}, Window State: {window_ex1}, Recommended Action: {action_ex1}")

# Case 2
temp_ex2 = "not hot"
window_ex2 = "window  open"
action_ex2 = car_engine.make_decision(temp_ex2, window_ex2)
print("Case 2: ")
print(f"Temperature: {temp_ex2}, Window State: {window_ex2}, Recommended Action: {action_ex2}")

# Case 3
temp_ex3 = "cold"
window_ex3 = "thermostat is down"
action_ex3 = car_engine.make_decision(temp_ex3, window_ex3)
print("Case 3: ")
print(f"Temperature: {temp_ex3}, Thermostat : {window_ex3}, Recommended Action: {action_ex3}")

# Case 4
temp_ex4 = "random text"
window_ex4 = "random text"
action_ex4 = car_engine.make_decision(temp_ex4, window_ex4)
print("Case 4: ")
print(f"Temperature: {temp_ex4}, Window State: {window_ex4}, Recommended Action: {action_ex4}")