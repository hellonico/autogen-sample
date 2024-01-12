import autogen

config_list_mistral = [
    {
        'base_url' : "http://0.0.0.0:8000",
        'api_key' : "NULL",
        'model': "mistral",
    }
]

config_list_codellama = [
    {
        'base_url' : "http://0.0.0.0:14657",
        'api_key' : "NULL",
        'model': "ollama/codellama",
    }
]

llm_config_mistral = {
    "config_list": config_list_mistral,
}
llm_config_codellama = {
    "config_list": config_list_codellama,
}
assistant = autogen.AssistantAgent(
    name="Assistant",
    llm_config=llm_config_mistral
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config_codellama
)
user_proxy = autogen.UserProxyAgent(
    name="userproxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content","").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config_mistral,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
    Otherwise, reply CONTINUE, or the reason why the task is not solved yet.
    """
)