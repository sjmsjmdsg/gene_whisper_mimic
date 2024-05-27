from crewai import Crew
from gene_whisper_mimic.whisper_tasks import *
from gene_whisper_mimic.whisper_agents import *
import os


with open(r'D:\PycharmProj\science_digital\ini_file\OpenAI\openaikey.txt', 'r') as file_r:
    key = file_r.readline()
os.environ["OPENAI_API_KEY"] = key


class GeneWhisperMimic:

    @staticmethod
    def run(query):
        qs_agent = gene_expert()
        qs_task = answer_question(qs_agent, query)

        crew = Crew(
            agents=[qs_agent],
            tasks=[qs_task],
            verbose=True,
        )
        result = crew.kickoff()
        return result


if __name__ == '__main__':
    query = input("Enter your query: ")
    result = GeneWhisperMimic.run(query)
    print(result)
