# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, List, Optional, Any
from rasa_sdk.forms import FormValidationAction
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ValidateModuleForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_module_form"

    async def required_slots(
        self,
        domain_slots: List[Text],
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Text]:
        additional_slots = []
        
        updated_slots = domain_slots.copy()
                
        if tracker.slots.get("module") == "embedded C programming" and tracker.slots.get("confirm") == "yes":
            additional_slots += ["q1e", "q2e", "q3e", "q4e", "q5e", "q6e", "q7e", "q8e", "q9e", "q10e", "ql1e", "ql2e", "ql3e", "ql4e", "ql5e"]
        if tracker.slots.get("module") == "thermodynamics" and tracker.slots.get("confirm") == "yes":
            additional_slots += ["q1t", "q2t", "q3t", "q4t", "q5t", "q6t", "q7t", "q8t", "q9t", "q10t", "ql1t", "ql2t", "ql3t", "ql4t", "ql5t"]
        if tracker.slots.get("module") == "NSS" and tracker.slots.get("confirm") == "yes":
            additional_slots += ["nss" + str(n) for n in range(1,29)]
            
        if tracker.slots.get("nss_optional") == "yes":
            available_slots = ["nss" + str(n) for n in range(1,50) + "_opt"]
            additional_slots += np.sample(available_slots, 10)
        
        if tracker.slots.get("nss27") != None:
            additional_slots.append("nss_optional")
            
        if tracker.slots.get("ql5e") == "yes":
            additional_slots.append("ql5eb")
            
        if tracker.slots.get("q10e") == "yes":
            additional_slots.append("q10eb")
            
        if tracker.slots.get("ql5t") == "yes":
            additional_slots.append("ql5tb")
            
        if tracker.slots.get("q10t") == "yes":
            additional_slots.append("q10tb")
        
        text_of_last_user_message = tracker.latest_message.get("text")

        return additional_slots + updated_slots

    def validate_module(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "module":
            if not "." in slot_value:
                return {"module": None}
            slot_value = slot_value[:-1].lower().split(" ")
            if "embedded" in slot_value:
                return {"module": "embedded C programming"}
            elif "thermodynamics" in slot_value:
                return {"module": "thermodynamics"}
            elif "nss" in slot_value or "exit" in slot_value:
                return {"module": "NSS"}
            else:
                return {"module": None}
        
        return {"module": tracker.slots.get("module")}
        
    def validate_confirm(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "confirm":
            if not "." in slot_value:
                return {"confirm": None}
            slot_value = slot_value[:-1].lower().split(" ")
            if "no" in slot_value or "incorrect" in slot_value:
                return {"confirm": None, "module": None}
            elif "yes" in slot_value or "correct" in slot_value:
                return {"confirm": "yes"}
        
        return {"confirm": tracker.slots.get("confirm")}
        
    def validate_nss_optional(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss_optional":
            if not "." in slot_value:
                return {"nss_optional": None}
            slot_value = slot_value[:-1].lower().split(" ")
            if "no" in slot_value or "don't" in slot_value:
                return {"nss_optional": "no"}
            elif "yes" in slot_value or "sure" in slot_value or "ok" in slot_value:
                return {"nss_optional": "yes"}
        
        return {"nss_optional": tracker.slots.get("nss_optional")}
        
        
    def validate_ql1e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql1e":
            if not "." in slot_value:
                return {"ql1e": None}
        return {"ql1e": tracker.slots.get("ql1e")}
                
    def validate_ql2e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql2e":
            if not "." in slot_value:
                return {"ql2e": None}
        return {"ql2e": tracker.slots.get("ql2e")}
                
    def validate_ql3e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql3e":
            if not "." in slot_value:
                return {"ql3e": None}
        return {"ql3e": tracker.slots.get("ql3e")}
                
    def validate_ql4e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql4e":
            if not "." in slot_value:
                return {"ql4e": None}
        return {"ql4e": tracker.slots.get("ql4e")}
        
    def validate_ql5e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if tracker.slots["requested_slot"] != "ql5e":
            return {"ql5e": tracker.slots.get("ql5e")}
        if not "." in slot_value:
            return {"ql5e": None}
            
        slot_value = slot_value[:-1].lower().split(" ")
        
        if "yes" in slot_value or ("do" in slot_value and len(slot_value) < 4):
            return {"ql5e": "yes"}
        else:
            return {"ql5e": "no"}
                            
    def validate_ql5eb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql5b":
            if not "." in slot_value:
                return {"ql5eb": None}
        return {"ql5eb": tracker.slots.get("ql5eb")}
        
    def validate_q1e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q1e":
            if not "." in slot_value:
                return {"q1e": None}
        return {"q1e": tracker.slots.get("q1e")}
                    
    def validate_q2e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q2e":
            if not "." in slot_value:
                return {"q2e": None}
        return {"q2e": tracker.slots.get("q2e")}
                    
    def validate_q3e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q3e":
            if not "." in slot_value:
                return {"q3e": None}
        return {"q3e": tracker.slots.get("q3e")}
                    
    def validate_q4e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q4e":
            if not "." in slot_value:
                return {"q4e": None}
        return {"q4e": tracker.slots.get("q4e")}
                    
    def validate_q5e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q5e":
            if not "." in slot_value:
                return {"q5e": None}
        return {"q5e": tracker.slots.get("q5e")}
                    
    def validate_q6e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q6e":
            if not "." in slot_value:
                return {"q6e": None}
        return {"q6e": tracker.slots.get("q6e")}
                    
    def validate_q7e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q7e":
            if not "." in slot_value:
                return {"q7e": None}
        return {"q7e": tracker.slots.get("q7e")}
                    
    def validate_q8e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q8e":
            if not "." in slot_value:
                return {"q8e": None}
        return {"q8e": tracker.slots.get("q8e")}
                    
    def validate_q9e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q9e":
            if not "." in slot_value:
                return {"q9e": None}
        return {"q9e": tracker.slots.get("q9e")}
        
    def validate_q10e(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if tracker.slots["requested_slot"] != "q10e":
            return {"q10e": tracker.slots.get("q10e")}
        slot_value = slot_value[:-1].lower().split(" ")
        
        if "yes" in slot_value or ("do" in slot_value and len(slot_value) < 4):
            return {"q10e": "yes"}
        else:
            return {"q10e": "no"}
                    
    def validate_q10eb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q10eb":
            if not "." in slot_value:
                return {"q10eb": None}
        return {"q10eb": tracker.slots.get("q10eb")}
        
    def validate_ql1t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql1t":
            if not "." in slot_value:
                return {"ql1t": None}
        return {"ql1t": tracker.slots.get("ql1t")}
                
    def validate_ql2t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql2t":
            if not "." in slot_value:
                return {"ql2t": None}
        return {"ql2t": tracker.slots.get("ql2t")}
                
    def validate_ql3t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql3t":
            if not "." in slot_value:
                return {"ql3t": None}
        return {"ql3t": tracker.slots.get("ql3t")}
                
    def validate_ql4t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql4t":
            if not "." in slot_value:
                return {"ql4t": None}
        return {"ql4t": tracker.slots.get("ql4t")}
        
    def validate_ql5t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if tracker.slots["requested_slot"] != "ql5t":
            return {"ql5t": tracker.slots.get("ql5t")}
        if not "." in slot_value:
            return {"ql5t": None}
            
        slot_value = slot_value[:-1].lower().split(" ")
        
        if "yes" in slot_value or ("do" in slot_value and len(slot_value) < 4):
            return {"ql5t": "yes"}
        else:
            return {"ql5t": "no"}
                            
    def validate_ql5tb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "ql5tb":
            if not "." in slot_value:
                return {"ql5tb": None}
        return {"ql5tb": tracker.slots.get("ql5tb")}
        
    def validate_q1t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q1t":
            if not "." in slot_value:
                return {"q1t": None}
        return {"q1t": tracker.slots.get("q1t")}
                    
    def validate_q2t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q2t":
            if not "." in slot_value:
                return {"q2t": None}
        return {"q2t": tracker.slots.get("q2t")}
                    
    def validate_q3t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q3t":
            if not "." in slot_value:
                return {"q3t": None}
        return {"q3t": tracker.slots.get("q3t")}
                    
    def validate_q4t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q4t":
            if not "." in slot_value:
                return {"q4t": None}
        return {"q4t": tracker.slots.get("q4t")}
                    
    def validate_q5t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q5t":
            if not "." in slot_value:
                return {"q5t": None}
        return {"q5t": tracker.slots.get("q5t")}
                    
    def validate_q6t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q6t":
            if not "." in slot_value:
                return {"q6t": None}
        return {"q6t": tracker.slots.get("q6t")}
                    
    def validate_q7t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q7t":
            if not "." in slot_value:
                return {"q7t": None}
        return {"q7t": tracker.slots.get("q7t")}
                    
    def validate_q8t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q8t":
            if not "." in slot_value:
                return {"q8t": None}
        return {"q8t": tracker.slots.get("q8t")}
                    
    def validate_q9t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q9t":
            if not "." in slot_value:
                return {"q9t": None}
        return {"q9t": tracker.slots.get("q9t")}
        
    def validate_q10t(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        if tracker.slots["requested_slot"] != "q10t":
            return {"q10t": tracker.slots.get("q10t")}
        slot_value = slot_value[:-1].lower().split(" ")
        
        if "yes" in slot_value or ("do" in slot_value and len(slot_value) < 4):
            return {"q10t": "yes"}
        else: # "do" in slot_value or "have" in slot_value or "yes" in slot_value:
            return {"q10t": "no"}
                    
    def validate_q10tb(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "q10tb":
            if not "." in slot_value:
                return {"q10tb": None}
        return {"q10tb": tracker.slots.get("q10tb")}
                    
    def validate_nss1(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss1":
            if not "." in slot_value:
                return {"nss1": None}
        return {"nss1": tracker.slots.get("nss1")}
                    
    def validate_nss2(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss2":
            if not "." in slot_value:
                return {"nss2": None}
        return {"nss2": tracker.slots.get("nss2")}
                    
    def validate_nss3(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss3":
            if not "." in slot_value:
                return {"nss3": None}
        return {"nss3": tracker.slots.get("nss3")}
                    
    def validate_nss4(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss4":
            if not "." in slot_value:
                return {"nss4": None}
        return {"nss4": tracker.slots.get("nss4")}
                    
    def validate_nss5(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss5":
            if not "." in slot_value:
                return {"nss5": None}
        return {"nss5": tracker.slots.get("nss5")}
                    
    def validate_nss6(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss6":
            if not "." in slot_value:
                return {"nss6": None}
        return {"nss6": tracker.slots.get("nss6")}
                    
    def validate_nss7(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss7":
            if not "." in slot_value:
                return {"nss7": None}
        return {"nss7": tracker.slots.get("nss7")}
                    
    def validate_nss8(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss8":
            if not "." in slot_value:
                return {"nss8": None}
        return {"nss8": tracker.slots.get("nss8")}
                    
    def validate_nss9(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss9":
            if not "." in slot_value:
                return {"nss9": None}
        return {"nss9": tracker.slots.get("nss9")}
                    
    def validate_nss10(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss10":
            if not "." in slot_value:
                return {"nss10": None}
        return {"nss10": tracker.slots.get("nss10")}
                    
    def validate_nss11(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss11":
            if not "." in slot_value:
                return {"nss11": None}
        return {"nss11": tracker.slots.get("nss11")}
                    
    def validate_nss12(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss12":
            if not "." in slot_value:
                return {"nss12": None}
        return {"nss12": tracker.slots.get("nss12")}
                    
    def validate_nss13(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss13":
            if not "." in slot_value:
                return {"nss13": None}
        return {"nss13": tracker.slots.get("nss13")}
                    
    def validate_nss14(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss14":
            if not "." in slot_value:
                return {"nss14": None}
        return {"nss14": tracker.slots.get("nss14")}
                    
    def validate_nss15(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss15":
            if not "." in slot_value:
                return {"nss15": None}
        return {"nss15": tracker.slots.get("nss15")}
                    
    def validate_nss16(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss16":
            if not "." in slot_value:
                return {"nss16": None}
        return {"nss16": tracker.slots.get("nss16")}
                    
    def validate_nss17(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss17":
            if not "." in slot_value:
                return {"nss17": None}
        return {"nss17": tracker.slots.get("nss17")}
                    
    def validate_nss18(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss18":
            if not "." in slot_value:
                return {"nss18": None}
        return {"nss18": tracker.slots.get("nss18")}
                    
    def validate_nss19(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss19":
            if not "." in slot_value:
                return {"nss19": None}
        return {"nss19": tracker.slots.get("nss19")}
                    
    def validate_nss20(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss20":
            if not "." in slot_value:
                return {"nss20": None}
        return {"nss20": tracker.slots.get("nss20")}
                    
    def validate_nss21(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss21":
            if not "." in slot_value:
                return {"nss21": None}
        return {"nss21": tracker.slots.get("nss21")}
                    
    def validate_nss22(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss22":
            if not "." in slot_value:
                return {"nss22": None}
        return {"nss22": tracker.slots.get("nss22")}
                    
    def validate_nss23(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss23":
            if not "." in slot_value:
                return {"nss23": None}
        return {"nss23": tracker.slots.get("nss23")}
                    
    def validate_nss24(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss24":
            if not "." in slot_value:
                return {"nss24": None}
        return {"nss24": tracker.slots.get("nss24")}
                    
    def validate_nss25(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss25":
            if not "." in slot_value:
                return {"nss25": None}
        return {"nss25": tracker.slots.get("nss25")}
                    
    def validate_nss26(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss26":
            if not "." in slot_value:
                return {"nss26": None}
        return {"nss26": tracker.slots.get("nss26")}
                    
    def validate_nss27(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss27":
            if not "." in slot_value:
                return {"nss27": None}
        return {"nss27": tracker.slots.get("nss27")}
                    
    def validate_nss28(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss28":
            if not "." in slot_value:
                return {"nss28": None}
        return {"nss28": tracker.slots.get("nss28")}
                    
    def validate_nss1_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss1_opt":
            if not "." in slot_value:
                return {"nss1_opt": None}
        return {"nss1_opt": tracker.slots.get("nss1_opt")}
                    
    def validate_nss2_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss2_opt":
            if not "." in slot_value:
                return {"nss2_opt": None}
        return {"nss2_opt": tracker.slots.get("nss3_opt")}
                    
    def validate_nss3_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss3_opt":
            if not "." in slot_value:
                return {"nss3_opt": None}
        return {"nss3_opt": tracker.slots.get("nss3_opt")}
                    
    def validate_nss4_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss4_opt":
            if not "." in slot_value:
                return {"nss4_opt": None}
        return {"nss4_opt": tracker.slots.get("nss4_opt")}
                    
    def validate_nss5_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss5_opt":
            if not "." in slot_value:
                return {"nss5_opt": None}
        return {"nss5_opt": tracker.slots.get("nss5_opt")}
                    
    def validate_nss6_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss6_opt":
            if not "." in slot_value:
                return {"nss6_opt": None}
        return {"nss6_opt": tracker.slots.get("nss6_opt")}
                    
    def validate_nss7_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss7_opt":
            if not "." in slot_value:
                return {"nss7_opt": None}
        return {"nss7_opt": tracker.slots.get("nss7_opt")}
                    
    def validate_nss8_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss8_opt":
            if not "." in slot_value:
                return {"nss8_opt": None}
        return {"nss8_opt": tracker.slots.get("nss8_opt")}
                    
    def validate_nss9_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss9_opt":
            if not "." in slot_value:
                return {"nss9_opt": None}
        return {"nss9_opt": tracker.slots.get("nss9_opt")}
                    
    def validate_nss10_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss10_opt":
            if not "." in slot_value:
                return {"nss10_opt": None}
        return {"nss10_opt": tracker.slots.get("nss10_opt")}
                    
    def validate_nss11_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss11_opt":
            if not "." in slot_value:
                return {"nss11_opt": None}
        return {"nss11_opt": tracker.slots.get("nss11_opt")}
                    
    def validate_nss12_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss12_opt":
            if not "." in slot_value:
                return {"nss12_opt": None}
        return {"nss12_opt": tracker.slots.get("nss12_opt")}
                    
    def validate_nss13_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss13_opt":
            if not "." in slot_value:
                return {"nss13_opt": None}
        return {"nss13_opt": tracker.slots.get("nss13_opt")}
                    
    def validate_nss14_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss14_opt":
            if not "." in slot_value:
                return {"nss14_opt": None}
        return {"nss14_opt": tracker.slots.get("nss14_opt")}
                    
    def validate_nss15_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss15_opt":
            if not "." in slot_value:
                return {"nss15_opt": None}
        return {"nss15_opt": tracker.slots.get("nss15_opt")}
                    
    def validate_nss16_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss16_opt":
            if not "." in slot_value:
                return {"nss16_opt": None}
        return {"nss166_opt": tracker.slots.get("nss16_opt")}
                    
    def validate_nss17_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss17_opt":
            if not "." in slot_value:
                return {"nss17_opt": None}
        return {"nss17_opt": tracker.slots.get("nss17_opt")}
                    
    def validate_nss18_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss18_opt":
            if not "." in slot_value:
                return {"nss18_opt": None}
        return {"nss18_opt": tracker.slots.get("nss18_opt")}
                    
    def validate_nss19_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss19_opt":
            if not "." in slot_value:
                return {"nss19_opt": None}
        return {"nss19_opt": tracker.slots.get("nss19_opt")}
                    
    def validate_nss20_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss20_opt":
            if not "." in slot_value:
                return {"nss20_opt": None}
        return {"nss20_opt": tracker.slots.get("nss20_opt")}
                    
    def validate_nss21_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss21_opt":
            if not "." in slot_value:
                return {"nss21_opt": None}
        return {"nss21_opt": tracker.slots.get("nss21_opt")}
                    
    def validate_nss22_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss22_opt":
            if not "." in slot_value:
                return {"nss22_opt": None}
        return {"nss22_opt": tracker.slots.get("nss22_opt")}
                    
    def validate_nss23_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss23_opt":
            if not "." in slot_value:
                return {"nss23_opt": None}
        return {"nss23_opt": tracker.slots.get("nss23_opt")}
                    
    def validate_nss24_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss24_opt":
            if not "." in slot_value:
                return {"nss24_opt": None}
        return {"nss24_opt": tracker.slots.get("nss24_opt")}
                    
    def validate_nss25_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss25_opt":
            if not "." in slot_value:
                return {"nss25_opt": None}
        return {"nss25_opt": tracker.slots.get("nss25_opt")}
                    
    def validate_nss26_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss26_opt":
            if not "." in slot_value:
                return {"nss26_opt": None}
        return {"nss26_opt": tracker.slots.get("nss26_opt")}
                    
    def validate_nss27_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss27_opt":
            if not "." in slot_value:
                return {"nss27_opt": None}
        return {"nss27_opt": tracker.slots.get("nss27_opt")}
                    
    def validate_nss28_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss28_opt":
            if not "." in slot_value:
                return {"nss28_opt": None}
        return {"nss28_opt": tracker.slots.get("nss28_opt")}
                    
    def validate_nss29_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss29_opt":
            if not "." in slot_value:
                return {"nss29_opt": None}
        return {"nss29_opt": tracker.slots.get("nss29_opt")}
                    
    def validate_nss30_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss30_opt":
            if not "." in slot_value:
                return {"nss30_opt": None}
        return {"nss30_opt": tracker.slots.get("nss30_opt")}
                    
    def validate_nss31_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss31_opt":
            if not "." in slot_value:
                return {"nss31_opt": None}
        return {"nss31_opt": tracker.slots.get("nss31_opt")}
                    
    def validate_nss32_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss32_opt":
            if not "." in slot_value:
                return {"nss32_opt": None}
        return {"nss32_opt": tracker.slots.get("nss32_opt")}
                    
    def validate_nss33_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss33_opt":
            if not "." in slot_value:
                return {"nss33_opt": None}
        return {"nss33_opt": tracker.slots.get("nss33_opt")}
                    
    def validate_nss34_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss34_opt":
            if not "." in slot_value:
                return {"nss34_opt": None}
        return {"nss34_opt": tracker.slots.get("nss34_opt")}
                    
    def validate_nss35_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss35_opt":
            if not "." in slot_value:
                return {"nss35_opt": None}
        return {"nss35_opt": tracker.slots.get("nss35_opt")}
                    
    def validate_nss36_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss36_opt":
            if not "." in slot_value:
                return {"nss36_opt": None}
        return {"nss36_opt": tracker.slots.get("nss36_opt")}
                    
    def validate_nss37_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss37_opt":
            if not "." in slot_value:
                return {"nss37_opt": None}
        return {"nss37_opt": tracker.slots.get("nss37_opt")}
                    
    def validate_nss38_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss38_opt":
            if not "." in slot_value:
                return {"nss38_opt": None}
        return {"nss38_opt": tracker.slots.get("nss38_opt")}
                    
    def validate_nss39_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss39_opt":
            if not "." in slot_value:
                return {"nss39_opt": None}
        return {"nss39_opt": tracker.slots.get("nss39_opt")}
                    
    def validate_nss40_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss40_opt":
            if not "." in slot_value:
                return {"nss40_opt": None}
        return {"nss40_opt": tracker.slots.get("nss40_opt")}
                    
    def validate_nss41_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss41_opt":
            if not "." in slot_value:
                return {"nss41_opt": None}
        return {"nss41_opt": tracker.slots.get("nss41_opt")}
                    
    def validate_nss42_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss42_opt":
            if not "." in slot_value:
                return {"nss42_opt": None}
        return {"nss42_opt": tracker.slots.get("nss42_opt")}
                    
    def validate_nss43_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss43_opt":
            if not "." in slot_value:
                return {"nss43_opt": None}
        return {"nss43_opt": tracker.slots.get("nss43_opt")}
                    
    def validate_nss44_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss44_opt":
            if not "." in slot_value:
                return {"nss44_opt": None}
        return {"nss44_opt": tracker.slots.get("nss44_opt")}
                    
    def validate_nss45_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss45_opt":
            if not "." in slot_value:
                return {"nss45_opt": None}
        return {"nss45_opt": tracker.slots.get("nss45_opt")}
                    
    def validate_nss46_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss46_opt":
            if not "." in slot_value:
                return {"nss46_opt": None}
        return {"nss46_opt": tracker.slots.get("nss46_opt")}
                    
    def validate_nss47_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss47_opt":
            if not "." in slot_value:
                return {"nss47_opt": None}
        return {"nss47_opt": tracker.slots.get("nss47_opt")}
                    
    def validate_nss48_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss48_opt":
            if not "." in slot_value:
                return {"nss48_opt": None}
        return {"nss48_opt": tracker.slots.get("nss48_opt")}
                    
    def validate_nss49_opt(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> Dict[Text, Any]:
        """Validate value."""
        if tracker.slots["requested_slot"] == "nss49_opt":
            if not "." in slot_value:
                return {"nss49_opt": None}
        return {"nss49_opt": tracker.slots.get("nss49_opt")}
