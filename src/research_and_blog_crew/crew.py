from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

#define the class of the our crew

@CrewBase
class ResearchAndBlogCrew():

    agents: list[BaseAgent]
    tasks: list[Task]

    #define the paths of the config files 
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    #=========== Agents =============
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["report_generator"]
        )

    @agent
    def blog_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["blog_writer"]
            
        )
    # ============== TASK ================
    # order of task definition matters


    @task
    def report_task(self) -> Task:
        return Task(
            config=self.tasks_config["report_task"]
        )

    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config=self.tasks_config["blog_writing_task"], 
            output_file="blogs/blog.md"
        )

    # ================ Crew ===================
    
    @crew
    def crew(self) -> Crew:
        # Creates the ResearchAndBlogCrew crew
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True, #verbose shows the ouput in terminal
        )
