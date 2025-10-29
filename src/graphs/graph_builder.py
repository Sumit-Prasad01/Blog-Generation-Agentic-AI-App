from langgraph.graph import StateGraph, START, END
from src.llms.groq_llm import GroqLLM
from src.states.blog_state import BlogState
from src.nodes.blog_node import BlogNode


class GraphBuilder:

    def __init__(self, llm):

        self.llm = llm
        self.graph = StateGraph(BlogState)

    
    def build_top_graph(self):
        """
        Build a graph to generates blogs based on provided topic.

        """

        self.blog_node_obj = BlogNode(self.llm)

        # Nodes 
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)

        # Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph
    

    def build_language_graph(self):
        """
        Build a graph for blog generation with inputs topic and language.
        
        """

        self.blog_node_obj = BlogNode(self.llm)

        # Nodes
        self.graph.add_node("title_creation", self.blog_node_obj.title_creation)
        self.graph.add_node("content_generation", self.blog_node_obj.content_generation)
        self.graph.add_node("hindi_translation", lambda state: self.blog_node_obj.translation({**state, "current_language" : "hindi"}))
        self.graph.add_node("french_translation", lambda state: self.blog_node_obj.translation({**state, "current_language" : "french"}))
        self.graph.add_node("route", self.blog_node_obj.route)

        # Edges 
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", "route")

        # Conditional edges
        self.graph.add_conditional_edges(
            "route",
            self.blog_node_obj.route_decision,
                {
                    "hindi" : "hindi_translation",
                    "french" : "french_translation"
                }
            )

        self.graph.add_edge("hindi_translation", END)
        self.graph.add_edge("french_translation", END)

        return self.graph


    
    def setup_graph(self, usecase):

        if usecase == "topic":
            self.build_top_graph()

        if usecase == "language":
            self.build_language_graph()
        
        return self.graph.compile()

# LangSmith LangGraph Studio
    
llm = GroqLLM().get_llm()

graph_builder = GraphBuilder(llm)
graph = graph_builder.build_language_graph().compile()