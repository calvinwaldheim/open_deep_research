"""
Architecture-specialized deep researcher that enhances the base research system
with architecture-specific prompts, search strategies, and report formatting.
"""

from typing import Optional, Dict, Any
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import HumanMessage

from .deep_researcher import (
    deep_researcher_builder,
    transform_messages_into_research_topic,
    AgentState
)
from .prompts import (
    clarify_with_user_instructions,
    lead_researcher_prompt,
    research_system_prompt,
    summarize_webpage_prompt
)
from .architecture_config import create_architecture_config
from .architecture_prompts import (
    architecture_research_topic_prompt,
    architecture_research_instructions,
    architecture_report_template
)
from .configuration import Configuration

async def architecture_transform_messages_into_research_topic(
    state: AgentState, config: RunnableConfig
) -> Dict[str, Any]:
    """
    Architecture-specific version of research topic transformation.
    Uses specialized prompts for better architecture trend research.
    """
    configurable = Configuration.from_runnable_config(config)
    
    # Extract parameters from the request
    messages = state["messages"]
    
    # Try to extract location and year from messages for customization
    location = None
    year = None
    
    # Simple extraction logic - could be enhanced
    for message in messages:
        content = message.content.lower() if hasattr(message, 'content') else str(message).lower()
        
        # Extract location hints
        location_keywords = {
            'new york': 'New York, USA',
            'california': 'California, USA', 
            'london': 'London, UK',
            'tokyo': 'Tokyo, Japan',
            'paris': 'Paris, France',
            'berlin': 'Berlin, Germany',
            'sydney': 'Sydney, Australia',
            'toronto': 'Toronto, Canada',
            'usa': 'United States',
            'europe': 'Europe',
            'asia': 'Asia'
        }
        
        for keyword, location_value in location_keywords.items():
            if keyword in content:
                location = location_value
                break
        
        # Extract year hints
        import re
        year_match = re.search(r'20(2[4-9]|3[0-5])', content)  # 2024-2035
        if year_match:
            year = int(year_match.group())
    
    # Create architecture-specific configuration
    arch_config = create_architecture_config(
        location=location,
        year=year or 2025,
        industry_focus="Architecture & Construction"
    )
    
    # Use architecture-specific prompt
    enhanced_prompt = arch_config.get_enhanced_research_prompt(
        messages=messages,
        date=configurable.get_today()
    )
    
    # Get the research topic using enhanced prompt
    model_config = {
        "model": configurable.research_topic_gen_model,
        "max_tokens": configurable.research_topic_gen_model_max_tokens,
    }
    
    configurable_model = configurable.get_model()
    
    try:
        research_topic = await configurable_model.with_config(model_config).ainvoke([
            HumanMessage(content=enhanced_prompt)
        ])
        
        return {
            "research_topic": research_topic.content,
            "messages": state["messages"] + [research_topic],
            "architecture_config": arch_config  # Store for later use
        }
        
    except Exception as e:
        # Fallback to original method if enhancement fails
        return await transform_messages_into_research_topic(state, config)

async def architecture_final_report_generation(state: AgentState, config: RunnableConfig):
    """
    Architecture-specific final report generation with enhanced formatting and structure.
    """
    configurable = Configuration.from_runnable_config(config)
    
    # Get architecture configuration from state or create default
    arch_config = state.get("architecture_config")
    if not arch_config:
        arch_config = create_architecture_config()
    
    research_findings = ""
    if state.get("research_findings"):
        for finding in state["research_findings"]:
            research_findings += f"\n\n{finding}\n\n"
    
    research_brief = state.get("research_topic", "Architecture trend analysis")
    
    # Use architecture-specific report template
    final_report_prompt = arch_config.get_report_template(
        research_brief=research_brief,
        findings=research_findings,
        date=configurable.get_today()
    )
    
    model_config = {
        "model": configurable.final_report_model,
        "max_tokens": configurable.final_report_model_max_tokens,
    }
    
    configurable_model = configurable.get_model()
    
    try:
        final_report = await configurable_model.with_config(model_config).ainvoke([
            HumanMessage(content=final_report_prompt)
        ])
        
        # Enhance the report with architecture-specific formatting
        enhanced_report = enhance_architecture_report(final_report.content, arch_config)
        
        return {
            "final_report": enhanced_report,
            "messages": [final_report],
        }
        
    except Exception as e:
        return {
            "final_report": f"Error generating architecture trend report: {e}",
            "messages": [],
        }

