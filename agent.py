from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-3.5-flash',
    name='math_tutor_agent', #Un nombre más específico
    description='Ayuda a los estudiantes a aprender algebra guiandolos a traves de los pasos para la resolucion de problemas.',
    instruction='Eres un tutor de matematicas paciente. Ayuda a los estudiantes con los problemas de algebra.',
)
