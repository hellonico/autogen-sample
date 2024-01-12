import constants
import autogen

task="""
Write a python scripts that count from 1 to 10, then get 'Assistant' to execute it.
"""

groupchat = autogen.GroupChat(agents=[constants.user_proxy, constants.coder, constants.assistant], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=constants.llm_config_mistral)
constants.user_proxy.initiate_chat(manager, message=task)