import importlib

def menu():
    print("\nGuardrails")
    print("1. instruction guardrails")
    print("2. scope guardrails")
    print("3. safety guardrails")
    print("4. behavior guardrails")
    print("5. output format guardrails")
    print("6. fallback guardrails")
    print("7. input guardrails")
    print("8. output validation guardrails")
    print("9. application guardrails")
    print("10. escalation guardrails")
    print("11. privacy guardrails")
    print("12. tool action guardrails")
    print("13. combined guardrails")
    print("14. bias, fairness, and ethical risks")
    print("15. controlling LLM behavior")
    print("q. quit")

def main():
    while True:
        menu()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'q' or choice == 'exit':
            print("Exiting program...")
            break

        module_map = {
            '1': 'examples.13_01_instruction_guardrails',
            '2': 'examples.13_02_scope_guardrails',
            '3': 'examples.13_03_safety_guardrails',
            '4': 'examples.13_04_behavior_guardrails',
            '5': 'examples.13_05_output_format_guardrails',
            '6': 'examples.13_06_fallback_guardrails',
            '7': 'examples.13_07_input_guardrails',
            '8': 'examples.13_08_output_validation_guardrails',
            '9': 'examples.13_09_application_guardrails',
            '10': 'examples.13_10_escalation_guardrails',
            '11': 'examples.13_11_privacy_guardrails',
            '12': 'examples.13_12_tool_action_guardrail_workflow',
            '13': 'examples.13_13_combined_guardrail_workflow',
            '14': 'examples.14_bias_fairness_ethics',
            '15': 'examples.15_controlling_llm_behavior',
        }

        if choice in module_map:
            module = importlib.import_module(module_map[choice])
            if hasattr(module, "main"):
                module.main()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()