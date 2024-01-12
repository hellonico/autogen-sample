import constants
import autogen

task="""
Tell me a joke
"""

groupchat = autogen.GroupChat(agents=[constants.user_proxy, constants.assistant, constants.coder ], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=constants.llm_config_mistral)
constants.user_proxy.initiate_chat(manager, message=task)