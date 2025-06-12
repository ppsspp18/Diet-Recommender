from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from dotenv import load_dotenv
load_dotenv()
@CrewBase
class DietRecommender():
    """DietRecommender crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def text_corrector(self) -> Agent:
        return Agent(
            config=self.agents_config['text_corrector'], # type: ignore[index]
            verbose=True
        )
    @agent
    def health_parameter_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['health_parameter_extractor'], # type: ignore[index]
            verbose=True
        )
    @agent 
    def diet_planner(self) -> Agent:
        return Agent(
            config=self.agents_config['diet_planner'], # type: ignore[index]
            verbose=True
        )


    @task
    def text_correction_task(self) -> Task:
        return Task(
            config=self.tasks_config['text_correction_task'], # type: ignore[index]
        )
    @task
    def health_parameter_extraction_task(self) -> Task:
        return Task(
            config=self.tasks_config['health_parameter_extraction_task'], # type: ignore[index]
        )
    @task
    def diet_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['diet_planning_task'], # type: ignore[index]
            output_file = 'veg_diet_plan.md',
        )
    @task
    def diet_planning_task2(self) -> Task:
        return Task(
            config=self.tasks_config['diet_planning_task2'], # type: ignore[index]
            output_file = 'nonveg_diet_plan.md',
        )

    @crew
    def crew(self) -> Crew:
        """Creates the DietRecommender crew"""

        selected_tasks = []

        print("---------------------------------------------------------------\n")
        print("Are you vegeterian or non vegeterian ? ")
        print("1. vegeterian")
        print("2. non vegeterian")
        choice = input("Enter your choice 1 or 2: ")

        if choice == '1':
            selected_tasks.append(self.text_correction_task())
            selected_tasks.append(self.health_parameter_extraction_task())
            selected_tasks.append(self.diet_planning_task())
        elif choice == '2':
            selected_tasks.append(self.text_correction_task())
            selected_tasks.append(self.health_parameter_extraction_task())
            selected_tasks.append(self.diet_planning_task2())

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=selected_tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