def enhance_architecture_report(report_content: str, arch_config) -> str:
    """
    Post-process the generated report to ensure it meets architecture-specific standards.
    """
    
    # Add architecture-specific enhancements
    enhancements = []
    
    # Add disclaimer about trends and implementation
    disclaimer = """
---
**Important Note:** This report provides trend analysis based on current market research. 
Implementation recommendations should be validated with local building codes, climate conditions, 
and budget constraints. Consult with licensed architects and engineers for specific projects.
---
"""
    
    # Add metadata section
    metadata = f"""
**Report Generated:** {arch_config.get_validation_criteria()['content_requirements']}
**Focus Area:** {arch_config.industry_focus}
**Geographic Scope:** {arch_config.location}
**Time Frame:** {arch_config.year}
"""
    
    # Combine enhancements with original report
    enhanced_report = f"{metadata}\n\n{report_content}\n\n{disclaimer}"
    
    return enhanced_report

# Create architecture-specific research system
def create_architecture_research_system():
    """
    Create a specialized research system for architecture trends.
    """
    
    # Clone the base builder
    arch_builder = deep_researcher_builder.get_graph().copy()
    
    # Replace specific nodes with architecture-enhanced versions
    arch_builder.nodes["transform_messages_into_research_topic"] = architecture_transform_messages_into_research_topic
    arch_builder.nodes["final_report_generation"] = architecture_final_report_generation
    
    return arch_builder.compile()

# Enhanced research instructions for architecture researchers
def get_enhanced_research_instructions():
    """
    Get architecture-specific research instructions to replace the default ones.
    """
    return architecture_research_instructions

# Architecture-specific search query enhancement
def enhance_search_queries_for_architecture(base_queries: list, location: str = None, year: int = None) -> list:
    """
    Enhance search queries with architecture-specific terms and filters.
    """
    enhanced_queries = []
    
    architecture_terms = [
        "architecture trends",
        "building design innovation", 
        "sustainable construction",
        "smart building technology",
        "green architecture",
        "modular construction",
        "prefab housing",
        "energy efficient buildings",
        "LEED certified projects",
        "biophilic design"
    ]
    
    for query in base_queries:
        # Add architecture context to each query
        for term in architecture_terms[:3]:  # Use top 3 most relevant terms
            enhanced_query = f"{query} {term}"
            if location:
                enhanced_query += f" {location}"
            if year:
                enhanced_query += f" {year}"
            enhanced_queries.append(enhanced_query)
    
    return enhanced_queries

# Quality validation for architecture reports
def validate_architecture_report_quality(report_content: str, arch_config) -> Dict[str, Any]:
    """
    Validate that the generated report meets architecture-specific quality standards.
    """
    validation_criteria = arch_config.get_validation_criteria()
    
    results = {
        "passes_validation": True,
        "issues": [],
        "recommendations": []
    }
    
    # Check content requirements
    content_req = validation_criteria["content_requirements"]
    
    # Count trends mentioned (simple heuristic)
    trend_count = report_content.lower().count("trend")
    if trend_count < content_req["minimum_trends"]:
        results["issues"].append(f"Report mentions {trend_count} trends, minimum required: {content_req['minimum_trends']}")
        results["passes_validation"] = False
    
    # Check for required sections
    for section in content_req["required_sections"]:
        if section.lower() not in report_content.lower():
            results["issues"].append(f"Missing required section: {section}")
            results["passes_validation"] = False
    
    # Check quality indicators
    quality_indicators = validation_criteria["quality_indicators"]
    
    # Check for specific project examples
    if quality_indicators["specific_project_examples"]:
        if "project" not in report_content.lower() and "building" not in report_content.lower():
            results["recommendations"].append("Consider adding specific project examples")
    
    # Check for cost information
    if quality_indicators["cost_information"]:
        cost_terms = ["cost", "$", "budget", "price", "expensive", "affordable"]
        if not any(term in report_content.lower() for term in cost_terms):
            results["recommendations"].append("Consider adding cost analysis and budget implications")
    
    return results 